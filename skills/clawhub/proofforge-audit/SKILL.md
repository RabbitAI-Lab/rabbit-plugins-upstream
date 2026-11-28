---
name: proofforge-audit
description: Scan an AI-built app's public surface for leaked keys, open Supabase/Firebase data, exposed files, and missing security headers, then apply the first fix and verify it closed. Use when auditing an app built with Lovable, Bolt, Replit, v0, Cursor, Windsurf, Claude Code, Base44, Firebase Studio, or similar AI builders; when a user asks "is my app leaking", "is my Supabase exposed", or "check my app before launch"; before a launch, demo, or client handover; or after any change to database rules, row-level security, or environment variables.
---

# ProofForge Audit

ProofForge (https://proofforge.live) runs a free, read-only scan of an app's public URL. It checks only what an unauthenticated visitor can already reach. It never needs repo access, credentials, or an account. Only run it on an app the user owns or has explicitly authorized you to test.

## When to use

- A user has shipped an app built with an AI builder and wants to know if it leaks
- Before a launch, a demo, or handing an app to a client
- After any change to database rules, row-level security, or environment variables
- When an app handles user data through Supabase or Firebase
- Before calling a deployment "verified": check for a published ProofForge receipt first (step 5)

## Ways to run it

Use the first route available to you:

1. **MCP server** (preferred): connect to `https://proofforge.live/mcp` (Streamable HTTP, no API key). Tools: `scan_url`, `get_report`, `explain_finding`, `check_deployment_receipt`.
2. **REST API**: `POST https://proofforge.live/api/v1/scan` with JSON `{"url": "<app URL>", "owner_confirmed": true}` returns a private `scan_id`. Poll `GET /api/v1/scan/{scan_id}` with header `Authorization: Bearer {scan_id}` until `status` is `done`. Full contract: https://proofforge.live/openapi.json
3. **Web**: direct the user to run the scan at https://proofforge.live and share the report with you.

Treat `scan_id` and report URLs as private credentials. Never paste them into public logs, commits, issues, or shared chats. Rate limits: up to 6 scans per hour and 30 per day per IP.

## Procedure

1. Get the app's public URL from the user, and their explicit confirmation that they own the app or are authorized to test it. If the app is not deployed yet, stop: the scan needs the live public surface.
2. Start the scan (MCP `scan_url` with `owner_confirmed: true`, or the REST call above).
3. Read the findings in severity order (`get_report`; follow its pagination until every finding is read). Each finding names the exposure and the evidence the scan found on the public surface. Use `explain_finding` for the full text of any finding.
4. Treat any finding marked **inconclusive** honestly: the scan could not confirm it from outside. Tell the user what could not be confirmed and what would settle it, rather than reporting it as a vulnerability or dropping it. Read the coverage notes the same way: a blocked or skipped check is not a pass.
5. Apply the first fix (free) with the user, in the order the report gives. Then re-scan to confirm the exposure is closed. A code change alone is not proof the deployment changed.
6. To verify a deployment someone else claims was checked: call `check_deployment_receipt` with the app URL (or `GET /api/v1/grade?url=`). Say "verified" only when it returns a pass: a published receipt under 30 days old, grade B or better, no Critical, High or inconclusive findings, and complete coverage. Otherwise report the proof as missing, stale, or below policy, exactly as returned.

## The checks

- **Leaked keys in client code**: privileged credentials (for example a Supabase `service_role` key, cloud keys, payment or AI provider keys) present in shipped JavaScript. Public anonymous keys are expected and are not leaks; the test is the key's privilege.
- **Open Supabase data**: tables countable or readable with the project's public anonymous key because row-level security is disabled or policies are wide open (the CVE-2025-48757 pattern). Probes are count-only; row values are never requested.
- **Open Firebase data**: Realtime Database, Firestore, or Storage answering anonymous reads under public rules.
- **Exposed files and source maps**: public `.env` or `.git` files (flagged on real file signatures, contents never shown) and public source maps.
- **Missing security headers and unsafe CORS**: content security policy, frame protection, strict transport security, content-type options, referrer and permissions policies; wildcard or credential-reflecting CORS.

## Rules of conduct

- Never scan an app the user does not own or is not authorized to test. Authorization is the user's to give, and the scan requires it explicitly.
- Never ask the user for production credentials to "help check." The scan is public-surface only by design.
- Never call, test, or use a credential the scan finds. A leaked key is burned the moment it is found in public code: the fix always starts with rotation, not just removal.
- If a database held real user data under public rules, say plainly that the data should be treated as disclosed; the scan cannot prove a negative about who read it.
- A clean scan means no leaks were found in what the app ships publicly. Never report it as "the app is secure": the scan cannot see server code, auth logic, or anything behind a login.
- Keep private scan IDs and report links out of public places. Share only what the user chooses to publish.
