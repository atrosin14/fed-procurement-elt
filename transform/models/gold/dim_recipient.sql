-- Build gold table for recipients

WITH recipients AS (
  SELECT * FROM {{ ref('slv_recipients') }}
)

SELECT
  -- Generates surrogate key based on the recipient ID
  {{ dbt_utils.generate_surrogate_key(['recipient_uei']) }} AS recipient_key,
  recipient_uei,
  recipient_name
FROM recipients
