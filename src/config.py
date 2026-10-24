class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='JoseElias'
    MYSQL_PASSWORD='180986'
    MYSQL_DB='api_utl'
    MYSQL_CURSORCLASS = 'Cursor'

config={
        'development':DevelopmentConfig
    }