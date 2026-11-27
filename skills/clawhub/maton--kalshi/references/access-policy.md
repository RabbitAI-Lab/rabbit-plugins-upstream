# Kalshi access policy

An access policy limits which endpoints Kalshi connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/kalshi#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Kalshi: its 86 read-only endpoints. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create kalshi --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "trade-api/v2/account/api_usage_level/volume_progress"},
    {"method": "GET", "path": "trade-api/v2/account/endpoint_costs"},
    {"method": "GET", "path": "trade-api/v2/account/limits"},
    {"method": "GET", "path": "trade-api/v2/api_keys"},
    {"method": "GET", "path": "trade-api/v2/communications/block-trade-proposals"},
    {"method": "GET", "path": "trade-api/v2/communications/id"},
    {"method": "GET", "path": "trade-api/v2/communications/quotes"},
    {"method": "GET", "path": "trade-api/v2/communications/quotes/{id}"},
    {"method": "GET", "path": "trade-api/v2/communications/rfqs"},
    {"method": "GET", "path": "trade-api/v2/communications/rfqs/{id}"},
    {"method": "GET", "path": "trade-api/v2/communications/rfqs/{id}/quotes/{id}"},
    {"method": "GET", "path": "trade-api/v2/events"},
    {"method": "GET", "path": "trade-api/v2/events/fee_changes"},
    {"method": "GET", "path": "trade-api/v2/events/multivariate"},
    {"method": "GET", "path": "trade-api/v2/events/{id}"},
    {"method": "GET", "path": "trade-api/v2/events/{id}/metadata"},
    {"method": "GET", "path": "trade-api/v2/series/{id}/events/{id}/candlesticks"},
    {"method": "GET", "path": "trade-api/v2/series/{id}/events/{id}/forecast_percentile_history"},
    {"method": "GET", "path": "trade-api/v2/exchange/schedule"},
    {"method": "GET", "path": "trade-api/v2/exchange/status"},
    {"method": "GET", "path": "trade-api/v2/exchange/user_data_timestamp"},
    {"method": "GET", "path": "trade-api/v2/series/fee_changes"},
    {"method": "GET", "path": "trade-api/v2/fcm/fills"},
    {"method": "GET", "path": "trade-api/v2/fcm/orders"},
    {"method": "GET", "path": "trade-api/v2/fcm/positions"},
    {"method": "GET", "path": "trade-api/v2/fcm/subtraders"},
    {"method": "GET", "path": "trade-api/v2/fcm/subtraders/blocked_categories"},
    {"method": "GET", "path": "trade-api/v2/fcm/subtraders/event_contract_daily_cap"},
    {"method": "GET", "path": "trade-api/v2/historical/cutoff"},
    {"method": "GET", "path": "trade-api/v2/historical/fills"},
    {"method": "GET", "path": "trade-api/v2/historical/markets"},
    {"method": "GET", "path": "trade-api/v2/historical/markets/{id}"},
    {"method": "GET", "path": "trade-api/v2/historical/markets/{id}/candlesticks"},
    {"method": "GET", "path": "trade-api/v2/historical/orders"},
    {"method": "GET", "path": "trade-api/v2/historical/positions"},
    {"method": "GET", "path": "trade-api/v2/historical/trades"},
    {"method": "GET", "path": "trade-api/v2/incentive_programs"},
    {"method": "GET", "path": "trade-api/v2/incentive_schedules"},
    {"method": "GET", "path": "trade-api/v2/live_data/batch"},
    {"method": "GET", "path": "trade-api/v2/live_data/events/{id}"},
    {"method": "GET", "path": "trade-api/v2/live_data/milestone/{id}"},
    {"method": "GET", "path": "trade-api/v2/live_data/milestone/{id}/game_stats"},
    {"method": "GET", "path": "trade-api/v2/live_data/weather/{id}"},
    {"method": "GET", "path": "trade-api/v2/live_data/weather/{id}/calibrations"},
    {"method": "GET", "path": "trade-api/v2/live_data/{id}/milestone/{id}"},
    {"method": "GET", "path": "trade-api/v2/markets"},
    {"method": "GET", "path": "trade-api/v2/markets/candlesticks"},
    {"method": "GET", "path": "trade-api/v2/markets/orderbooks"},
    {"method": "GET", "path": "trade-api/v2/markets/trades"},
    {"method": "GET", "path": "trade-api/v2/markets/{id}"},
    {"method": "GET", "path": "trade-api/v2/markets/{id}/orderbook"},
    {"method": "GET", "path": "trade-api/v2/series"},
    {"method": "GET", "path": "trade-api/v2/series/{id}"},
    {"method": "GET", "path": "trade-api/v2/series/{id}/markets/{id}/candlesticks"},
    {"method": "GET", "path": "trade-api/v2/concert_cancellation_markets/availability"},
    {"method": "GET", "path": "trade-api/v2/concert_cancellation_markets/concerts"},
    {"method": "GET", "path": "trade-api/v2/concert_cancellation_markets/concerts/search"},
    {"method": "GET", "path": "trade-api/v2/weather_point_markets/availability"},
    {"method": "GET", "path": "trade-api/v2/milestones"},
    {"method": "GET", "path": "trade-api/v2/milestones/{id}"},
    {"method": "GET", "path": "trade-api/v2/multivariate_event_collections"},
    {"method": "GET", "path": "trade-api/v2/multivariate_event_collections/{id}"},
    {"method": "GET", "path": "trade-api/v2/portfolio/order_groups"},
    {"method": "GET", "path": "trade-api/v2/portfolio/order_groups/{id}"},
    {"method": "GET", "path": "trade-api/v2/portfolio/orders"},
    {"method": "GET", "path": "trade-api/v2/portfolio/orders/queue_positions"},
    {"method": "GET", "path": "trade-api/v2/portfolio/orders/{id}"},
    {"method": "GET", "path": "trade-api/v2/portfolio/orders/{id}/queue_position"},
    {"method": "GET", "path": "trade-api/v2/portfolio/balance"},
    {"method": "GET", "path": "trade-api/v2/portfolio/credit_history"},
    {"method": "GET", "path": "trade-api/v2/portfolio/deposits"},
    {"method": "GET", "path": "trade-api/v2/portfolio/fills"},
    {"method": "GET", "path": "trade-api/v2/portfolio/intra_exchange_instance_transfers"},
    {"method": "GET", "path": "trade-api/v2/portfolio/intra_exchange_instance_transfers/{id}"},
    {"method": "GET", "path": "trade-api/v2/portfolio/positions"},
    {"method": "GET", "path": "trade-api/v2/portfolio/settlements"},
    {"method": "GET", "path": "trade-api/v2/portfolio/subaccounts/balances"},
    {"method": "GET", "path": "trade-api/v2/portfolio/subaccounts/netting"},
    {"method": "GET", "path": "trade-api/v2/portfolio/subaccounts/transfers"},
    {"method": "GET", "path": "trade-api/v2/portfolio/summary/total_resting_order_value"},
    {"method": "GET", "path": "trade-api/v2/portfolio/target_balance_allocation"},
    {"method": "GET", "path": "trade-api/v2/portfolio/withdrawals"},
    {"method": "GET", "path": "trade-api/v2/search/filters_by_sport"},
    {"method": "GET", "path": "trade-api/v2/search/tags_by_categories"},
    {"method": "GET", "path": "trade-api/v2/structured_targets"},
    {"method": "GET", "path": "trade-api/v2/structured_targets/{id}"}
  ],
  "deny": []
}
```

## Endpoints

The Kalshi endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| POST | trade-api/v2/account/api_usage_level/upgrade | write | account | Upgrade Account API Usage Level. |
| GET | trade-api/v2/account/api_usage_level/volume_progress | read | account | Get Account API Usage Level Volume Progress. |
| GET | trade-api/v2/account/endpoint_costs | read | account | List Non-Default Endpoint Costs. |
| GET | trade-api/v2/account/limits | read | account | Get Account API Limits. |
| GET | trade-api/v2/api_keys | read | api keys | Get API Keys. |
| POST | trade-api/v2/api_keys | write | api keys | Create API Key. |
| POST | trade-api/v2/api_keys/generate | write | api keys | Generate API Key. |
| DELETE | trade-api/v2/api_keys/{id} | write | api keys | Delete API Key. |
| GET | trade-api/v2/communications/block-trade-proposals | read | communications | Get Block Trade Proposals. |
| POST | trade-api/v2/communications/block-trade-proposals | write | communications | Propose Block Trade. |
| DELETE | trade-api/v2/communications/block-trade-proposals/{id} | write | communications | Cancel Block Trade Proposal. |
| POST | trade-api/v2/communications/block-trade-proposals/{id}/accept | write | communications | Accept Block Trade Proposal. |
| POST | trade-api/v2/communications/block-trade-proposals/{id}/reject | write | communications | Reject Block Trade Proposal. |
| GET | trade-api/v2/communications/id | read | communications | Get Communications ID. |
| GET | trade-api/v2/communications/quotes | read | communications | Get Quotes. |
| POST | trade-api/v2/communications/quotes | write | communications | Create Quote. |
| GET | trade-api/v2/communications/quotes/{id} | read | communications | Get Quote. |
| DELETE | trade-api/v2/communications/quotes/{id} | write | communications | Delete Quote. |
| PUT | trade-api/v2/communications/quotes/{id}/accept | write | communications | Accept Quote. |
| PUT | trade-api/v2/communications/quotes/{id}/confirm | write | communications | Confirm Quote. |
| GET | trade-api/v2/communications/rfqs | read | communications | Get RFQs. |
| POST | trade-api/v2/communications/rfqs | write | communications | Create RFQ. |
| GET | trade-api/v2/communications/rfqs/{id} | read | communications | Get RFQ. |
| DELETE | trade-api/v2/communications/rfqs/{id} | write | communications | Delete RFQ. |
| GET | trade-api/v2/communications/rfqs/{id}/quotes/{id} | read | communications | Get RFQ Quote. |
| DELETE | trade-api/v2/communications/rfqs/{id}/quotes/{id} | write | communications | Delete RFQ Quote. |
| PUT | trade-api/v2/communications/rfqs/{id}/quotes/{id}/accept | write | communications | Accept RFQ Quote. |
| PUT | trade-api/v2/communications/rfqs/{id}/quotes/{id}/confirm | write | communications | Confirm RFQ Quote. |
| GET | trade-api/v2/events | read | events | Get Events. |
| GET | trade-api/v2/events/fee_changes | read | events | Get Event Fee Changes. |
| GET | trade-api/v2/events/multivariate | read | events | Get Multivariate Events. |
| GET | trade-api/v2/events/{id} | read | events | Get Event. |
| GET | trade-api/v2/events/{id}/metadata | read | events | Get Event Metadata. |
| GET | trade-api/v2/series/{id}/events/{id}/candlesticks | read | events | Get Event Candlesticks. |
| GET | trade-api/v2/series/{id}/events/{id}/forecast_percentile_history | read | events | Get Event Forecast Percentile History. |
| GET | trade-api/v2/exchange/schedule | read | exchange | Get Exchange Schedule. |
| GET | trade-api/v2/exchange/status | read | exchange | Get Exchange Status. |
| GET | trade-api/v2/exchange/user_data_timestamp | read | exchange | Get User Data Timestamp. |
| GET | trade-api/v2/series/fee_changes | read | exchange | Get Series Fee Changes. |
| GET | trade-api/v2/fcm/fills | read | fcm | Get FCM Fills. |
| GET | trade-api/v2/fcm/orders | read | fcm | Get FCM Orders. |
| GET | trade-api/v2/fcm/positions | read | fcm | Get FCM Positions. |
| POST | trade-api/v2/fcm/positions/transfers | write | fcm | Create FCM Position Transfer. |
| GET | trade-api/v2/fcm/subtraders | read | fcm | List FCM Subtraders. |
| POST | trade-api/v2/fcm/subtraders | write | fcm | Create FCM Subtrader. |
| GET | trade-api/v2/fcm/subtraders/blocked_categories | read | fcm | Get FCM Subtrader Blocked Categories. |
| PUT | trade-api/v2/fcm/subtraders/blocked_categories | write | fcm | Update FCM Subtrader Blocked Categories. |
| GET | trade-api/v2/fcm/subtraders/event_contract_daily_cap | read | fcm | Get FCM Subtrader Event Contract Daily Cap. |
| PUT | trade-api/v2/fcm/subtraders/event_contract_daily_cap | write | fcm | Update FCM Subtrader Event Contract Daily Cap. |
| DELETE | trade-api/v2/fcm/subtraders/event_contract_daily_cap | write | fcm | Delete FCM Subtrader Event Contract Daily Cap. |
| GET | trade-api/v2/historical/cutoff | read | historical | Get Historical Cutoff Timestamps. |
| GET | trade-api/v2/historical/fills | read | historical | Get Historical Fills. |
| GET | trade-api/v2/historical/markets | read | historical | Get Historical Markets. |
| GET | trade-api/v2/historical/markets/{id} | read | historical | Get Historical Market. |
| GET | trade-api/v2/historical/markets/{id}/candlesticks | read | historical | Get Historical Market Candlesticks. |
| GET | trade-api/v2/historical/orders | read | historical | Get Historical Orders. |
| GET | trade-api/v2/historical/positions | read | historical | Get Historical Positions. |
| GET | trade-api/v2/historical/trades | read | historical | Get Historical Trades. |
| GET | trade-api/v2/incentive_programs | read | incentive programs | Get Incentives. |
| GET | trade-api/v2/incentive_schedules | read | incentive programs | Get Incentive Schedules. |
| GET | trade-api/v2/live_data/batch | read | live data | Get Multiple Live Data. |
| GET | trade-api/v2/live_data/events/{id} | read | live data | Get Event Live Data. |
| GET | trade-api/v2/live_data/milestone/{id} | read | live data | Get Live Data. |
| GET | trade-api/v2/live_data/milestone/{id}/game_stats | read | live data | Get Game Stats. |
| GET | trade-api/v2/live_data/weather/{id} | read | live data | Get Weather Index. |
| GET | trade-api/v2/live_data/weather/{id}/calibrations | read | live data | Get Weather Index Calibrations. |
| GET | trade-api/v2/live_data/{id}/milestone/{id} | read | live data | Get Live Data (with type). |
| GET | trade-api/v2/markets | read | market | Get Markets. |
| GET | trade-api/v2/markets/candlesticks | read | market | Batch Get Market Candlesticks. |
| GET | trade-api/v2/markets/orderbooks | read | market | Get Multiple Market Orderbooks. |
| GET | trade-api/v2/markets/trades | read | market | Get Trades. |
| GET | trade-api/v2/markets/{id} | read | market | Get Market. |
| GET | trade-api/v2/markets/{id}/orderbook | read | market | Get Market Orderbook. |
| GET | trade-api/v2/series | read | market | Get Series List. |
| GET | trade-api/v2/series/{id} | read | market | Get Series. |
| GET | trade-api/v2/series/{id}/markets/{id}/candlesticks | read | market | Get Market Candlesticks. |
| POST | trade-api/v2/concert_cancellation_markets | write | markets | Create Concert Cancellation Market. |
| GET | trade-api/v2/concert_cancellation_markets/availability | read | markets | Get Concert Cancellation Market Availability. |
| GET | trade-api/v2/concert_cancellation_markets/concerts | read | markets | Get Concerts. |
| GET | trade-api/v2/concert_cancellation_markets/concerts/search | read | markets | Search Concerts. |
| POST | trade-api/v2/weather_point_markets | write | markets | Create Weather Point Market. |
| GET | trade-api/v2/weather_point_markets/availability | read | markets | Get Weather Point Market Availability. |
| GET | trade-api/v2/milestones | read | milestone | Get Milestones. |
| GET | trade-api/v2/milestones/{id} | read | milestone | Get Milestone. |
| GET | trade-api/v2/multivariate_event_collections | read | multivariate | Get Multivariate Event Collections. |
| GET | trade-api/v2/multivariate_event_collections/{id} | read | multivariate | Get Multivariate Event Collection. |
| POST | trade-api/v2/multivariate_event_collections/{id} | write | multivariate | Create Market In Multivariate Event Collection. |
| GET | trade-api/v2/portfolio/order_groups | read | order groups | Get Order Groups. |
| POST | trade-api/v2/portfolio/order_groups/create | write | order groups | Create Order Group. |
| GET | trade-api/v2/portfolio/order_groups/{id} | read | order groups | Get Order Group. |
| DELETE | trade-api/v2/portfolio/order_groups/{id} | write | order groups | Delete Order Group. |
| PUT | trade-api/v2/portfolio/order_groups/{id}/limit | write | order groups | Update Order Group Limit. |
| PUT | trade-api/v2/portfolio/order_groups/{id}/reset | write | order groups | Reset Order Group. |
| PUT | trade-api/v2/portfolio/order_groups/{id}/trigger | write | order groups | Trigger Order Group. |
| POST | trade-api/v2/portfolio/events/orders | write | orders | Create Order (V2). |
| DELETE | trade-api/v2/portfolio/events/orders | write | orders | Cancel All Orders. |
| POST | trade-api/v2/portfolio/events/orders/batched | write | orders | Batch Create Orders (V2). |
| DELETE | trade-api/v2/portfolio/events/orders/batched | write | orders | Batch Cancel Orders (V2). |
| DELETE | trade-api/v2/portfolio/events/orders/{id} | write | orders | Cancel Order (V2). |
| POST | trade-api/v2/portfolio/events/orders/{id}/amend | write | orders | Amend Order (V2). |
| POST | trade-api/v2/portfolio/events/orders/{id}/decrease | write | orders | Decrease Order (V2). |
| GET | trade-api/v2/portfolio/orders | read | orders | Get Orders. |
| GET | trade-api/v2/portfolio/orders/queue_positions | read | orders | Get Queue Positions for Orders. |
| GET | trade-api/v2/portfolio/orders/{id} | read | orders | Get Order. |
| GET | trade-api/v2/portfolio/orders/{id}/queue_position | read | orders | Get Order Queue Position. |
| GET | trade-api/v2/portfolio/balance | read | portfolio | Get Balance. |
| GET | trade-api/v2/portfolio/credit_history | read | portfolio | Get Credit History. |
| GET | trade-api/v2/portfolio/deposits | read | portfolio | Get Deposits. |
| GET | trade-api/v2/portfolio/fills | read | portfolio | Get Fills. |
| POST | trade-api/v2/portfolio/intra_exchange_instance_transfer | write | portfolio | Intra Account Transfer. |
| GET | trade-api/v2/portfolio/intra_exchange_instance_transfers | read | portfolio | Get Intra Account Transfers. |
| GET | trade-api/v2/portfolio/intra_exchange_instance_transfers/{id} | read | portfolio | Get Intra Account Transfer. |
| GET | trade-api/v2/portfolio/positions | read | portfolio | Get Positions. |
| GET | trade-api/v2/portfolio/settlements | read | portfolio | Get Settlements. |
| POST | trade-api/v2/portfolio/subaccounts | write | portfolio | Create Subaccount. |
| GET | trade-api/v2/portfolio/subaccounts/balances | read | portfolio | Get All Subaccount Balances. |
| GET | trade-api/v2/portfolio/subaccounts/netting | read | portfolio | Get Subaccount Netting. |
| PUT | trade-api/v2/portfolio/subaccounts/netting | write | portfolio | Update Subaccount Netting. |
| POST | trade-api/v2/portfolio/subaccounts/transfer | write | portfolio | Transfer Between Subaccounts. |
| GET | trade-api/v2/portfolio/subaccounts/transfers | read | portfolio | Get Subaccount Transfers. |
| GET | trade-api/v2/portfolio/summary/total_resting_order_value | read | portfolio | Get Total Resting Order Value. |
| GET | trade-api/v2/portfolio/target_balance_allocation | read | portfolio | Get Target Balance Allocation. |
| POST | trade-api/v2/portfolio/target_balance_allocation | write | portfolio | Set Target Balance Allocation. |
| GET | trade-api/v2/portfolio/withdrawals | read | portfolio | Get Withdrawals. |
| GET | trade-api/v2/search/filters_by_sport | read | search | Get Filters for Sports. |
| GET | trade-api/v2/search/tags_by_categories | read | search | Get Tags for Series Categories. |
| GET | trade-api/v2/structured_targets | read | structured targets | Get Structured Targets. |
| GET | trade-api/v2/structured_targets/{id} | read | structured targets | Get Structured Target. |
