create table PGP.AWS_PGP_OFFERS
(
    ID                        int auto_increment primary key,
    HASHID                    varchar(250) not null,
    LINK                      text         null,
    TITLE                     text         null,
    SELLER                    text         null,
    SELLER_LINK               text         null,
    OFFER_PRICE               text         null,
    OFFER_DELIVERY_INFO       text         null,
    OFFER_SHORT_DESCRIPTION   text         null,
    PRODUCT_BRAND             text         null,
    PRODUCT_MODEL_NUMBER      text         null,
    PRODUCT_COLOUR            text         null,
    PRODUCT_DIMENSIONS        text         null,
    PRODUCT_MATERIAL          text         null,
    PRODUCT_WEIGHT            text         null,
    PRODUCT_ASIN              text         null,
    PRODUCT_RATINGS           text         null,
    PRODUCT_BEST_SELLERS_RANK text         null
);

create index IDX_ID
    on PGP.AWS_PGP_OFFERS (ID);
