import os

os.getcwd()

git_example53_Path = '/home/example/lichengfeng/git/example53/'

git_example80_Path = '/home/example/lichengfeng/git6580/example80/'

git_example35m_Path = '/home/example/lichengfeng/git6735m/example35m/'

git_update_log_path = '/home/example/lichengfeng/gitUpdateLog/'

git_6753_update_log_path = git_update_log_path+'6753/'

git_6580_update_log_path = git_update_log_path+'6580/'

git_6735m_update_log_path = git_update_log_path+'6735m/'

#check if path exists
if os.path.exists(git_update_log_path):
	pass
else:
	os.mkdir(git_update_log_path)

if os.path.exists(git_6753_update_log_path):
	pass
else:
	os.mkdir(git_6753_update_log_path)

if os.path.exists(git_6580_update_log_path):
	pass
else:
	os.mkdir(git_6580_update_log_path)

if os.path.exists(git_6735m_update_log_path):
	pass
else:
	os.mkdir(git_6735m_update_log_path)


#update 6753
os.chdir(git_example53_Path)
os.system('date >> '+git_6753_update_log_path+'autogitupdate.log')
os.system('git pull origin master >> '+git_6753_update_log_path+'autogitupdate.log')

#update 6735m
os.chdir(git_example35m_Path)	
os.system('date >> '+git_6735m_update_log_path+'autogitupdate.log')
os.system('git pull origin master >> '+git_6735m_update_log_path+'autogitupdate.log')

#update 6753
os.chdir(git_example80_Path)	
os.system('date >> '+git_6580_update_log_path+'autogitupdate.log')
os.system('git pull origin master >> '+git_6580_update_log_path+'autogitupdate.log')

