
DROP TABLE IF EXISTS test_pyencrypt;
CREATE TEMP TABLE test_pyencrypt ON COMMIT PRESERVE ROWS AS
SELECT pyencrypt(p.CID , 'test-password') ecid FROM hdc_cmi.PERSON p  WHERE thaimod11(p.CID) = 1 LIMIT 10;

SELECT * FROM test_pyencrypt;

SELECT  pydecrypt(ecid, 'test-password') FROM test_pyencrypt;
DROP TABLE IF EXISTS test_pyencrypt;
