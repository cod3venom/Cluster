CREATE TABLE IF NOT EXISTS AWS_PRODUCTS(
    ID INT  PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(250) NOT NULL,
    LINK VARCHAR(1000) NOT NULL,
    TITLE VARCHAR(1000) NOT NULL,
    SELLER VARCHAR(1000) NOT NULL,
    SELLER_LINK VARCHAR(1000) NOT NULL,
    OFFER_RATING VARCHAR(10),
    OFFER_PRICE VARCHAR(50) NOT NULL,
    OFFER_SHIPPING_INFO VARCHAR(500),
    OFFER_SHORT_DESCRIPTION TEXT,
    PRODUCT_INFO_TABLE_KEY TEXT,
    PRODUCT_INFO_TABLE_VALUE TEXT,
    PRODUCT_DESCRIPTION TEXT,
    PRODUCT_FROM_MANUFACTURER TEXT,
    INDEX `IDX_ID` (ID)
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS AWS_CUSTOMERS_WHO_REVIEWED_TITLE(
    ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(350) NOT NULL,
    TITLE VARCHAR(2000) NOT NULL,
    INDEX `IDX_ID` (ID)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS AWS_CUSTOMERS_WHO_REVIEWED_LINK(
    ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(350) NOT NULL,
    LINK VARCHAR(2000) NOT NULL,
    INDEX `IDX_ID` (ID)
) ENGINE=INNODB;
CREATE TABLE IF NOT EXISTS AWS_CUSTOMERS_WHO_REVIEWED_IMAGE(
    ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(350) NOT NULL,
    IMAGE VARCHAR(2000) NOT NULL,
    INDEX `IDX_ID` (ID)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS AWS_CUSTOMERS_WHO_REVIEWED_PRICE(
    ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(350) NOT NULL,
    PRICE VARCHAR(50) NOT NULL,
    INDEX `IDX_ID` (ID)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS AWS_CUSTOMERS_WHO_REVIEWED_STARS(
    ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(350) NOT NULL,
    STARS VARCHAR(50) NOT NULL,
    INDEX `IDX_ID` (ID)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS AWS_PRODUCT_REVIEW_USER(
    ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(350) NOT NULL,
    USERNAME VARCHAR(100) NOT NULL,
    INDEX `IDX_ID` (ID)
) ENGINE=INNODB;
CREATE TABLE IF NOT EXISTS AWS_PRODUCT_REVIEW_USER_LINK(
    ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(350) NOT NULL,
    LINK VARCHAR(100) NOT NULL,
    INDEX `IDX_ID` (ID)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS AWS_PRODUCT_REVIEW_USER_AVATAR(
    ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(350) NOT NULL,
    AVATAR VARCHAR(100) NOT NULL,
    INDEX `IDX_ID` (ID)
) ENGINE=INNODB;
CREATE TABLE IF NOT EXISTS AWS_PRODUCT_REVIEW_USER_STARS(
    ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(350) NOT NULL,
    STARS VARCHAR(100) NOT NULL,
    INDEX `IDX_ID` (ID)
) ENGINE=INNODB;
CREATE TABLE IF NOT EXISTS AWS_PRODUCT_REVIEW_USER_LOCATION_DATE(
    ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(350) NOT NULL,
    DATE VARCHAR(100) NOT NULL,
    INDEX `IDX_ID` (ID)
) ENGINE=INNODB;
CREATE TABLE IF NOT EXISTS AWS_PRODUCT_REVIEW_USER_COMMENT(
    ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    HASHID VARCHAR(350) NOT NULL,
    COMMENT TEXT NOT NULL,
    INDEX `IDX_ID` (ID)
) ENGINE=INNODB;
