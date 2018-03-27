#!/usr/bin/python


class File(object):
    __allowed_params = ('target', 'owner', 'mod', 'default_source')

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            if key in self.__class__.__allowed_params:
                setattr(self, key, value)

    def __repr__(self):
        return '{%s, %s, %s}' % (self.target, self.owner, self.mod)


class MapManager(object):
    @classmethod
    def update_maps(self, maps):
        for filename, properties in self.files.items():
            self.add_file(maps, filename, **properties)

    @classmethod
    def add_file(self, maps, filename, **kwargs):
        self.init_kwargs_by_defaults(kwargs)
        maps[filename] = File(**kwargs)

    @classmethod
    def init_kwargs_by_defaults(self, kwargs):
        if not hasattr(self, 'defaults'):
            return

        if ('owner' in self.defaults) and ('owner' not in kwargs):
            kwargs['owner'] = self.defaults['owner']
        if ('mod' in self.defaults) and ('mod' not in kwargs):
            kwargs['mod'] = self.defaults['mod']


class DownloadMapManager(MapManager):
    pkg_target = "/var/packages/DownloadStation/target"
    mnt_source = "/volume1/mnt/source"
    defaults = {'owner': "DownloadStation:DownloadStation", 'mod': "755"}
    files = {
        'youtube-dl': {
            'target': pkg_target + "/plugins/youtube/youtube-dl",
            'default_source': mnt_source + "/youtube-dl/youtube-dl"
        },
        'youtube.php': {
            'target': pkg_target + "/plugins/youtube/phpsrc/youtube.php",
            'default_source': mnt_source + "/DownloadStation/plugins/youtube/phpsrc/youtube.php.enc"
        },
        'download.js': {
            'target': pkg_target + "/ui/download.js",
            'mod': "644",
            'default_source': mnt_source + "/DownloadStation/ui/download.js"
        },
        # once only
        'synodlekkotool': {
            'target': pkg_target + "/bin/synodlekkotool",
            'default_source': mnt_source + "/DownloadStation/tool/ekko/synodlekkotool"
        },
        'synodldsocketd': {
            'target': pkg_target + "/bin/synodldsocketd",
            'default_source': mnt_source + "/DownloadStation/domain_socket_daemon/synodldsocketd"
        },
        'libdownloaddomainsocket.so': {
            'target': pkg_target + "/lib/libdownloaddomainsocket.so",
            'default_source': mnt_source + "/DownloadStation/lib/downloaddomainsocket/libdownloaddomainsocket.so"
        }
    }


class NoteMapManager(MapManager):
    pkg_target = "/var/packages/NoteStation/target"
    mnt_source = "/volume1/mnt/source61"
    defaults = {'owner': "NoteStation:NoteStation", 'mod': "755"}
    files = {
        'notestation.js': {
            'target': pkg_target + "/ui/notestation.js",
            'default_source': mnt_source + "/NoteStation/ui/notestation.js"
        }
    }


maps = dict()
DownloadMapManager.update_maps(maps)
NoteMapManager.update_maps(maps)


def main():
    print "Dev file maps:"
    for filename, file_info in maps.items():
        print '  %s: %s' % (repr(filename), repr(file_info))


if __name__ == '__main__':
    main()
