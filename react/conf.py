from optional_django import conf


class Conf(conf.Conf):
    # The devtool that webpack uses when bundling components
    DEVTOOL = None

    # A JavaScript regex which is used to test if a file should have the babel
    # loader run over it
    TRANSLATE_TEST = '/.jsx?$/'

    JS_HOST_FUNCTION = 'react'

settings = Conf()