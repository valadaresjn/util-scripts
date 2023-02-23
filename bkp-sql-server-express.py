#Backup SQL Server Express
#Author: João Neto Valadares - @valadaresjn

import time, os, zipfile, zlib
from datetime import datetime

#pega data do sistema
hoje = datetime.today()
dia = hoje.day
mes = hoje.month
ano = hoje.year

#guarda dia mes e ano separados por '-'
data = str(dia)+"-"+str(mes)+"-"+str(ano)

#caminho do arquivo com o SQL
path_arquivo_sql = 'G:\\Backup_dir\\script\\up.sql'

#lista de databases para o backup
databases = ['BD1','BD2']
def geraSQL(bd, arquivo):
	
	sql = "BACKUP DATABASE ["+bd+"] TO DISK = N'G:\Backup_dir\script\\"+bd+"_"+data+".bak' WITH NOFORMAT, INIT, NAME = N'Backup diario "+bd+"', SKIP, NOREWIND, NOUNLOAD, STATS = 10\nGO"
	try:
		arq = open(arquivo, "w")
		#grava SQL que sera executado pelo sqlcmd no arquivo up.sql para ca base de dados
		arq.write(sql)
		arq.close()
		
	except Exception as ex:
		print ('Erro: ao criar SQL da base '+databases[x]+' ', ex)

def fazBackup(bd, sql):
	
	#Realiza o backup ao executano a precedure (SQL) gerada anteriormente	
	print ("Realizando backup de "+bd+"...")
	os.system('sqlcmd -E -i "'+sql+'"')

def compactaBackup(arquivo_zip, arquivo_bak):
	
	#Compacta os arquivos de backup gerados pelos SQLCMD .bak em .zip
	print ("Compactando arquivos...")
	try:
		zip = zipfile.ZipFile(arquivo_zip, 'w')
		zip.write(arquivo_bak, compress_type=zipfile.ZIP_DEFLATED)
		zip.close()
	#except:
	except Exception as ex:	
			print ('Erro: Ao compactar aquivos... ', ex)
			
def removeTemp():

	os.remove('G:/Backup_dir/script/up.sql')
	os.remove('G:/Backup_dir/script/'+databases[x]+'_'+data+'.bak')
	
for x in range(len(databases)):
                        
	geraSQL(databases[x], path_arquivo_sql)

	fazBackup(databases[x], path_arquivo_sql)

	compactaBackup('G:/Backup_dir/Diario/'+databases[x]+'_'+data+'.zip', databases[x]+'_'+data+'.bak')

	removeTemp()