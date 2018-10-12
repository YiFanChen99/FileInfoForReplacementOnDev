#!/usr/bin/python
import sys
import json
from DevFile import map_define


class FileMap(object):
    name = None

    @staticmethod
    def createFileMapsLeaf(name, map_define, **kwargs):
        print 'createFileMapsLeaf enter'
        if FileMap.is_group(map_define):
            return FileMapGroup(name, map_define, **kwargs)
        else:
            return FileMapFile(name, map_define, **kwargs)

    @staticmethod
    def is_group(map_define):
        return 'elements' in map_define

    def __init__(self, map_define):
        self.name = map_define['name']

    def get_file(self, filename):
        raise NotImplementedError

    def get_display_info(self):
        raise NotImplementedError

    def get_full_info(self):
        raise NotImplementedError


class FileMapGroup(FileMap):
    _extended_attr = ['pre_target', 'pre_source']
    _overwritten_attr = ['owner', 'mod']

    def __init__(self, map_define, **kwargs):
        FileMap.__init__(self, map_define)
        self._init_extended_attr(map_define, **kwargs)
        self._init_overwritten_attr(map_define, **kwargs)
        self._init_elements(map_define)

    def _init_extended_attr(self, map_define, **kwargs):
        for attr in FileMapGroup._extended_attr:
            if attr in map_define:
                setattr(self, attr, map_define[attr].format(kwargs.get(attr, "")))
            else:
                setattr(self, attr, kwargs.get(attr))

    def _init_overwritten_attr(self, map_define, **kwargs):
        for attr in FileMapGroup._overwritten_attr:
            if attr in map_define:
                setattr(self, attr, map_define[attr])
            else:
                setattr(self, attr, kwargs.get(attr))

    def _init_elements(self, map_define):
        self.sub_groups = []
        self.sub_files = {}

        for leaf_define in self._get_elements_define(map_define):
            if FileMap.is_group(leaf_define):
                self.sub_groups.append(FileMapGroup(leaf_define, **self.get_config()))
            else:
                self.sub_files[leaf_define['name']] = FileMapFile(leaf_define, **self.get_config())

    def _get_elements_define(self, map_define):
        return map_define['elements']

    def get_config(self):
        config = {}
        for attr in FileMapGroup._extended_attr:
            config[attr] = getattr(self, attr)
        for attr in FileMapGroup._overwritten_attr:
            config[attr] = getattr(self, attr)
        return config

    def get_display_info(self):
        return self.name, self.get_sub_display_info()

    def get_sub_display_info(self):
        elements = {}
        for element in self.sub_groups + self.sub_files.values():
            name, info = element.get_display_info()
            elements[name] = info
        return elements

    def find_file(self, filename):
        if filename in self.sub_files:
            return self.sub_files[filename]

        for group in self.sub_groups:
            file = group.find_file(filename)
            if file is not None:
                return file

        return None


class FileMapRoot(FileMapGroup):
    def __init__(self, map_define, **kwargs):
        self.name = "root"
        self._init_elements(map_define)

    def _init_extended_attr(self, map_define, **kwargs):
        pass

    def _init_overwritten_attr(self, map_define, **kwargs):
        pass

    def _get_elements_define(self, map_define):
        return map_define

    def get_config(self):
        config = {}
        for attr in (FileMapGroup._extended_attr + FileMapGroup._overwritten_attr):
            config[attr] = ""
        return config

    def get_display_info(self):
        return self.get_sub_display_info()


class FileMapFile(FileMap):
    _extended_attr = {
        'target': 'pre_target',
        'gz': 'pre_target',
        'default_source': 'pre_source'
    }
    _overwritten_attr = ['owner', 'mod']

    def __init__(self, map_define, **kwargs):
        super(FileMapFile, self).__init__(map_define)
        self._init_extended_attr(map_define, **kwargs)
        self._init_overwritten_attr(map_define, **kwargs)

    def _init_extended_attr(self, map_define, **kwargs):
        for attr, pre_attr in self._extended_attr.items():
            if attr in map_define:
                pre_arg = kwargs.get(pre_attr, "")
                value = map_define[attr].format(pre_arg)
                setattr(self, attr, value)

    def _init_overwritten_attr(self, map_define, **kwargs):
        for attr in FileMapFile._overwritten_attr:
            if attr in map_define:
                setattr(self, attr, map_define[attr])
            else:
                setattr(self, attr, kwargs.get(attr))

    def get_display_info(self):
        return self.name, "{ %s, %s, %s }" % (self.target, self.owner, self.mod)

    def __repr__(self):
        return "%s: %s" % (self.get_display_info())


maps = FileMapRoot(map_define)


def find_file(filename):
    """ Return the corresponding FileMap or None.

    >>> find_file('notestation.js')
    notestation.js: { /var/packages/NoteStation/target/ui/notestation.js, NoteStation:NoteStation, 644 }

    >>> find_file('wrong_filename_undefined')

    """
    return maps.find_file(filename)


def display_all():
    info = maps.get_display_info()
    print "Dev file maps:\n%s" % json.dumps(info, indent=3)


def main(argv):
    """
    Display all defined files.
    >>> main([])  # doctest: +SKIP
    >>> main(["all"])  # doctest: +SKIP

    Display corresponding file if matched. Display None otherwise.
    >>> main(["notestation.js"])
    notestation.js: { /var/packages/NoteStation/target/ui/notestation.js, NoteStation:NoteStation, 644 }
    >>> main(["wrong_filename_undefined"])
    None

    Run doctest
    >>> main(["test"])  # doctest: +SKIP
    """

    if len(argv) == 0:
        display_all()
        return

    command = argv[0]
    if (command == "test"):
        import doctest
        doctest.testmod(report=True)
        print "Complete doctest."
    elif (command == "all"):
        display_all()
    else:
        file = find_file(command)
        print file


if __name__ == '__main__':
    main(sys.argv[1:])
