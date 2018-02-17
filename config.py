import web

db_host = 'tuy8t6uuvh43khkk.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'j00uc751stih03u9'
db_user = 'jowjl2uvslxqpp2y'
db_pw = 'wl6aoamaiagvg5ss'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )