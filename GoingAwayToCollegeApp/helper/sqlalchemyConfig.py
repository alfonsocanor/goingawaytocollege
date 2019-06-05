class SqlAlchemyConfig():
    def config(self):
        userpass = 'mysql+pymysql://root:@'
        basedir  = '127.0.0.1'
        dbname   = '/gatcdb'
        socket   = '?unix_socket=/opt/lampp/var/mysql/mysql.sock'
        dbname   = userpass + basedir + dbname + socket
        dbname  =  dbname + socket
        return dbname