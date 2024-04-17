select version();


\set libfile '\''`pwd`'/all_pylib.py\''

CREATE OR REPLACE LIBRARY pylib AS :libfile DEPENDS '/home/dbadmin/pyenv/lib64/python3.11/site-packages' LANGUAGE 'Python';

CREATE OR REPLACE FUNCTION pyencrypt AS LANGUAGE 'Python' NAME 'pyencrypt_factory' LIBRARY pylib fenced;
CREATE OR REPLACE FUNCTION pydecrypt AS LANGUAGE 'Python' NAME 'pydecrypt_factory' LIBRARY pylib fenced;


CREATE OR REPLACE FUNCTION vb64encode AS LANGUAGE 'Python' NAME 'vb64encode_factory' LIBRARY pylib fenced;
CREATE OR REPLACE FUNCTION vb64decode AS LANGUAGE 'Python' NAME 'vb64decode_factory' LIBRARY pylib fenced;

CREATE OR REPLACE FUNCTION thaimod11 AS LANGUAGE 'Python' NAME 'thaimod11_factory' LIBRARY pylib fenced;


