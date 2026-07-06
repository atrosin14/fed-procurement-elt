-- Build silver view for agencies

WITH awards AS (
  SELECT * FROM {{ ref('brz_awards') }}
)

SELECT DISTINCT
  awarding_agency,
  awarding_sub_agency
FROM awards
WHERE awarding_agency IS NOT NULL
