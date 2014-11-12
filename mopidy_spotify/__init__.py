from __future__ import unicode_literals

import os

from mopidy import config, ext


__version__ = '2.0.0'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Spotify'
    ext_name = 'spotify'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()

        schema['username'] = config.String()
        schema['password'] = config.Secret()

        schema['bitrate'] = config.Integer(choices=(96, 160, 320))

        schema['timeout'] = config.Integer(minimum=0)

        schema['cache_dir'] = config.Path(optional=True)
        schema['settings_dir'] = config.Path()

        schema['toplist_countries'] = config.List(optional=True)

        schema['allow_network'] = config.Boolean()

        # TODO Add more configrations:
        # - show_playlists = true/false, requested in #25
        # - volume_normalization = true/false, requested in #13

        return schema

    def setup(self, registry):
        from mopidy_spotify.backend import SpotifyBackend

        registry.add('backend', SpotifyBackend)
