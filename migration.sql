INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Generating static SQL
INFO  [alembic.runtime.migration] Will assume transactional DDL.
BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

INFO  [alembic.runtime.migration] Running upgrade  -> a7cbea07959a, empty message
-- Running upgrade  -> a7cbea07959a

DROP TABLE "Article";

DROP TABLE "Publisher";

INSERT INTO alembic_version (version_num) VALUES ('a7cbea07959a');

INFO  [alembic.runtime.migration] Running upgrade a7cbea07959a -> 3645a0f5765b, empty message
-- Running upgrade a7cbea07959a -> 3645a0f5765b

DROP TABLE "Publisher";

DROP TABLE "Article";

UPDATE alembic_version SET version_num='3645a0f5765b' WHERE alembic_version.version_num = 'a7cbea07959a';

COMMIT;

