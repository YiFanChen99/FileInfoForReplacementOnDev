#!/usr/bin/python

""" Template
{
    'name': "Package",
    'pre_target': "/var/packages/",
    'pre_source': "/volume1/mnt/",
    'owner': "user:group",
    'mod': "755",
    'elements': [
        {
            'name': "notestation.js",
            'target': "{0}/ui/notestation.js",
            'owner': "user:group",
            'mod': "755",
            'default_source': "{0}/NoteStation/ui/notestation.js"
        }
    ]
}
"""


class Definer(object):
    @staticmethod
    def get_define():
        return {}


class DownloadStationDefiner(Definer):
    @staticmethod
    def get_define():
        return {
            'name': "DownloadStation",
            'pre_target': "/var/packages/DownloadStation/target",
            'pre_source': "/volume1/mnt/source",
            'owner': "DownloadStation:DownloadStation",
            'mod': "755",
            'elements': [
                DownloadStationDefiner.get_define_temp_deving(),
                {
                    'name': "download.js",
                    'target': "{0}/ui/download.js",
                    'gz': "{0}/ui/download.js.gz",
                    'mod': "644",
                    'default_source': "{0}/DownloadStation/ui/download.js"
                }, {
                    'name': "scheduler",
                    'target': "{0}/sbin/scheduler",
                    'default_source': "{0}/DownloadStation/scheduler/scheduler"
                }, {
                    'name': "transmissiond",
                    'target': "{0}/sbin/transmissiond",
                    'default_source': "{0}/transmission-2.8x/daemon/transmission-daemon"
                }, {
                    'name': "lftp",
                    'target': "{0}/bin/lftp",
                    'default_source': "{0}/lftp-4.x-virtual-DownloadStation/src/lftp"
                }, {
                    'name': "wget",
                    'target': "{0}/bin/wget",
                    'default_source': "{0}/wget-1.10.1/src/wget"
                }, {
                    'name': "wget-spider",
                    'target': "{0}/bin/wget-spider",
                    'default_source': "{0}/wget-1.14.x/src/wget-spider"
                }, {
                    'name': "style.css",
                    'target': "{0}/ui/style.css",
                    'gz': "{0}/ui/style.css.gz",
                    'mod': "644",
                    'default_source': "{0}/DownloadStation/ui/style.css"
                }, {
                    'name': "nzbget",
                    'target': "{0}/bin/nzbget",
                    'default_source': "{0}/nzbget-0.7.0/nzbget"
                }, {
                    'name': "downloadman.cgi",
                    'target': "{0}/ui/dlm/downloadman.cgi",
                    'default_source': "{0}/DownloadStation/dlm/downloadman.cgi",
                    'owner': "root:root",
                    'mod': "750",
                },
                DownloadStationDefiner.get_define_web_api(),
                DownloadStationDefiner.get_define_libs(),
                DownloadStationDefiner.get_define_hostscripts(),
                DownloadStationDefiner.get_define_btsearch(),
                DownloadStationDefiner.get_define_binary_tool(),
                DownloadStationDefiner.get_define_youtube(),
                DownloadStationDefiner.get_define_hyperbackup(),
                DownloadStationDefiner.get_define_plugins(),
            ]
        }

    @staticmethod
    def get_define_temp_deving():
        return {
            'name': "TempDeving",
            'elements': [
            ]
        }

    @staticmethod
    def get_define_web_api():
        task_bt = {
            'name': "TaskBT",
            'pre_source': "{0}/task_bt",
            'elements': [
                {
                    'name': "SYNO.DownloadStation2.Task.BT.lib",
                    'target': "{0}/SYNO.DownloadStation2.Task.BT.lib",
                    'mod': "644",
                    'default_source': "{0}/SYNO.DownloadStation2.Task.BT.lib"
                }, {
                    'name': "SYNO.DownloadStation2.Task.BT.so",
                    'target': "{0}/SYNO.DownloadStation2.Task.BT.so",
                    'default_source': "{0}/SYNO.DownloadStation2.Task.BT.so"
                }
            ]
        }
        thumbnail = {
            'name': "Thumbnail",
            'pre_source': "{0}/thumbnail",
            'elements': [
                {
                    'name': "SYNO.DownloadStation2.Thumbnail.lib",
                    'target': "{0}/SYNO.DownloadStation2.Thumbnail.lib",
                    'mod': "644",
                    'default_source': "{0}/SYNO.DownloadStation2.Thumbnail.lib"
                }, {
                    'name': "SYNO.DownloadStation2.Thumbnail.so",
                    'target': "{0}/SYNO.DownloadStation2.Thumbnail.so",
                    'default_source': "{0}/SYNO.DownloadStation2.Thumbnail.so"
                }
            ]
        }
        settings = {
            'name': "Settings",
            'pre_source': "{0}/settings",
            'elements': [
                {
                    'name': "SYNO.DownloadStation2.Settings.lib",
                    'target': "{0}/SYNO.DownloadStation2.Settings.lib",
                    'mod': "644",
                    'default_source': "{0}/SYNO.DownloadStation2.Settings.lib"
                }, {
                    'name': "SYNO.DownloadStation2.Settings.so",
                    'target': "{0}/SYNO.DownloadStation2.Settings.so",
                    'default_source': "{0}/SYNO.DownloadStation2.Settings.so"
                }
            ]
        }
        btsearch = {
            'name': "BtSearch",
            'pre_source': "{0}/btsearch",
            'elements': [
                {
                    'name': "SYNO.DownloadStation2.BTSearch.lib",
                    'target': "{0}/SYNO.DownloadStation2.BTSearch.lib",
                    'mod': "644",
                    'default_source': "{0}/SYNO.DownloadStation2.BTSearch.lib"
                }, {
                    'name': "SYNO.DownloadStation2.BTSearch.so",
                    'target': "{0}/SYNO.DownloadStation2.BTSearch.so",
                    'default_source': "{0}/SYNO.DownloadStation2.BTSearch.so"
                }
            ]
        }
        task = {
            'name': "Task",
            'pre_source': "{0}/task",
            'elements': [
                {
                    'name': "SYNO.DownloadStation2.Task.lib",
                    'target': "{0}/SYNO.DownloadStation2.Task.lib",
                    'mod': "644",
                    'default_source': "{0}/SYNO.DownloadStation2.Task.lib"
                }, {
                    'name': "SYNO.DownloadStation2.Task.so",
                    'target': "{0}/SYNO.DownloadStation2.Task.so",
                    'default_source': "{0}/SYNO.DownloadStation2.Task.so"
                }
            ]
        }

        return {
            'name': "WebApi",
            'pre_target': "{0}/webapi",
            'pre_source': "{0}/DownloadStation/webapiv5",
            'elements': [
                task_bt, thumbnail, settings, btsearch, task
            ]
        }

    @staticmethod
    def get_define_libs():
        return {
            'name': "Libs",
            'pre_target': "{0}/lib",
            'pre_source': "{0}/DownloadStation",
            'mod': "644",
            'elements': [
                {
                    'name': "libdownloaddb",
                    'target': "{0}/libdownloaddb.so",
                    'default_source': "{0}/libdownloaddb/libdownloaddb.so.1.0"
                }, {
                    'name': "libdownloaddomainsocket.so",
                    'target': "{0}/libdownloaddomainsocket.so",
                    'default_source': "{0}/lib/downloaddomainsocket/libdownloaddomainsocket.so"
                }, {
                    'name': "libsynodlupdate.so",
                    'target': "{0}/libsynodlupdate.so",
                    'default_source': "{0}/lib/update/libsynodlupdate.so"
                }, {
                    'name': "libsynodlbtsearch.so",
                    'target': "{0}/libsynodlbtsearch.so",
                    'default_source': "{0}/lib/btsearch/libsynodlbtsearch.so"
                }, {
                    'name': "libsynodlcommon.so",
                    'target': "{0}/libsynodlcommon.so",
                    'default_source': "{0}/lib/common/libsynodlcommon.so"
                }, {
                    'name': "libsynodlcore.so",
                    'target': "{0}/libsynodlcore.so",
                    'default_source': "{0}/lib/core/libsynodlcore.so"
                }
            ]
        }

    @staticmethod
    def get_define_hostscripts():
        hosts = {
            'name': "Hosts",
            'pre_target': "{0}/hosts",
            'pre_source': "{0}/hosts",
            'elements': [
                {
                    'name': "mega.php",
                    'target': "{0}/mega/mega.php",
                    'default_source': "{0}/mega/mega"
                }, {
                    'name': "mega.class.php",
                    'target': "{0}/mega/lib/mega.class.php",
                    'default_source': "{0}/mega/lib/mega.class"
                }
            ]
        }
        return {
            'name': "Hostscript",
            'pre_target': "{0}/hostscript",
            'pre_source': "{0}/DownloadStation/hostscript",
            'elements': [
                {
                    'name': "host.php",
                    'target': "{0}/host.php",
                    'default_source': "{0}/host"
                },
                hosts
            ]
        }

    @staticmethod
    def get_define_btsearch():
        plugins = {
            'name': "BtSearchPlugins",
            'pre_target': "{0}/plugins",
            'pre_source': "{0}/plugins",
            'mod': "644",
            'elements': [
                {
                    'name': "bitsoup.php",
                    'target': "{0}/bitsoup/search.php",
                    'default_source': "{0}/bitsoup/search.php"
                }
            ]
        }
        return {
            'name': "Btsearch",
            'pre_target': "{0}/btsearch",
            'pre_source': "{0}/DownloadStation/dlm/btsearch",
            'elements': [
                {
                    'name': "btsearch.php",
                    'target': "{0}/btsearch.php",
                    'default_source': "{0}/encrypted/btsearch.php"
                },
                plugins
            ]
        }

    @staticmethod
    def get_define_binary_tool():
        return {
            'name': "BinaryTool",
            'pre_target': '{0}/bin',
            'pre_source': "{0}/DownloadStation/tool",
            'elements': [
                {
                    'name': "synorsstool",
                    'target': "{0}/synorsstool",
                    'default_source': "{0}/synorsstool"
                }, {
                    'name': "synodltransmissiondsocketdevtool",
                    'target': "{0}/synodltransmissiondsocketdevtool",
                    'default_source': "{0}/transmissiondsocketdev/synodltransmissiondsocketdevtool"
                }, {
                    'name': "synodlmaxtaskslimittool",
                    'target': "{0}/synodlmaxtaskslimittool",
                    'default_source': "{0}/maxtaskslimit/synodlmaxtaskslimittool"
                }, {
                    'name': "synodlvolumechecktool",
                    'target': "{0}/synodlvolumechecktool",
                    'default_source': "{0}/volumecheck/synodlvolumechecktool"
                }, {
                    'name': "synodlupdate",
                    'target': "{0}/synodlupdate",
                    'default_source': "{0}/update/synodlupdate"
                }
            ]
        }

    @staticmethod
    def get_define_youtube():
        return {
            'name': "Youtube",
            'pre_target': '{0}/plugins/youtube',
            'elements': [
                {
                    'name': "youtube-dl",
                    'target': "{0}/youtube-dl",
                    'default_source': "{0}/youtube-dl/youtube-dl"
                }, {
                    'name': "youtube.php",
                    'target': "{0}/phpsrc/youtube.php",
                    'default_source': "{0}/DownloadStation/plugins/youtube/phpsrc/youtube.php.enc"
                }
            ]
        }

    @staticmethod
    def get_define_hyperbackup():
        return {
            'name': "Backup",
            'pre_target': "/var/packages/DownloadStation/scripts/backup/2.x",
            'pre_source': "{0}/DownloadStation/hyperbackup/2.x",
            'owner': "root:root",
            'mod': "700",
            'elements': [
                {
                    'name': "import",
                    'target': "{0}/import",
                    'default_source': "{0}/import"
                }, {
                    'name': "export",
                    'target': "{0}/export",
                    'default_source': "{0}/export"
                }, {
                    'name': "can_import",
                    'target': "{0}/can_import",
                    'default_source': "{0}/can_import"
                }, {
                    'name': "can_export",
                    'target': "{0}/can_export",
                    'default_source': "{0}/can_export"
                }, {
                    'name': "estimate_exportion",
                    'target': "{0}/estimate_exportion",
                    'default_source': "{0}/estimate_exportion"
                }, {
                    'name': "summary",
                    'target': "{0}/summary",
                    'default_source': "{0}/summary"
                }
            ]
        }

    @staticmethod
    def get_define_plugins():
        return {
            'name': "Plugins",
            'pre_target': "/var/packages/DownloadStation/target/plugins",
            'pre_source': "{0}/DownloadStation/plugins",
            'owner': "DownloadStation:DownloadStation",
            'mod': "644",
            'elements': [
                {
                    'name': "move",
                    'target': "{0}/move/move.so",
                    'default_source': "{0}/move/move.so"
                }
            ]
        }


class NoteStationDefiner(Definer):
    @staticmethod
    def get_define():
        return {
            'name': "NoteStation",
            'pre_target': "/var/packages/NoteStation/target",
            'pre_source': "/volume1/mnt/source61",
            'owner': "NoteStation:NoteStation",
            'mod': "644",
            'elements': [
                {
                    'name': "notestation.js",
                    'target': "{0}/ui/notestation.js",
                    'default_source': "{0}/NoteStation/ui/notestation.js"
                },
                NoteStationDefiner.get_define_tinymce()
            ]
        }

    @staticmethod
    def get_define_tinymce():
        return {
            'name': "TinymcePlugin",
            'elements': [
                {
                    'name': "TinymcePluginOnNS",
                    'pre_target': "{0}/ui/js/tinymce_plugins",
                    'pre_source': "{0}/NoteStation/ui/js/tinymce_plugins",
                    'elements': [
                        {
                            'name': "syno_textcolor",
                            'target': "{0}/syno_textcolor/plugin.min.js",
                            'default_source': "{0}/syno_textcolor/plugin.min.js"
                        }, {
                            'name': "syno_headingselect",
                            'target': "{0}/syno_headingselect/plugin.min.js",
                            'default_source': "{0}/syno_headingselect/plugin.min.js"
                        }
                    ]
                }, {
                    'name': "TinymcePluginOnTinymce",
                    'elements': [
                    ]
                }
            ]
        }


download_station = DownloadStationDefiner.get_define()
note_station = NoteStationDefiner.get_define()

map_define = [
    download_station, note_station
]
