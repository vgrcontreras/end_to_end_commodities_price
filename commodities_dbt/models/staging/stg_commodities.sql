with source as (

    select
        "Date",
        "Close",
        "ticker"
    from 
        {{ source('commodities', 'commodities') }}

),

renamed as (

    select
        cast("Date" as date) as data,
        "Close" as valor_fechamento,
        ticker
    from
        source

)

select * from renamed