/*
ONLINE_SALE 온라인 상품 판매 정보
ONLINE_SALE_ID, USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE

OFFLINE_SALE 오프라인 상품 판매 정보
OFFLINE_SALE_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE

[질문]
2022년 3월의 오프라인/온라인 상품 판매 데이터의 판매 날짜, 상품ID, 유저ID, 판매량을 출력

[결과]
OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 
판매일 ASC, 상품 ID ASC, 유저 ID ASC
*/


SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE 
WHERE SALES_DATE LIKE "%2022-03%"
UNION
SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE SALES_DATE LIKE "%2022-03%"
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID