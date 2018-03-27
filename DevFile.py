#!/usr/bin/python
map_define = [
    {
        'name': "DownloadStation",
        'pre_target': "/var/packages/DownloadStation/target",
        'pre_source': "/volume1/mnt/source",
        'owner': "DownloadStation:DownloadStation",
        'mod': "755",
        'elements': [
            {
                'name': "TempDeving",
                'elements': [
                    {
                        'name': "synodlekkotool",
                        'target': "{0}/bin/synodlekkotool",
                        'default_source': "{0}/DownloadStation/tool/ekko/synodlekkotool"
                    }, {
                        'name': "synodldsocketd",
                        'target': "{0}/bin/synodldsocketd",
                        'default_source': "{0}/DownloadStation/domain_socket_daemon/synodldsocketd"
                    }
                ]
            }, {
                'name': "download.js",
                'target': "{0}/ui/download.js",
                'mod': "644",
                'default_source': "{0}/DownloadStation/ui/download.js"
            }, {
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
        ]
    }, {
        'name': "NoteStation",
        'pre_target': "/var/packages/NoteStation/target",
        'pre_source': "/volume1/mnt/source61",
        'owner': "NoteStation:NoteStation",
        'mod': "755",
        'elements': [
            {
                'name': "notestation.js",
                'target': "{0}/ui/notestation.js",
                'default_source': "{0}/NoteStation/ui/notestation.js"
            }
        ]
    }
]
