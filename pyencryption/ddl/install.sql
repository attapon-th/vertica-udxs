select version();


\set libfile '\''`pwd`'/src/pyencryption.py\''

\set depen '\'/home/dbadmin/pyenv/lib64/python3.11/site-packages/\''

CREATE OR REPLACE LIBRARY pyencryption AS :libfile DEPENDS :depen LANGUAGE 'Python';

CREATE OR REPLACE FUNCTION pyencrypt AS LANGUAGE 'Python' NAME 'pyencrypt_factory' LIBRARY pyencryption fenced;
CREATE OR REPLACE FUNCTION pydecrypt AS LANGUAGE 'Python' NAME 'pydecrypt_factory' LIBRARY pyencryption fenced;




