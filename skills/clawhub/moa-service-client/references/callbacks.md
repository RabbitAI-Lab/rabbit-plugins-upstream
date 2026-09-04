# MOA Callback Guide

MOA can send `POST` callbacks to the request `callbackUrl` or its deployment default. Callback configuration is optional; polling `GET /v1/designs/{designId}` remains required because callbacks can fail, arrive late, repeat, or arrive out of order.

Supported events are:

- `design.ready` for an initial version ready for review.
- `design.revised` for a revised version ready for review.
- `design.failed` for a terminal failure.

Each event includes a stable `eventId`, `designId`, `version`, `multicaTask`, event timestamp, repository snapshot, and (for ready/revised) `packageHash` plus artifact metadata. Failed events include `lastError`.

Receiver requirements:

1. Persist and uniquely deduplicate by `eventId`; return any 2xx for a duplicate without applying state twice.
2. Save the raw event, receive time, processing result, `designId`, version, repository snapshot, package hash, and failure details where applicable.
3. On ready/revised, retrieve artifacts through MOA HTTP and verify every advertised SHA-256 before presenting them as reviewed content.
4. On failed, surface `lastError` and retain a link or route to re-query MOA status.
5. Return non-2xx only for a genuinely unprocessed event. MOA may retry delivery; retry does not alter the MOA run state.

Do not assume a callback signature header exists. The current contract relies on HTTPS plus a configured callback host allow-list. If the receiving system requires signed callbacks or mTLS, treat it as a protocol extension that needs coordination with the MOA service owner.
