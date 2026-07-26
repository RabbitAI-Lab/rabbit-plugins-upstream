# API Reference (Local Mode)

Use this as a compact reminder. For full details, consult the official docs.

## Base URL and Auth

- Local Server base: `http://<device_ip>:<port>` (default `8080`).
- Local Server supports Basic Auth only.

Note: The Local Server quickstart shows `POST /message`, while the OpenAPI spec lists `/messages`. Prefer `/messages`; if you see 404 on Local Server, try `/message`.

## Health and Devices

- `GET /health`
- `GET /devices`

## Send SMS (Text)

- `POST /messages`
- Required: `phoneNumbers` (array)
- Preferred payload: `textMessage: { "text": "..." }`
- Optional fields: `deviceId`, `simNumber`, `priority`, `ttl`, `validUntil`, `withDeliveryReport`
- Query params: `skipPhoneValidation` (bool), `deviceActiveWithin` (hours)

Example (text message):
```json
{
  "phoneNumbers": ["+15551234567"],
  "textMessage": { "text": "Hello from Local Server" },
  "withDeliveryReport": true
}
```

## Message Status

- `GET /messages/{id}`
- `GET /messages` with query params: `from`, `to`, `state`, `deviceId`, `limit`, `offset`
- States: `Pending`, `Processed`, `Sent`, `Delivered`, `Failed`
- `Delivered` is only available if `withDeliveryReport` was enabled at send time.

## Receive SMS (Webhooks)

- `POST /webhooks` with body `{ "url": "https://...", "event": "sms:received", "deviceId": "..." }`
- Events: `sms:received`, `sms:data-received`, `mms:received`, `sms:sent`, `sms:delivered`, `sms:failed`, `system:ping`
- HTTPS is required for private IPs; only `http://127.0.0.1` can be used without TLS.

## Inbox Export (Historical Receive)

- `POST /messages/inbox/export` with `deviceId`, `since`, `until`
- Requires a registered `sms:received` webhook; the device will replay inbox messages to the webhook URL.

## Webhooks Management

- `GET /webhooks`
- `DELETE /webhooks/{id}`

## Test Scripts (Bash + curl)

All scripts live in `{baseDir}/scripts/` and use `curl.exe`.

Required env vars for all scripts:
- `SMS_GATE_BASE_URL` (example: `http://192.168.1.10:8080`)
- `SMS_GATE_USER`
- `SMS_GATE_PASS`

Linux tip: `chmod +x {baseDir}/scripts/*.sh` before running.

Per-script env vars:
- `send_sms`: `PHONE_NUMBERS` (comma-separated), `MESSAGE_TEXT`, optional `DEVICE_ID`, `SIM_NUMBER`, `WITH_DELIVERY_REPORT`
- `get_message`: `MESSAGE_ID`
- `list_messages`: optional `MSG_FROM`, `MSG_TO`, `MSG_STATE`, `DEVICE_ID`, `MSG_LIMIT`, `MSG_OFFSET`
- `register_webhook`: `WEBHOOK_URL`, optional `WEBHOOK_EVENT`, `DEVICE_ID`
- `delete_webhook`: `WEBHOOK_ID`
- `export_inbox`: `DEVICE_ID`, `INBOX_SINCE`, `INBOX_UNTIL`
