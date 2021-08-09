import os
work_dir = "/home/wsuser/work/project_git_repo/Python-Scripts-Deployment/assets/jupyterlab"

os.chdir(work_dir)

print(os.getcwdb())

from lib.sample_class import Employee


emp_1 = Employee('Catherine', 'Cao', 'F')

print(emp_1.fullname())

