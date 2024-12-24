with source as (

    select * from {{ source('commodities', 'movimentacao_commodities') }}

),

renamed as (

    select
        date,
        symbol as ticker,
        action as acao,
        quantity as quantidade
    from
        source

)

select * from renamed