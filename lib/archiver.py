import logging, os


## settings from env/activate
LOG_PATH = os.environ['ANX_ALMA__LOG_PATH']
LOG_LEVEL = os.environ['ANX_ALMA__LOG_LEVEL']  # 'DEBUG' or 'INFO'


## logging
log_level = { 'DEBUG': logging.DEBUG, 'INFO': logging.INFO }
logging.basicConfig(
    filename=LOG_PATH, level=log_level[LOG_LEVEL],
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S'
    )
log = logging.getLogger(__name__)
log.debug( 'log setup' )


class Archiver:

    def __init__(self):
        pass

    def check_for_new_file(self, dir_path):
        """ Checks if there is a file waiting. """
        assert type(dir_path) == str
        chk_rslt = False
        contents = os.listdir( dir_path )
        assert type(contents) == list
        for item in contents:
            log.debug( f'item, ``{item}``' )
            if item.startswith( 'BUL_ANNEX' ):
                chk_rslt = True
                break
        log.debug( f'chk_rslt, ``{chk_rslt}``' )
        return chk_rslt

    # def file_check( self ):
    #     """ Sees if there is a file waiting; returns unicode-text if so.
    #         Called by process_requests() """
    #     try:
    #       file_handler = open( self.PATH_TO_SOURCE_FILE )
    #       log.info( 'annex requests found' )
    #     except Exception, e:
    #       message = 'no annex requests found; quitting\n\n'
    #       log.info( message )
    #       sys.exit( message )
    #     utf8_data = file_handler.read()
    #     assert type(utf8_data) == str, type(utf8_data)
    #     data = utf8_data.decode( 'utf-8' )
    #     return data
