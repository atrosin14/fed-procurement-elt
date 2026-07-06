-- Build fact awards table

WITH awards AS (
  SELECT * FROM {{ ref('slv_awards') }}
)

SELECT
  --surrogate keys into the dimensions
  {{ dbt_utils.generate_surrogate_key(['recipient_uei']) }}                        AS recipient_key,
  {{ dbt_utils.generate_surrogate_key(['awarding_agency', 'awarding_sub_agency']) }} AS agency_key,

  -- degenerate dimensions
  award_internal_id,
  award_id,
  naics_code,
  psc_code,
  pop_state_code,
  pop_country_code,
  start_date,
  end_date,

  --measures
  award_amount,
  total_outlays
FROM awards
