# mx-data Result Fields

Read this only when parsing raw `mx_data_*_raw.json` or explaining generated tables.

## Core Paths

- `data.questionId`: unique request id.
- `data.dataTableDTOList[]`: normalized tables. Each item usually corresponds to one security and one metric group.
- `data.rawDataTableDTOList[]`: raw tables with the same general shape.
- `data.condition`: query conditions inferred by MX.
- `data.entityTagDTOList[]`: deduplicated entities involved in the query.

## Table Shape

- `dataTableDTOList[].code`: full security code, often with market suffix.
- `dataTableDTOList[].entityName`: entity name and code.
- `dataTableDTOList[].title`: table title for this result.
- `dataTableDTOList[].table`: normalized column data. Keys are indicator codes; `headName` is the time or dimension axis.
- `dataTableDTOList[].rawTable`: unnormalized table values.
- `dataTableDTOList[].nameMap`: maps internal field names to business-readable labels.
- `dataTableDTOList[].indicatorOrder`: preferred metric column order.
- `dataTableDTOList[].field`: current metric metadata, including source code/name and date range.
- `dataTableDTOList[].entityTagDTO`: security/entity attributes such as code, market, type, full name, and internal entity id.

## Parsing Rules

- Prefer generated Excel for user-facing tables.
- Use `nameMap` to turn internal keys into readable column names.
- Preserve units and date granularity from `field` when available.
- If `table` and `rawTable` differ, treat `table` as presentation-ready and `rawTable` as audit detail.
