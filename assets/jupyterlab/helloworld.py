print("hello world")
# cd "/home/wsuser/work/project_git_repo/Python-Scripts-Deployment"
# git commit -m 'hello'
# git push -u origin master
# or using UI

from project_lib import Project
project = Project.access()

DB2onCloud_metadata = project.get_connection(name="DB2OnCloud")

import os, jaydebeapi, pandas as pd

DB2onCloud_url = 'jdbc:db2://{}:{}/{}'.format(
    DB2onCloud_metadata['host'],
    50000,
    DB2onCloud_metadata['database']
)

DB2onCloud_connection = jaydebeapi.connect(
    'com.ibm.db2.jcc.DB2Driver',
    DB2onCloud_url,
    [DB2onCloud_metadata['username'],DB2onCloud_metadata['password']]
)
   
query = 'SELECT * FROM "JPF66625"."CREDITDATA"'
data_df_1 = pd.read_sql_query(query, con=DB2onCloud_connection)
data_df_1.head()

project.save_data("save_from_jupyterlab_as_job.csv", data_df_1.to_csv(index=False))



