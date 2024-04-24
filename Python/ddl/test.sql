
SELECT 'Test pyencrypt' title;
DROP TABLE IF EXISTS test_pyencrypt;
CREATE TEMP TABLE test_pyencrypt ON COMMIT PRESERVE ROWS AS
SELECT CID, pyencrypt(p.CID , 'test-password') ecid, CCID FROM hdc_cmi.PERSON p LIMIT 10;

SELECT * FROM test_pyencrypt;

SELECT  pydecrypt(ecid, 'test-password') cid, ecid  FROM test_pyencrypt;
DROP TABLE IF EXISTS test_pyencrvaypt;

SELECT 'Test Base64 Encoding' title;
select 'test-test-encode' ptxt,  vb64encode('test-test-encode') entext,  vb64decode(vb64encode('test-test-encode') ) detext;

SELECT 'Test thaimod11' title;
SELECT '1234567890123' cid_f, thaimod11('1234567890123') f, '1893535345732' cid_t, thaimod11('1893535345732') t;