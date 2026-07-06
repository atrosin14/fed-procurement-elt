-- Building awards silver view
-- Lightweight and similar to bronze but with NULL ID protection

with awards as (
  SELECT * FROM {{ ref('brz_awards') }}
)

SELECT
  award_internal_id,
  award_id,
  recipient_uei,
  recipient_name,
  awarding_agency,
  awarding_sub_agency,
  funding_agency,
  funding_sub_agency,
  naics_code,
  psc_code,
  pop_state_code,
  pop_country_code,
  award_amount,
  total_outlays,
  start_date,
  end_date,
  last_modified_at
FROM awards
WHERE award_internal_id IS NOT NULL
