-- Test that award amounts are non-negative
SELECT award_internal_id, award_amount
FROM {{ ref('fct_award_spend') }}
WHERE award_amount < 0
