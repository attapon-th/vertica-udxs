
SELECT 'Test pyencrypt' title;
SELECT 'test1' txt, pyencrypt('test1', 'test-password') cp;
SELECT 'test2' txt, pyencrypt('test2', 'test-password') cp;

SELECT 'Test pydecrypt' title;
SELECT 'test1' txt, pydecrypt('QvBb376Osh7U4741MPdV..M2Hk3H8=.SiU0LYdrECF6PrwuU0C7kQ==', 'test-password') d_text,  pydecrypt('QvBb376Osh7U4741MPdV..M2Hk3H8=.SiU0LYdrECF6PrwuU0C7kQ==', 'test-password') = 'test1' decrypt_is_success;
SELECT 'test2' txt, pydecrypt('AQwerTwngJMQRzjnhoyC..nzoBYbw=.ZQ1jNTxfPCYfZNaysLi6yw==', 'test-password') d_text, pydecrypt('AQwerTwngJMQRzjnhoyC..nzoBYbw=.ZQ1jNTxfPCYfZNaysLi6yw==', 'test-password') = 'test2' decrypt_is_success;


SELECT 'Test Base64 Encoding' title;
select 'test-test-encode' ptxt,  vb64encode('test-test-encode') entext,  vb64decode(vb64encode('test-test-encode') ) detext;

SELECT 'Test thaimod11' title;
SELECT '1234567890123' cid_f, thaimod11('1234567890123') f, '1893535345732' cid_t, thaimod11('1893535345732') t;