WITH agencies AS (
  SELECT * FROM {{ ref('slv_agencies') }}
)

SELECT
  {{ dbt_utils.generate_surrogate_key(['awarding_agency', 'awarding_sub_agency']) }} AS agency_key,
  awarding_agency,
  awarding_sub_agency
FROM agencies
