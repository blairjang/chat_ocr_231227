-- TCL 연습할 mem_TCL 테이블 만들기
CREATE TABLE mem_tcl AS SELECT mem_id, mem_name, mem_number FROM member;
SELECT * FROM mem_tcl;

-- mem_TCL 테이블에 데이터를 입력, 수정, 삭제
INSERT INTO mem_tcl VALUES ('ASP', '에스파', 4);

UPDATE mem_tcl SET mem_number = 5 WHERE mem_name = '에스파';

DELETE FROM mem_tcl WHERE mem_name = '에이핑크';

-- ROLLBACK으로 명령어 실행 취소
-- > ROLLBACK : 현재 트랜잭션에 포함된 데이터 조작 관련 명령어의 수행을 모두 취소
ROLLBACK;

SELECT * FROM mem_tcl;