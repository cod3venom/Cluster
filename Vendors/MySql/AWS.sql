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
    PRODUCT_FROM_MANUFACTURER TEXT

)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS AWS_REVIEWED_LINKS(
    ID INT PRIMARY KEY NOT NULL,
    HASHID VARCHAR(250) NOT NULL,
    LINK VARCHAR(2000) NOT NULL,
    INDEX `IDX_ID` (ID),
    CONSTRAINT `FK_ID` FOREIGN KEY (ID) REFERENCES AWS_PRODUCTS(ID) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=INNODB;