import logging, os, pathlib, shutil, sys


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

    def make_datetime_stamp( self, datetime_obj ):
        """ Creates a a time-stamp string for the files to be archived, like '2021-07-13T13-41-39' """
        iso_datestamp = datetime_obj.isoformat()
        custom_datestamp = iso_datestamp[0:19].replace( ':', '-' )  # colons to slashes to prevent filename issues
        return str( custom_datestamp )

    def copy_original_to_archives( self, source_file_path, destination_dir_path ):
        copy_result = False
        try:
            assert type(source_file_path) == str
            assert type(destination_dir_path) == str
            source_path_obj = pathlib.Path( source_file_path )
            source_filename = source_path_obj.name
            shutil.copy2( source_file_path, destination_dir_path )
            destination_filepath = f'{destination_dir_path}/{source_filename}'
            log.debug( f'destination_filepath, ``{destination_filepath}``' )
            destination_path_obj = pathlib.Path( destination_filepath )
            if destination_path_obj.exists():
                copy_result = True
        except:
            log.exception( 'problem copying original to archives' )
        log.debug( f'copy_result, ``{copy_result}``' )
        return copy_result

    # -- common ---------------------------------

    def log_and_quit( self, message ):
        """ Exits on various errors. """
        message = f'{message}\n\n'
        log.info( message )
        sys.exit( message )

## end class Archiver
