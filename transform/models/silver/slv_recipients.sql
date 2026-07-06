-- Build sliver view for distinct vendors
WITH awards AS (
  SELECT * FROM {{ ref('brz_awards') }}
)

SELECT DISTINCT
  recipient_uei,
  recipient_name
FROM awards
WHERE recipient_uei IS NOT NULL
