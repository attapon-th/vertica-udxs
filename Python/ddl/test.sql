
DROP TABLE IF EXISTS test_pyencrypt;
CREATE TEMP TABLE test_pyencrypt ON COMMIT PRESERVE ROWS AS
SELECT CID, pyencrypt(p.CID , 'test-password') ecid, CCID, thaimod11(p.CID) thaimod FROM hdc_cmi.PERSON p  WHERE thaimod11(p.CID) = 1 LIMIT 10;

SELECT * FROM test_pyencrypt;

SELECT  pydecrypt(ecid, 'test-password') cid, ecid  FROM test_pyencrypt;
DROP TABLE IF EXISTS test_pyencrvaypt;

select 'test-test-encode' ptxt,  vb64encode('test-test-encode') entext,  vb64decode(vb64encode('test-test-encode') ) detext;