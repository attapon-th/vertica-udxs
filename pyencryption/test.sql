
select pyencrypt('test', 'test-pass');


select pydecrypt(pyencrypt('test', 'test-pass'), 'test-pass');