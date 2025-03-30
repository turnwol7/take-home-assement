CREATE TABLE rewards (
        protocol VARCHAR(3),
        address VARCHAR(50),
        amount NUMERIC,
        date DATE
    );

CREATE TABLE delegators (
        protocol VARCHAR(3),
        address VARCHAR(50),
        total_figment_staked NUMERIC,
        total_staked NUMERIC
    );

INSERT INTO rewards VALUES ('AXL', 'axelar120zgt5384kj4qlrv5z7ag38efgelyfykr6xnjf', 9660870969, '01-28-2025');
INSERT INTO rewards VALUES ('AXL', 'axelar120zgt5384kj4qlrv5z7ag38efgelyfykr6xnjf', 4067270214, '02-12-2025');
INSERT INTO delegators VALUES ('AXL', 'axelar120zgt5384kj4qlrv5z7ag38efgelyfykr6xnjf', 1399400, 1399400);
INSERT INTO delegators VALUES ('INJ', 'inj19u2t52ee57yjljz0804cu5f9pwm3yeny37hx4q', 22555.86251221, 65124.84846388);
