---
name: android-sms-gateway-local
description: Send and receive SMS/MMS via SMS Gateway for Android (android-sms-gateway / sms-gate) using Local Server mode with Basic Auth, including webhooks, inbox export, and message status checks.
---

# Android SMS Gateway (Local)

Use this skill when working with the Android SMS Gateway app in Local Server mode. Keep the flow minimal and confirm missing inputs before calling the API.

## Gather Inputs

Ask for any missing details:
- Device local IP and port (default port is 8080)
- Local Server username and password
- Action: send SMS, receive SMS (webhook), export inbox, or check status
- For sending: phone numbers, message text, optional `deviceId` and `simNumber`
- For receiving: webhook URL and whether HTTPS is available
- For exporting inbox: `deviceId` and a time window (`since`, `until`)

## Connect and Validate

- Base URL for Local Server is `http://<device_ip>:<port>`.
- Local Server supports Basic Auth only; include credentials in every request.
- Validate connectivity first with `GET /health`, then list devices with `GET /devices`.

## Send SMS

- Use `POST /messages` with `phoneNumbers` and `textMessage.text` (preferred) or `dataMessage` if requested.
- Include `deviceId` or `simNumber` when the user wants to target a specific device or SIM.
- Use `withDeliveryReport: true` if the user needs delivery confirmation.

## Receive SMS

- Register a webhook with `POST /webhooks` and `event: "sms:received"` (optionally scope to a `deviceId`).
- The webhook receiver must support HTTPS for private IPs unless it is `http://127.0.0.1`.
- To fetch historical inbox messages, call `POST /messages/inbox/export` after the webhook is registered.

## Status Tracking

- Use `GET /messages/{id}` to read the message `state` and other fields.
- Consider also registering `sms:sent`, `sms:delivered`, and `sms:failed` webhooks for near-real-time status updates.

## References

- Use `{baseDir}/references/api.md` for endpoint summaries, payload shapes, and event names.

## Scripts

- Use `{baseDir}/scripts/health.sh` and `{baseDir}/scripts/list_devices.sh` to verify connectivity.
- Use `{baseDir}/scripts/send_sms.sh` to send a text message.
- Use `{baseDir}/scripts/get_message.sh` and `{baseDir}/scripts/list_messages.sh` to check status.
- Use `{baseDir}/scripts/register_webhook.sh`, `{baseDir}/scripts/list_webhooks.sh`, and `{baseDir}/scripts/delete_webhook.sh` to manage webhooks.
- Use `{baseDir}/scripts/export_inbox.sh` to replay inbox messages.
