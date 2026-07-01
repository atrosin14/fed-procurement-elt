-- Bronze layer - cleaned up column names and typed

with source as (
  SELECT *
  FROM {{source('raw', 'awards')}}
)

select
    generated_internal_id                         as award_internal_id,
    "Award ID"                                    as award_id,
    "Recipient Name"                              as recipient_name,
    "Recipient UEI"                               as recipient_uei,
    "Awarding Agency"                             as awarding_agency,
    "Awarding Sub Agency"                         as awarding_sub_agency,
    "Funding Agency"                              as funding_agency,
    "Funding Sub Agency"                          as funding_sub_agency,
    "Award Type"                                  as award_type,
    "Contract Award Type"                         as contract_award_type,
    "NAICS"                                       as naics_code,
    "PSC"                                         as psc_code,
    "Place of Performance State Code"             as pop_state_code,
    "Place of Performance Country Code"           as pop_country_code,
    cast("Award Amount" as double)                as award_amount,
    cast("Total Outlays" as double)               as total_outlays,
    cast("Start Date" as date)                    as start_date,
    cast("End Date" as date)                      as end_date,
    cast("Last Modified Date" as timestamp)       as last_modified_at
from source
