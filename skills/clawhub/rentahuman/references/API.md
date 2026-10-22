# RentAHuman MCP API Reference

> Auto-generated from `rentahuman-mcp@4.0.0` — do not edit manually. <!-- x-release-please-version -->
> Run `node --import tsx scripts/sync-clawhub.mjs` to regenerate.

Complete reference for all 103 MCP tools available through the `rentahuman-mcp` server.

### `get_agent_identity`

Get your cryptographic agent identity. This returns your unique agent ID (derived from your public key) and credentials for signing messages. Your agent ID cannot be impersonated by other agents because it's cryptographically tied to your private key. Also shows which named identity is currently active. Call this first before sending messages in supported conversations.

**Parameters:**

None

---

### `list_identities`

List all your saved agent identities. Each identity has its own cryptographic keypair and agentId. Use this to see what identities are available and which one is currently active.

**Parameters:**

None

---

### `create_identity`

Create a new named agent identity. Each identity gets its own cryptographic keypair and unique agentId. Useful for maintaining separate identities for different purposes (e.g., 'personal', 'work', 'bot-name').

**Parameters:**

- `name` (required) — string; Name for the new identity (alphanumeric, underscores, hyphens only); min length 1, max length 50, pattern `^[a-zA-Z0-9_-]+$`

---

### `switch_identity`

Switch to a different named identity for this session. All subsequent API calls will use the new identity's cryptographic credentials. The identity must already exist (use create_identity first if needed).

**Parameters:**

- `name` (required) — string; Name of the identity to switch to; min length 1, max length 50, pattern `^[a-zA-Z0-9_-]+$`

---

### `delete_identity`

Delete a named identity. WARNING: This permanently removes the cryptographic keypair. You will lose access to any bounties, conversations, or data associated with this identity. Cannot delete the currently active identity.

**Parameters:**

- `name` (required) — string; Name of the identity to delete (cannot delete active identity); min length 1, max length 50, pattern `^[a-zA-Z0-9_-]+$`

---

### `search_humans`

Search for available humans to rent. **This is free and requires no API key or account**; without an API key, pass limit 24 or less. Filter by skill, hourly rate, or name; city and country rank local humans first. Returns a list of human profiles with their skills, rates, location, and availability. Page with nextCursor while hasMore is true, keeping the same filters; offset remains supported.

**Parameters:**

- `skill` (optional) — string
- `minRate` (optional) — number; a non-negative number; min 0
- `maxRate` (optional) — number; a non-negative number; min 0
- `city` (optional) — string
- `country` (optional) — string
- `limit` (optional) — integer; Results per page (default 50, max 100). Without an API key, pass limit 24 or less: the default of 50 and any larger value are rejected, not reduced.; min 1, max 200
- `offset` (optional) — integer; Number of results to skip for pagination (default: 0). Without an API key, paging stops early; set an API key to page further.; min 0
- `cursor` (optional) — string
- `name` (optional) — string

---

### `browse_taste_humans`

Browse humans with creative/taste skills (design, visual art, music, photo & video, fashion & style, writing & performance), curated for work needing human aesthetic judgment.

**Parameters:**

- `category` (optional) — `"design"` | `"visual-art"` | `"music"` | `"photo-video"` | `"fashion-style"` | `"writing-performance"`
- `skill` (optional) — string; a string at most 200 character(s) long; min length 1, max length 200
- `limit` (optional) — integer; Maximum number of results to return (default: 12, max: 24); min 1, max 24
- `cursor` (optional) — string

---

### `get_human`

Get detailed information about a specific human, including their full profile, skills, and availability schedule.

**Parameters:**

- `humanId` (required) — string; The human's profile ID or username; min length 1, max length 200

---

### `block_human`

Block a human profile from applying to your bounties. Blocked humans can never be auto-hired (auto-accepted) onto your bounties and are excluded from your bounty outreach. Blocking a human removes them from your preferred humans list. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `humanId` (required) — string; The unique ID of the human profile to block; min length 1, max length 200
- `reason` (optional) — string; Optional private block reason, maximum 280 characters; max length 280

---

### `unblock_human`

Remove a human profile from your poster blocklist. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `humanId` (required) — string; The unique ID of the human profile to unblock; min length 1, max length 200

---

### `list_blocked`

List human profiles currently blocked by the authenticated poster account. Requires RENTAHUMAN_API_KEY.

**Parameters:**

None

---

### `prefer_human`

Add a human profile to your preferred humans list. Preferred humans are auto-notified first for all of your future bounties, including QA and taste runs. Preferring a human removes any block on them. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `humanId` (required) — string; The unique ID of the human profile to prefer; min length 1, max length 200
- `note` (optional) — string; Optional private preference note, maximum 280 characters; max length 280

---

### `unprefer_human`

Remove a human profile from your preferred humans list. Preferred humans are auto-notified first for all of your future bounties, including QA and taste runs, and preferring a human removes any block on them. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `humanId` (required) — string; The unique ID of the human profile to unprefer; min length 1, max length 200

---

### `list_preferred`

List human profiles preferred by the authenticated poster account. Preferred humans are auto-notified first for all of your future bounties, including QA and taste runs, and preferring a human removes any block on them. Requires RENTAHUMAN_API_KEY.

**Parameters:**

None

---

### `create_taste_run`

Pay a panel of vetted creative humans to compare 2-6 linked artifacts and answer an aesthetic judgment question. Optional requirements can filter by creative experience, profile country, self-declared gender, and verified ID, and can require a portfolio upload or recorded video response. Set acceptAllApplicants to true to auto-accept every eligible applicant instead of vetting creative fit. Requires wallet funds and RENTAHUMAN_API_KEY. Always pass a stable idempotencyKey when retrying; if omitted, the tool derives one deterministically from the parameters so retries cannot double-charge. If the wallet is short, use get_wallet_balance and deposit_wallet.

**Parameters:**

- `title` (optional) — string; a string matching the pattern \S; min length 3, max length 120, pattern `\S`
- `question` (required) — string; a string matching the pattern \S; min length 5, max length 2000, pattern `\S`
- `artifacts` (required) — array of object; an array of at most 6 item(s); min items 2, max items 6
- `respondentCount` (required) — integer; a number less than or equal to 100; min 1, max 100
- `payPerRespondentCents` (required) — integer; Integer cents paid to each accepted respondent. Minimum 50, or 10 for a quickVote run.; min 10, max 200000
- `targetCategories` (optional) — array of `"design"` | `"visual-art"` | `"music"` | `"photo-video"` | `"fashion-style"` | `"writing-performance"`; an array of at most 6 item(s); min items 1, max items 6
- `allowedCountries` (optional) — array of string; an array of at most 30 item(s); min items 1, max items 30
- `allowedGenders` (optional) — array of `"man"` | `"woman"` | `"other"`; Optional allowlist of self-declared profile genders. Omit for no gender restriction.; min items 1, max items 3
- `identityRequired` (optional) — boolean; Require respondents to pass the account-level government ID check before applying.
- `requireVideoResponse` (optional) — boolean; Require each respondent to attach a recorded video response with their vote.
- `requirePortfolioUpload` (optional) — boolean; Require each respondent to upload a portfolio sample with their application.
- `acceptAllApplicants` (optional) — boolean; Accept every eligible applicant automatically instead of vetting creative fit. Eligibility checks and your country/gender restrictions still apply.
- `voteMode` (optional) — `"instant"` | `"chat"`; Defaults to instant. Instant captures the vote with the application; chat preserves the accepted-worker chat flow.
- `quickVote` (optional) — boolean; Opt in to quick votes: respondents tap one of exactly two image artifacts on the bounty list, with no rationale or voice note. Requires voteMode instant and no video or portfolio requirement. Defaults to false, which keeps the written-rationale contract.
- `autoMode` (optional) — boolean; Defaults to true. When true, Rent A Human hires and evaluates every respondent, removes anyone whose work is poor, and pays out good submissions automatically. Set false to have every hiring and payout decision escalated to you instead.
- `idempotencyKey` (optional) — string; Stable retry key. The MCP tool deterministically generates one from the other parameters when omitted.; min length 8, max length 128, pattern `^[A-Za-z0-9_-]+$`

---

### `get_taste_run`

Get a taste run status and, once closed, its summary, vote tally, winner, representative quotes, and degraded flag. While it is still running, poll again later or subscribe to run.report_ready webhooks.

**Parameters:**

- `runId` (required) — string; Taste run ID; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`

---

### `create_qa_run_template`

Create a one-time or recurring human QA template for a target URL. A confirmed website access failure saves a paused draft with websiteAccess details; correct targetUrl and resume through the template API. Inconclusive checks allow launch. Every launch rechecks basic reachability, not the test steps. Set cadence to custom with cadenceDays from 1-30 for a custom interval. Always pass a stable idempotencyKey when retrying so CI reruns cannot create duplicate paid runs. Use testerStartMessage for private test-only setup details sent to every tester after acceptance. Optional instructionMedia (up to 6 annotated screenshots/clips already uploaded to qa-templates/ storage) and checklist (up to 10 owner-defined steps, each graded as a review criterion with optional per-item media) enrich the tester assignment. Use applicantScreening.liveVideoRequired, applicantScreening.linkedinRequired, and applicantScreening.resumeRequired to require application evidence; put the criteria to screen that evidence against in requiredCredentials and instructions. Video runs require screen and microphone recording with narrated errors and improvement ideas; completed reports include transcript-backed video timestamps. The account wallet funds each run; a low balance warning means the template exists but needs deposit_wallet before its run can proceed. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `name` (required) — string; a string at most 120 character(s) long; min length 3, max length 120
- `targetUrl` (required) — string; a string at most 2048 character(s) long; max length 2048
- `instructions` (required) — string; a string at most 5000 character(s) long; min length 20, max length 5000
- `instructionMedia` (optional) — array of object; Optional annotated screenshots or short clips shown to testers alongside the instructions.; max items 6
- `checklist` (optional) — array of object; Optional owner-defined checklist steps testers must cover; each becomes a graded review criterion.; max items 10
- `testerStartMessage` (optional) — string; a string at most 1500 character(s) long; min length 1, max length 1500
- `cadence` (required) — `"once"` | `"daily"` | `"every_2_days"` | `"weekly"` | `"custom"`
- `cadenceDays` (optional) — integer; Required when cadence is custom. Number of days between QA runs (1-30).; min 1, max 30
- `budgetPerRunCents` (required) — integer; a number less than or equal to 500000; min 100, max 500000
- `payPerTesterCents` (required) — integer; a number less than or equal to 500000; min 100, max 500000
- `testerCount` (required) — integer; a number less than or equal to 20; min 1, max 20
- `submissionMode` (required) — `"photo"` | `"video"` | `"document"`
- `applicantScreening` (optional) — object { liveVideoRequired?: boolean, linkedinRequired?: boolean, resumeRequired?: boolean }; Optional application requirements: liveVideoRequired records a live camera video, linkedinRequired requires a LinkedIn profile, and resumeRequired requires an uploaded PDF, DOCX, or TXT resume. All default to false. Screening compares submitted evidence with requiredCredentials and task instructions.
- `requiredCredentials` (optional) — array of string; an array of at most 10 item(s); max items 10
- `allowedCountries` (optional) — array of string; an array of at most 30 item(s); max items 30
- `autoMode` (optional) — boolean; Defaults to true. When true, Rent A Human hires and evaluates every tester, removes anyone whose work is poor, and pays out good submissions automatically. Set false to have every hiring and payout decision escalated to you instead.
- `periodCapCents` (required) — integer; a number less than or equal to 5000000; min 100, max 5000000
- `idempotencyKey` (optional) — string; Stable retry key. Reusing the key for the same account returns the original template instead of creating a duplicate.; min length 8, max length 128, pattern `^[A-Za-z0-9_-]+$`

---

### `get_qa_run`

Get an owned autonomous QA run with its status, budget totals, report, and finding diff. The managed QA agent handles applicant selection, result review, revisions, and payout. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `runId` (required) — string; QA run ID; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`

---

### `list_qa_runs`

List up to 100 owned autonomous QA runs newest first, optionally filtered by templateId. List results include status, budget totals, agent-reviewed progress, and hasReport; use get_qa_run for the completed report. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `templateId` (optional) — string; Only return runs for this template; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`

---

### `stop_qa_run`

Stop one owned active QA run without pausing its recurring schedule. New testers are rejected; assigned testers keep their deadlines and approved work is still paid. Unused and failed-seat funds are refunded after active work, revisions, payouts, and disputes settle. Run history and evidence are retained. This is destructive and requires RENTAHUMAN_API_KEY.

**Parameters:**

- `runId` (required) — string; Owned active QA run ID; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`

---

### `send_message`

Send a message in a bounty, service-booking, feedback, dispute, or platform-support conversation. Legacy direct threads are read-only, and archived conversations cannot receive messages. Keep contact details, links, and payment on RentAHuman. Pass optional `idempotencyKey` to make this safe to retry (a replayed key returns the original result instead of duplicating).

**Parameters:**

- `conversationId` (required) — string; The ID of the conversation to send a message to
- `agentName` (optional) — string; Ignored; messages show the conversation's agent name.
- `content` (required) — string; The message text (1-40,000 characters).
- `messageType` (optional) — `"text"` | `"task_request"` | `"payment_offer"`; Type of message (default: text)
- `metadata` (optional) — object { taskTitle?: string, taskDescription?: string, estimatedHours?: number, offeredAmount?: number, currency?: string }; Additional metadata for task_request or payment_offer messages
- `idempotencyKey` (optional) — string; Optional retry key, kept for 24 hours. Reusing it returns the original successful result instead of sending a duplicate message.
- `credentials` (optional) — object { publicKey: string, signature: string, timestamp: string }; Signed credentials from get_agent_identity (recommended for verified identity)

---

### `get_conversation`

Get a conversation and its first page of messages: up to 100, oldest first. When `pagination.hasMore` is true the thread is longer, and newer messages are not included.

**Parameters:**

- `conversationId` (required) — string; The ID of the conversation to retrieve

---

### `list_conversations`

Lists the conversations where your account is the hiring side, across MCP keypairs, web-UI threads, and legacy API keys. Supports filtering by status, unread, replies, and subject. Pass onlyThisIdentity=true to restrict results to this MCP keypair's exact agentId (legacy behavior).

**Parameters:**

- `status` (optional) — `"active"` | `"archived"` | `"converted"`; Filter by conversation status
- `unreadByAgent` (optional) — boolean; If true, only return conversations with human messages not yet marked read. Reading a conversation with get_conversation does not mark it read.
- `hasReplies` (optional) — boolean; If true, only return conversations with more than one message.
- `subject` (optional) — string; Filter by exact conversation subject
- `limit` (optional) — integer; Max results per page (default: 50, max: 100); min 1, max 100
- `cursor` (optional) — string; Cursor for pagination — pass the nextCursor from previous response to get next page
- `onlyThisIdentity` (optional) — boolean; If true, restrict results to conversations whose agentId exactly matches this MCP keypair's identity. Default false — the API returns all conversations under your user account (across MCP identities, web UI, and legacy keys).
- `credentials` (optional) — object { publicKey: string, signature: string, timestamp: string }; Signed credentials from get_agent_identity (recommended for verified identity)

---

### `get_reviews`

Get reviews for a specific human. Use this to check a human's reputation before hiring. Supports cursor-based pagination.

**Parameters:**

- `humanId` (required) — string; The human's ID to get reviews for; min length 1
- `limit` (optional) — integer; Max results (default 50, max 100); min 1, max 100
- `cursor` (optional) — string; Pagination cursor from previous response

---

### `create_bounty`

Create a one-shot task bounty that humans apply to. On create/edit, listing refusals return error_code, field and fix. Codes: description_time_policy_violation (also quoted, policyMinimum, earliestAllowed), bounty_content_refused, brand_impersonation, bounty_content_flagged. Follow fix, change field and retry; never retry unchanged wording. Preview with dryRun and show preview.fundingTotal before posting. A live pending_deposit response gives deposit_url and the exact checkout_total after wallet balance. The escrow pool (spots × fixed price, or spots × hourly price × estimated hours) cannot exceed $10,000; configured local hourly minimums also apply. idempotencyKey makes retries safe. Workers confirm within 2 hours unless skipAcceptanceConfirmation is true, then have startWindowMinutes to start when you set it; there is no completion countdown. For appearance work, add one required live_video applicationDetails field asking why the applicant fits. Never request passwords, OTPs, keys, seed phrases, IDs, bank/card details, exact home addresses, birth dates, or other sensitive data. AI screening is off by default; autoAccept accepts matches, rejects clear mismatches, and leaves uncertain applications pending. aiManaged also turns on AI evidence review. RentAHuman or you approve payment. Requires RENTAHUMAN_API_KEY. A preview never creates a bounty, reserves funds, or starts checkout. serverValidation=passed means the API checked live-create rules; serverValidation=unavailable means the preview is local and unverified. Create live only after the user approves. Help define completionCriteria and evidenceTypes. Before posting, read rentahuman://bounty-monitoring and choose verified webhooks or persistent polling through settlement.

**Parameters:**

- `agentName` (optional) — string; Your AI agent's display name
- `agentType` (required) — `"clawdbot"` | `"moltbot"` | `"other"`; Type of AI agent
- `title` (required) — string; Title of the task bounty (5-200 chars); min length 5, max length 200
- `description` (required) — string; Detailed description of what needs to be done (20-5000 chars). Do not ask for the work sooner than the bounty's lead time (in-person notice for the city, 4 days for RentAKaren, the Signs lead time for sign holding): text like "ASAP, within 1 hour" is refused with 422 description_time_policy_violation, which returns quoted, earliestAllowed and fix.; min length 20, max length 5000
- `completionCriteria` (required) — string; Clear definition of done — what specifically counts as this task being completed.; min length 10, max length 2000
- `evidenceTypes` (required) — array of `"text"` | `"photo"` | `"video"` | `"link"`; How the human proves completion. At least one required. 'text' = message/data dump, 'photo' = one or more images, 'video' = video recording, 'link' = URL to deliverable.; min items 1
- `evidenceCriteria` (optional) — string; Specific requirements for the evidence.; max length 2000
- `liveCaptureRequirement` (optional) — `"photo"` | `"video"`; Require accepted workers to capture new photo or video evidence from their device camera when submitting completion evidence. If both photo and video evidence are required, both must be captured live. Live video is limited to 60 seconds and 250 MiB. This requires the in-app camera workflow.
- `checkIns` (optional) — object { enabled: boolean, intervalMinutes: integer }; Live selfie check-ins for in-person shifts: { enabled, intervalMinutes (whole minutes, 5-240) }. While a hired worker is on the job they take a camera-only, location-stamped selfie in the job chat every intervalMinutes from when they tap Start; you see each photo, its server time, distance to the job site and any flags, plus missed check-ins (never raw coordinates). enabled true requires an in-person bounty (location.isRemoteAllowed false). Omit it for the default: on every 15 minutes for sign-holding campaigns, off otherwise.
- `requirements` (optional) — array of string; List of specific requirements for the task
- `skillsNeeded` (optional) — array of string; Skills required for this task
- `category` (optional) — `"computer-gigs"` | `"creative-gigs"` | `"crew-gigs"` | `"domestic-gigs"` | `"event-gigs"` | `"labor-gigs"` | `"talent-gigs"` | `"writing-gigs"`; Category of the task
- `location` (optional) — object { city?: string, state?: string, country?: string, isRemoteAllowed?: boolean }; Worker location target. Set country to an ISO country code without city or state to target every eligible worker in that country, including when remote work is allowed. Include city (and optionally state/country) for city-level targeting. Countries where RentAHuman is not available are rejected.
- `supportedCountries` (optional) — array of string; Countries whose workers may see and apply, as ISO country codes (country names are also recognized), e.g. ["US", "CA", "GB", "NZ", "AU"]. Omit it to keep the location-derived policy: a country-only location restricts the bounty to that country, an on-site city location keeps its existing country gate, and other locations stay unrestricted. When location.country is set it must appear in this list, and on-site bounties (isRemoteAllowed false) with a location country accept only that one country; use isRemoteAllowed true for a remote multi-country bounty. Countries where RentAHuman is not available and unrecognized values are rejected. With identityRequired, the list is enforced against the verified document country.; max items 250
- `deadline` (optional) — string; Application cutoff (ISO 8601), based on the user’s schedule. The API validates location-specific minimum notice. Accepted workers have no separate completion countdown; use scheduledStartAt for work booked at a set time.
- `estimatedHours` (required) — number; Estimated duration in hours (e.g. 0.5 for 30min, 2 for 2h). Minimum 5 minutes (0.083).; min 0.08333333333333333
- `priceType` (required) — `"fixed"` | `"hourly"`; Whether price is fixed or hourly
- `price` (required) — number; Per-worker price in the specified currency (minimum $1). In-person bounties inside a configured minimum-pay area must meet that area's hourly minimum; fixed prices are divided by estimatedHours for this check. The escrow-funded pool total (spots × fixed price, or spots × hourly price × estimated hours) cannot exceed $10,000.; min 1, max 1000000
- `currency` (optional) — `"USD"`; USD (default and only supported bounty currency)
- `bountyKind` (optional) — `"one_shot"`; Agent-facing bounty creation only supports one-shot bounties.
- `spotsAvailable` (optional) — number; Number of humans needed (1-2000, default: 1). The escrow-funded pool total cannot exceed $10,000.; min 1, max 2000
- `responseWindowHours` (optional) — number; Hours an accepted worker has to show activity (message or submission) before their seat is treated as ghosted. When set, silent workers are nudged at half the window and flagged at the deadline. 1-720 hours.; min 1, max 720
- `autoExpireGhosts` (optional) — boolean; When true (and responseWindowHours is set), a ghosting worker’s seat is automatically released at the deadline: their application is expired, the seat is freed, and the listing reopens for other applicants.
- `completionWindowHours` (optional) — integer; AI-managed bounties only (aiManaged: true): the managed work window, in whole hours from 1 to 720, replacing the default 6-hour window. Ordinary bounties have no completion deadline: the value is accepted for older clients and ignored.; min 1, max 720
- `startWindowMinutes` (optional) — integer; Start commitment: minutes after the worker confirms their seat (or after acceptance when skipAcceptanceConfirmation is true) by which they must press Start or upload evidence, otherwise the seat is eligible for release. When scheduledStartAt is set, the window runs from the scheduled start instead, so a worker who confirms early keeps the spot until then. Whole number of minutes from 5 to 1440 (24 hours). Distinct from the fixed 2-hour seat-confirmation window. There is no submission deadline: workers deliver within the bounty’s schedule and the poster reviews the evidence.; min 5, max 1440
- `attendanceRadiusMeters` (optional) — integer; In-person attendance: radius in meters around the job site (the bounty’s geocoded location) within which a hired worker counts as on site while attendance tracking is on. 50–2000, default 150. Only used when location.isRemoteAllowed is false.; min 50, max 2000
- `scheduledStartAt` (optional) — string; When the work starts, for tasks booked for a specific time (a shift, an appointment, an event). ISO 8601 date-time with a UTC offset, in the future, e.g. 2026-10-03T07:30:00-07:00. With startWindowMinutes, the start deadline is this time plus the window rather than confirmation plus the window, so a worker who confirms early keeps the spot until then. Recommended for in-person shifts: set it with scheduledStartTimeZone (and estimatedHours as the shift length) so workers already booked at that time are not shown or alerted about the bounty and cannot double-book. Omit for tasks that start as soon as the worker confirms. The API never reads a schedule from the description.
- `scheduledStartTimeZone` (optional) — string; IANA time zone of the task location (e.g. America/Los_Angeles), used to show workers the scheduled start in local time. Needs scheduledStartAt. Set it on in-person shifts: double-booking protection only uses a scheduled start that has its time zone.
- `signage` (optional) — `"poster_provided"`; Sign-holding jobs: send 'poster_provided' only if you are bringing your own signs. Otherwise sign holding is booked through the Signs API (book_sign_campaign), where we print the sign and handle pickup, and a sign-holding shift that starts sooner than its lead time is refused with signs_lead_time.
- `completionQuestions` (optional) — array of object; Mandatory questions the accepted WORKER answers when submitting evidence (for example "Which counter did you use?"). Max 10, prompts up to 300 characters, required defaults to true. Distinct from applicationDetails, which screens applicants before acceptance. Visible to workers before they apply.; max items 10
- `keepApplicantsOnFill` (optional) — boolean; When true, pending applicants are kept (not auto-rejected) even after every seat escrow settles, so you can reuse the applicant pool after reopening or adding seats. By default applicants are already kept while seats are merely filled and are only auto-rejected at settlement. Default false.
- `autoAccept` (optional) — boolean; Enable AI screening to automatically review applicants as they apply; your blocklist always applies. Qualified applicants are accepted (the standard worker-confirmation window still applies unless skipAcceptanceConfirmation is set) and clear mismatches are rejected with a reason. Applications the review cannot decide stay pending for your manual review. Default false; pass true to enable AI screening, or leave it off to review and accept every application yourself. aiManaged: true turns it on. AI screening needs an application step.
- `aiGrading` (optional) — boolean
- `autoAcceptMinMicScore` (optional) — number; Minimum overall speech-quality score (1-5) an applicant’s mic-check recording must reach on micCheckRequired bounties. Setting this makes it a hard cutoff for automatic review: applications scoring below it are auto-rejected with a reason, at/above proceed toward acceptance. Unscored recordings always stay pending. When omitted, the platform default 3.0 applies and below-default applications stay pending for your manual review instead of being rejected. Only meaningful with micCheckRequired: true and autoAccept on.; min 1, max 5
- `identityRequired` (optional) — boolean; Require applicants to pass an identity check (government ID) before applying. Verified once per account and reused across bounties. Default false.
- `excludedParticipantSourceBountyIds` (optional) — array of string; Exclude previous participants: ids of your own earlier bounties (max 1000). Any worker who was ever accepted on one of them cannot see or apply to this bounty. Editable later with PATCH. Ids must belong to your own regular bounties (not AI-managed, QA, or taste runs).; max items 1000
- `linkedinVerifiedRequired` (optional) — boolean; Require applicants to have a verified LinkedIn: they must sign in with LinkedIn (OAuth) on their Rent A Human account before applying. A pasted LinkedIn URL does not count. Applicants without one get 403 with code "linkedin_verification_required". Use requiredLinks instead when you only need a LinkedIn URL. Default false.
- `micCheckRequired` (optional) — boolean; Require applicants to pass an on-device microphone quality check (live recording scored for audio and speech quality) before applying. Applicants get up to 2 attempts; the result (pass/warn/fail plus scores) is visible to you on each application via get_bounty_applications. Default false.
- `languageProficiencyRequirement` (optional) — object { language: `"en"`, minimumCefr: `"A2"` | `"B1"` | `"B2"` | `"C1"` | `"C2"` }; Require applicants to pass an English speaking-proficiency check before applying. The applicant records about 45 seconds of spontaneous speech in the app; it is transcribed and scored automatically, and only a scored result at or above minimumCefr qualifies. Recordings that cannot be scored (too little speech, low confidence) ask the applicant to retry. A worker's scored level is saved on their profile as a lasting credential, reused across every bounty without retesting (only a newer scored check replaces it), and re-checked against the bounty's current threshold at acceptance; a stored level below your threshold still requires a new recording. Shape: { language: 'en', minimumCefr: 'A2' | 'B1' | 'B2' | 'C1' | 'C2' }. Omit for no requirement. Separate from micCheckRequired.
- `karen` (optional) — boolean; RentAKaren order: hire an approved RentAKaren negotiator. Requires priceType 'hourly' at ≥ $5/h (≥ $10/h with an English languageProficiencyRequirement) and a deadline ≥ 4 days out (defaults to 14 days). Only callers approved by RentAHuman can apply or be accepted. The hired caller records calls in the in-app call console; final submission requires at least one call recorded by that worker (400 call_recording_required with callsPath). Follow callsPath while signed in to open the console. Buyers can review the recordings, summaries and transcripts. Put every personal detail (names, phone, account numbers, the full story) in startInstructions; keep title and description general (personal details in public fields are refused with karen_public_details) and call the worker "the caller", never a Karen ("Karen" in title, description, requirements, skillsNeeded, completionCriteria or evidenceCriteria is rewritten to "caller"). Cannot be changed after creation.
- `aiManaged` (optional) — `true`; Let our AI run the bounty: AI screening reviews applicants and accepts qualified ones, and AI review checks submitted work; RentAHuman or you approve payment. Turns on autoAccept and aiGrading on an ordinary application bounty; a requested photo, video or document upload becomes the bounty's evidence type.
- `asOrg` (optional) — `true`; Use only when organization settings are available for the authenticated account. Posts the bounty on behalf of that account's organization; the org is resolved server-side and its members can co-manage the bounty. Funding still comes from your own wallet. Returns 403 when organizations are unavailable or you don't belong to one.
- `submissionMode` (optional) — `"application"` | `"photo_upload"` | `"video_upload"` | `"document_upload"`; How users submit to this bounty. 'application' shows the standard application form; 'photo_upload' shows consent and image upload; 'video_upload' shows consent and video upload; 'document_upload' shows consent and document upload.
- `photoSubmission` (optional) — object { maxImages?: integer, minimumResolutionPx?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Photo-upload submission settings. Required when setting submissionMode to photo_upload.
- `videoSubmission` (optional) — object { maxVideos?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Video-upload submission settings. Required when setting submissionMode to video_upload.
- `documentSubmission` (optional) — object { maxDocuments?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Document-upload submission settings. Required when setting submissionMode to document_upload.
- `requiredLinks` (optional) — array of object; Links applicants must provide when applying. Max 10. Each has a type and optional label for custom types.; max items 10
- `applicationDetails` (optional) — array of object; Applicant detail items applicants may complete before applying. Blank rows are ignored. Supports text questions, acknowledgment checkboxes, one-file uploads (image, docx, pdf, txt, video, or audio), and one required camera-only live video with a script in label. Max 3 upload fields, 5 acknowledgment fields, and 1 live video field. Do not ask for passwords, OTP/2FA codes, API keys, private keys, seed phrases, government IDs, bank/card details, exact home addresses, dates of birth, or other sensitive personal information.; max items 10
- `startInstructions` (optional) — string; Private instructions shown to the worker only after they are accepted. Supports a {inviteCode} token that is replaced with the worker's invite code. Max 3000 chars.; max length 3000
- `lifecycleMessages` (optional) — object { onAccepted?: string, onRejected?: string, onSubmissionReceived?: string, onSubmissionApproved?: string, onSubmissionRejected?: string }; Auto-sent to the doer in the bounty conversation on lifecycle transitions. Supports {{name}}, {{bountyTitle}}, {{deadline}}, {{reason}} interpolation. Accepted/submission templates are only ever delivered to accepted applicants.
- `imageUrls` (optional) — array of string; Reference image URLs for the bounty (max 5).; max items 5
- `listingType` (optional) — `"seeking"` | `"offering"`; Whether this listing is seeking a human or offering a service.
- `estimatedDurationUnit` (optional) — `"minutes"` | `"hours"` | `"days"`; Display unit for the estimated duration.
- `dryRun` (optional) — boolean; Preview the bounty without creating it.
- `idempotencyKey` (optional) — string; Optional retry key. Reusing the same key returns the original result instead of creating a duplicate bounty.

---

### `list_bounties`

List bounties. Filter by status, category, skill, or price range. Set mine=true to list the bounties you own in every status (including unfunded, paused, and web UI posts). Without mine or status, lists bounties currently accepting applications, including partially filled and staffed ones.

**Parameters:**

- `status` (optional) — `"pending_deposit"` | `"pending_review"` | `"open"` | `"pending_funding"` | `"in_review"` | `"partially_filled"` | `"assigned"` | `"completed"` | `"paid"` | `"closing"` | `"closed"` | `"cancelled"` | `"paused"`; Filter by status: open, assigned, completed, paid, closed, or cancelled (other values return 400). Omit to list bounties accepting applications (with mine=true, all your bounties).
- `category` (optional) — string; Filter by category
- `skill` (optional) — string; Filter by required skill
- `minPrice` (optional) — number; Minimum price; min 0
- `maxPrice` (optional) — number; Maximum price; min 0
- `limit` (optional) — integer; Maximum number of results (default: 20, max: 100); min 1, max 100
- `includePartiallyFilled` (optional) — boolean; With status 'open', also include partially filled and staffed bounties still recruiting (default: true)
- `mine` (optional) — boolean; List bounties owned by the authenticated account, including bounties posted from the web UI and through MCP/API keys.

---

### `get_bounty`

Get detailed information about a specific bounty, including full description, requirements, completionCriteria, evidenceTypes, evidenceCriteria, and liveCaptureRequirement. Inspect those criteria before reviewing evidence. Automated submission findings are advisory and never approve work or release payment.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty

---

### `fund_bounty`

Fund an existing pending_deposit bounty. Always call with dryRun=true first: the preview returns the amount, service fee, total, current wallet balance, whether the wallet covers the total (walletCoversTotal), and any shortfall without charging anything. Show it to the account owner, and only after their explicit approval call again with confirm=true. A confirmed call may reserve available wallet funds immediately. If the wallet cannot cover the total, the response returns status requires_payment with deposit_url and checkout_total for the account owner to complete in hosted checkout. It may also return mppPayment, a single-use MPP card payment that credits the wallet and funds this bounty in one step; pay the checkout or mppPayment, never both. Reusing the tool returns an existing open checkout instead of charging twice. Unknown arguments are rejected. A bounty that is no longer pending_deposit returns 400. If the response includes setupUrl, the account owner must add their country there, then retry. Owner only.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the pending_deposit bounty to fund
- `dryRun` (optional) — boolean; true returns a no-charge preview: amount, service fee, total, and current wallet balance. Nothing is reserved, charged, or started.
- `confirm` (optional) — boolean; Must be true to fund. Set it only after showing the dryRun preview to the account owner and receiving their explicit approval.

---

### `update_bounty`

Update one of your ordinary one-shot bounties; only passed fields change. On create/edit, listing refusals return error_code, field and fix. Codes: description_time_policy_violation (also quoted, policyMinimum, earliestAllowed), bounty_content_refused, brand_impersonation, bounty_content_flagged. Follow fix, change field and retry; never retry unchanged wording. You can edit the listing text, price, application deadline, location and supportedCountries, screening settings, lifecycleMessages, seats, per-seat clocks, schedule, AI screening (autoAccept), and AI review of submissions (aiGrading). Status 'paused' stops applications and outreach, 'open' resumes, and 'closed' by itself closes an unassigned bounty and returns unused funding; 'completed' and 'paid' are system-managed. Use cancel_bounty to cancel. An edit cannot grow an escrow-funded pool above $10,000. On a wallet-funded bounty, a price raise or added seats first returns wallet_impact_confirmation_required with a cost preview and nothing charged: show the operator the cost, wallet balance before and after, and hiredSeatsRepriced, and only after they approve repeat the call with walletImpactAcknowledged: true and walletImpactCents from the preview. A raise after hiring reprices every hired worker. With aiGrading on, RentAHuman review may approve a submission and pay the worker for you; you can still decide first with review_submission. Clock changes (startWindowMinutes, responseWindowHours, autoExpireGhosts) apply only to seats confirmed after the edit; moving scheduledStartAt later pushes back confirmed workers' start deadlines and never brings one forward. The 2-hour seat-confirmation window is fixed. requiredLinks, completionQuestions, and adding or switching liveCaptureRequirement are refused once applications exist; removing live capture is always allowed. AI-managed bounties allow only task-content and deadline edits; QA and taste runs and ongoing-bounty settings are not editable here.

**Parameters:**

- `scheduleTimes` (optional) — object { startHour: integer, startMinute?: integer, endHour: integer, endMinute?: integer }; Local start/end hours and minutes for an existing task schedule. Availability, time increments, and timing restrictions depend on the task type; currently supported for managed sign campaigns. Keeps dates, timezone, and paid duration unchanged.
- `bountyId` (required) — string; The unique ID of the bounty to update
- `title` (optional) — string; New title for the bounty; min length 5, max length 200
- `description` (optional) — string; New description; min length 20, max length 5000
- `price` (optional) — number; New per-worker price (minimum $1). In-person bounties inside a configured minimum-pay area must meet that area's hourly minimum; fixed prices are divided by estimatedHours for this check. An edit that grows an escrow-funded pool cannot raise its total above $10,000.; min 1, max 1000000
- `priceType` (optional) — `"fixed"` | `"hourly"`; New price type
- `estimatedHours` (optional) — number; New estimated duration in hours (min 5 minutes = 0.083). For hourly bounties, an edit that grows an escrow-funded pool cannot raise its total above $10,000.; min 0.08333333333333333
- `deadline` (optional) — string; New application cutoff (ISO 8601), based on the user’s schedule. The API validates minimum notice when the deadline or physical location changes. This does not retime accepted workers.
- `requirements` (optional) — array of string; New requirements list
- `skillsNeeded` (optional) — array of string; New skills list
- `category` (optional) — `"computer-gigs"` | `"creative-gigs"` | `"crew-gigs"` | `"domestic-gigs"` | `"event-gigs"` | `"labor-gigs"` | `"talent-gigs"` | `"writing-gigs"`; New task category
- `location` (optional) — object { city?: string, state?: string, country?: string, isRemoteAllowed?: boolean }; Worker location target. Set country to an ISO country code without city or state to target every eligible worker in that country, including when remote work is allowed. Include city (and optionally state/country) for city-level targeting. Countries where RentAHuman is not available are rejected. Replaces the whole location: send every part you want to keep.
- `supportedCountries` (optional) — array of string; Replace the eligible-country list with the full new list of ISO country codes (country names are also recognized), e.g. ["US", "CA", "GB", "NZ", "AU"]. Omitting it leaves an explicit multi-country list in place, so a location-only edit never drops it; legacy bounties that only mirror a country-only location keep deriving that single country from location. On-site bounties (isRemoteAllowed false) with a location country accept only that one country. An empty array is stored as an explicit empty list; it never lifts a country-only or on-site country restriction (remove location.country first), while a remote city location with a country stays unrestricted as before. When location.country is set it must appear in the list. Countries where RentAHuman is not available and unrecognized values are rejected.; max items 250
- `status` (optional) — `"open"` | `"in_review"` | `"paused"` | `"closed"`; New owner-managed status. Owners can pause/unpause a bounty or close it before accepting a worker. 'completed' and 'paid' are system-managed from escrow and payout evidence and cannot be set directly.
- `identityRequired` (optional) — boolean; Require applicants to pass an identity check (government ID) before applying. Verified once per account and reused across bounties.
- `excludedParticipantSourceBountyIds` (optional) — array of string; Replace the exclude-previous-participants list: ids of your own earlier regular bounties (max 1000), never this bounty itself. An empty array clears it. Exclusion is evaluated live, so a source added later hides the bounty from its ever-accepted workers and blocks accepting them; pending applications are not auto-rejected.; max items 1000
- `linkedinVerifiedRequired` (optional) — boolean; Require applicants to have a verified LinkedIn: they must sign in with LinkedIn (OAuth) on their Rent A Human account before applying. A pasted LinkedIn URL does not count. Applicants without one get 403 with code "linkedin_verification_required". Use requiredLinks instead when you only need a LinkedIn URL. Default false. Can be switched on or off while the bounty is live, including after applications arrive; it applies to new applications only and never removes existing applicants.
- `micCheckRequired` (optional) — boolean; Require applicants to pass an on-device microphone quality check before applying (max 2 attempts; result visible on each application).
- `languageProficiencyRequirement` (optional) — object { language: `"en"`, minimumCefr: `"A2"` | `"B1"` | `"B2"` | `"C1"` | `"C2"` } | null; Require applicants to pass an English speaking-proficiency check before applying. The applicant records about 45 seconds of spontaneous speech in the app; it is transcribed and scored automatically, and only a scored result at or above minimumCefr qualifies. Recordings that cannot be scored (too little speech, low confidence) ask the applicant to retry. A worker's scored level is saved on their profile as a lasting credential, reused across every bounty without retesting (only a newer scored check replaces it), and re-checked against the bounty's current threshold at acceptance; a stored level below your threshold still requires a new recording. Shape: { language: 'en', minimumCefr: 'A2' | 'B1' | 'B2' | 'C1' | 'C2' }. Omit for no requirement. Separate from micCheckRequired. Pass null to remove the requirement. Changing the threshold applies to new applications and to every pending applicant at acceptance time.
- `responseWindowHours` (optional) — number | null; Hours an accepted worker has to show activity before their seat is treated as ghosted (1-720), or null to remove the ghost policy. Silent workers are nudged at half the window and flagged at the deadline.
- `autoExpireGhosts` (optional) — boolean; When true (with responseWindowHours set), ghosting workers’ seats are auto-released at the deadline and the listing reopens.
- `completionWindowHours` (optional) — integer | null; Retired for ordinary bounties, which have no completion deadline: a number is accepted for older clients and ignored, and null clears a value stored before the retirement.
- `startWindowMinutes` (optional) — integer | null; Start commitment: minutes after the worker confirms their seat (or after acceptance when skipAcceptanceConfirmation is true) by which they must press Start or upload evidence, otherwise the seat is eligible for release. When scheduledStartAt is set, the window runs from the scheduled start instead, so a worker who confirms early keeps the spot until then. Whole number of minutes from 5 to 1440 (24 hours). Distinct from the fixed 2-hour seat-confirmation window. There is no submission deadline: workers deliver within the bounty’s schedule and the poster reviews the evidence. Pass null to disable. Only affects seats armed after the edit; live start clocks are never re-timed.
- `attendanceRadiusMeters` (optional) — integer | null; In-person attendance: radius in meters around the job site (the bounty’s geocoded location) within which a hired worker counts as on site while attendance tracking is on. 50–2000, default 150. Only used when location.isRemoteAllowed is false. Pass null to restore the default.
- `scheduledStartAt` (optional) — string | null; When the work starts, for tasks booked for a specific time (a shift, an appointment, an event). ISO 8601 date-time with a UTC offset, in the future, e.g. 2026-10-03T07:30:00-07:00. With startWindowMinutes, the start deadline is this time plus the window rather than confirmation plus the window, so a worker who confirms early keeps the spot until then. Recommended for in-person shifts: set it with scheduledStartTimeZone (and estimatedHours as the shift length) so workers already booked at that time are not shown or alerted about the bounty and cannot double-book. Omit for tasks that start as soon as the worker confirms. The API never reads a schedule from the description. Pass null to clear. Moving it later also pushes back the start and submission deadlines of workers already confirmed; it never brings a live deadline forward.
- `scheduledStartTimeZone` (optional) — string | null; IANA time zone of the task location (e.g. America/Los_Angeles), used to show workers the scheduled start in local time. Needs scheduledStartAt. Set it on in-person shifts: double-booking protection only uses a scheduled start that has its time zone. Pass null to clear.
- `completionQuestions` (optional) — array of object; Mandatory questions the accepted WORKER answers when submitting evidence (for example "Which counter did you use?"). Max 10, prompts up to 300 characters, required defaults to true. Distinct from applicationDetails, which screens applicants before acceptance. Visible to workers before they apply. Locked once applications are received (409): accepted work snapshots the questions.; max items 10
- `spotsAvailable` (optional) — integer; Change the number of seats (humans needed, 1-2000). Cannot be set below spots already filled or grow an escrow-funded pool above $10,000. On a wallet-funded bounty the pool is resized in place: extra seats are debited from the poster wallet, freed seats are refunded to it.; min 1, max 2000
- `walletImpactAcknowledged` (optional) — boolean; Acknowledges the wallet impact of a wallet-funded bounty edit. Any edit that debits the poster wallet (adding seats via spotsAvailable, or raising the price) is first refused with error_code wallet_impact_confirmation_required and the exact amount; retry the same request with this set to true to apply the charge. A price raise after workers are hired also needs walletImpactCents.
- `walletImpactCents` (optional) — number; The cents value from the wallet_impact_confirmation_required response you are confirming. Required with walletImpactAcknowledged for a price raise after workers are hired; if the cost has changed since that response, the request is refused again with the new amount and nothing is charged.
- `keepApplicantsOnFill` (optional) — boolean; When true, pending applicants are kept (not auto-rejected) even after every seat escrow settles, so you can draw from the same pool after reopening or adding seats. By default applicants are already kept while seats are merely filled and are only auto-rejected at settlement. Default false.
- `autoAccept` (optional) — boolean; Turn AI screening on or off. When on, your blocklist always applies, qualified applicants are accepted, and clear mismatches are rejected; applications the review cannot decide stay pending for your manual review. Applications received while off stay pending; toggling on affects future applications only. Turning it off pauses AI screening at once: an automatic acceptance still in progress is refused and the applicant stays pending for you. Ignored only on older AI-managed bounties whose applicant review the platform runs. AI screening needs an application step.
- `aiGrading` (optional) — boolean; Turn AI review on or off. When on, our AI reviews each new evidence submission against what was agreed at acceptance. Its verdict is not shown to you, and RentAHuman review may approve the submission and pay the worker on your behalf; until then you can still approve, request changes or reject with review_submission. Default false. AI review needs submissions you review.
- `aiChatAssistant` (optional) — boolean; Reserved for the AI chat assistant, which is not available yet. Passing true is refused with 400 and the setting stays off.
- `autoAcceptMinMicScore` (optional) — number | null; Change the minimum overall mic score (1-5) for automatic review on micCheckRequired bounties — applications scoring below your configured cutoff are auto-rejected, at/above proceed toward acceptance — or pass null to reset to the platform default (3.0, below which applications only stay pending). Affects future applications only.
- `completionCriteria` (optional) — string; Updated definition of done.; min length 10, max length 2000
- `evidenceTypes` (optional) — array of `"text"` | `"photo"` | `"video"` | `"link"`; Updated evidence types. At least one required when present.; min items 1
- `evidenceCriteria` (optional) — string; Updated evidence requirements.; max length 2000
- `liveCaptureRequirement` (optional) — `"photo"` | `"video"` | null; Require new photo or video evidence captured with the device camera, or null to remove the requirement. Removing it is allowed at any time; adding or switching it is only allowed before applications are received. If both photo and video evidence are required, both must be captured live. Live video is limited to 60 seconds and 250 MiB.
- `checkIns` (optional) — object { enabled: boolean, intervalMinutes: integer }; Live selfie check-ins for in-person shifts: { enabled, intervalMinutes (whole minutes, 5-240) }. While a hired worker is on the job they take a camera-only, location-stamped selfie in the job chat every intervalMinutes from when they tap Start; you see each photo, its server time, distance to the job site and any flags, plus missed check-ins (never raw coordinates). enabled true requires an in-person bounty (location.isRemoteAllowed false). Omit it for the default: on every 15 minutes for sign-holding campaigns, off otherwise. Changing it affects check-ins from now on; past check-ins are kept. To make an on-site bounty with check-ins enabled remote, send checkIns with enabled false in the same update.
- `submissionMode` (optional) — `"application"` | `"photo_upload"` | `"video_upload"` | `"document_upload"`; How users submit to this bounty. 'application' shows the standard application form; 'photo_upload' shows consent and image upload; 'video_upload' shows consent and video upload; 'document_upload' shows consent and document upload.
- `photoSubmission` (optional) — object { maxImages?: integer, minimumResolutionPx?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Photo-upload submission settings. Required when setting submissionMode to photo_upload.
- `videoSubmission` (optional) — object { maxVideos?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Video-upload submission settings. Required when setting submissionMode to video_upload.
- `documentSubmission` (optional) — object { maxDocuments?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Document-upload submission settings. Required when setting submissionMode to document_upload.
- `reactivate` (optional) — boolean; Reactivate a bounty that was hidden after a period of inactivity.
- `requiredLinks` (optional) — array of object; Update required links. Only allowed when applicationCount is 0.; max items 10
- `applicationDetails` (optional) — array of object; Update application detail items. Blank rows are ignored. Max 3 upload fields, 5 acknowledgment fields, and 1 required camera-only live video field. May change after applications arrive; existing applications keep their original answers.; max items 10
- `lifecycleMessages` (optional) — object { onAccepted?: string, onRejected?: string, onSubmissionReceived?: string, onSubmissionApproved?: string, onSubmissionRejected?: string }; Auto-sent to the doer in the bounty conversation on lifecycle transitions. Supports {{name}}, {{bountyTitle}}, {{deadline}}, {{reason}} interpolation. Accepted/submission templates are only ever delivered to accepted applicants.

---

### `cancel_bounty`

Cancel one of your bounties by ID: pending and hired applications are closed and unreleased funding is refunded (wallet funds go back to your wallet). The response reports rejectedApplications and cancelledEscrows. A canonical reason is required; details are required only for other. The reason and optional details are private and are never shown to workers. Completed, paid or closed bounties cannot be cancelled. If work was delivered or payment released, or a dispute or review is open, it returns 409 with an error_code and a message saying what to do (for delivered work, use open_dispute). Safe to retry; a repeat returns alreadyCancelled: true.

**Parameters:**

- `reason` (required) — `"not_enough_applicants"` | `"applicants_not_fit"` | `"worker_not_completed"` | `"task_no_longer_needed"` | `"budget_timing_requirements_changed"` | `"other"`; Why the owner is closing or cancelling the entire bounty.
- `details` (optional) — string; Private explanation required only when reason is other. Maximum 500 characters.; max length 500, pattern `\S`
- `bountyId` (required) — string; The unique ID of the bounty

---

### `get_bounty_applications`

View applications to one of your bounties; while `hasMore` is true, pass the response's `nextCursor` as `cursor`. Applications come best match first (accepted first, rejected last, ties newest first). `completedTasksCount` and `totalEarnedCents` (USD cents released to them) are their RentAHuman track record; 0 means new. Each application includes the cover letter, availability, `isBlockedByOwner` and `isPreferredByOwner` (change them with `block_human` or `prefer_human` and the `humanId`; blocking is future-only and never removes an accepted worker), and `reviewSummary` (`averageRating` 1-5 or null, `reviewCount`, up to 3 `recentReviews`). A null averageRating with reviewCount 0 means no history, not a low score; weigh reviewSummary with `identitySignals` before accept_application. With a `languageProficiencyRequirement`, applications include `languageProficiency` with `status` passed, pending (still being scored), or failed, plus the scored `cefr` once scored. Hired seats (accepted, or expired with an escrow trace) include `jobOverview`, null for other applicants. Its `overallState` lets escrow state win over stale submission or chat state: released > resolved > refunded > disputed or rejected_disputed > seat_released > cancelled > the evidence state (awaiting_confirmation, awaiting_start, in_progress, evidence_in_review, changes_requested, redo_overdue, approved_awaiting_release, completed). `nextAction.kind` is the single next step: review_evidence, release_payment, pay_now, fund_seat, reject_or_wait, and view_dispute are yours (`actorIsOwner: true`); wait_for_confirmation, wait_for_start, wait_for_evidence, and wait_for_redo mean the worker moves next; none means settled; `nextDeadline`, `missingEvidence`, and `money` give the details. `isTeamReview: true` marks a disputed seat the platform team is reviewing because the 4-day poster review period lapsed (`teamReviewReopenUsed: true` once you used your single reopen); overallState and nextAction are unchanged.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty
- `status` (optional) — `"pending"` | `"accepted"` | `"rejected"` | `"withdrawn"` | `"expired"`; Filter by application status
- `limit` (optional) — integer; Max results per page (default 50, max 100); min 1, max 100
- `cursor` (optional) — string; `nextCursor` from the previous response

---

### `get_bounty_dataset`

List every file collected by one of your upload-collection bounties (submissionMode 'photo_upload', 'video_upload', or 'document_upload'). Returns download URLs for all accepted applications' uploaded photos, videos, and documents, grouped by applicant. To review uploads before accepting, use get_bounty_applications — pending applications include imageUrls/videoUrls/documentUrls. For a bulk zip archive of the same files, GET /api/bounties/{bountyId}/applications/dataset with your X-API-Key header. Owner only.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the upload-collection bounty (submissionMode photo_upload, video_upload, or document_upload)

---

### `get_applicant_context`

Get everything needed to decide on one application to your bounty, in one call: the listing (title, description, requirements, completion criteria, skills, pay, location rules, screening settings, and seats filled/open), the applicant's profile (display name, bio, skills, expertise, declared city and country, verified badge, rating, review count, completed jobs), the application (cover letter, availability, screening answers with uploaded files as owner-only download paths, submitted links, mic check, language result), and the outcome so far (`status`; `needsManualReview` when AI screening left the decision to you, with its note in `reason`; for a rejection, `reason` is the message the applicant received). To open a file, GET `https://rentahuman.ai{downloadPath}` with your API key; it redirects to a short-lived download link. Decide with accept_application or reject_application. Owner only.

**Parameters:**

- `bountyId` (required) — string; The bounty ID
- `applicationId` (required) — string; The application to read the decision context for

---

### `accept_application`

Accept a human's application for your bounty. For an escrow-funded seat, accepting takes the seat's payment from the bounty's funding and holds it in escrow until you release it; the worker is not paid yet. If the response's next_steps say payment comes after the work is completed, follow that instruction instead. For multi-person bounties, accept each applicant separately. If the seat needs funding and none covers it, this returns 402 and nothing is charged: for `escrow_not_funded`, fund this application with create_escrow_checkout and retry; `pool_drained` means the bounty's funding has no seat left. An application whose seat expired because the worker did not confirm in time can be accepted again. Other pending applications are kept even when every seat fills — a filled seat can still be released and refilled — and are auto-rejected only once every seat's escrow is settled (released/paid). Pass optional `idempotencyKey` to make this safe to retry (a replayed key returns the original result instead of duplicating). Check the applicant's `reviewSummary` from get_bounty_applications before accepting; a null averageRating means no history, not a bad record. On bounties with a `languageProficiencyRequirement`, accepting an applicant whose current scored level does not meet the bounty's current threshold returns 409 `language_proficiency_unsatisfied`.

**Parameters:**

- `bountyId` (required) — string; The bounty ID
- `applicationId` (required) — string; The application ID to accept
- `response` (optional) — string; Optional message to the applicant, up to 1000 characters.
- `idempotencyKey` (optional) — string; Optional retry key. Reusing the same key returns the original result instead of accepting twice.

---

### `reject_application`

Reject a pending application to your bounty. The optional `response` is sent to the applicant as the reason.

**Parameters:**

- `bountyId` (required) — string; The bounty ID
- `applicationId` (required) — string; The application ID to reject
- `response` (optional) — string; Optional reason shown to the applicant, up to 1000 characters.

---

### `expire_application`

Release a previously accepted seat when the worker has ghosted (no message or submission after being accepted). Transitions their application to 'expired', frees the seat by decrementing the bounty's filled-seat count, reopens the listing so a pending applicant can take the freed seat, and cancels/refunds any escrow bound to that application (wallet-funded escrows return to your wallet). The released worker is notified. Owner only; only works on 'accepted' applications.

**Parameters:**

- `bountyId` (required) — string; The bounty ID
- `applicationId` (required) — string; The accepted application whose seat should be released
- `reason` (optional) — string; Optional human-readable reason shown to the released worker (e.g. why the seat was reclaimed). Defaults to a generic no-activity explanation.

---

### `get_bounty_outreach_status`

See the automatic outreach the platform ran for one of your bounties: how many candidate humans were emailed (with timestamps), how many alerts are still queued, progress toward the delivered-alert target, and how many contacted humans applied or responded. Owner only. Use this to check whether a bounty is getting in front of qualified humans before deciding to boost.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty

---

### `boost_bounty_outreach`

Raise the outreach target for one of your open bounties by another wave of matched humans (up to 300 more, capped at 1250 lifetime) and run that wave right now. Owner only. Rate-limited to once per bounty per 24 hours. Use get_bounty_outreach_status first to see current reach.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty

---

### `pay_enterprise_bounty`

Pay an accepted worker on a legacy enterprise bounty (older bounties that were not escrow-funded) from the owner wallet. New bounties are always escrow-funded; use release_payment for them. This is an irreversible financial action: call it only when the user explicitly directs payment. For jobs in the evidence review flow the submitted evidence must be approved first and acknowledgeRelease must be true; otherwise HTTP 409 returns the code, the amount and the worker. If the user asks for evidence review instead of payment, use get_bounty, get_submission, and review_submission. The amount, worker, and wallet are loaded from stored records. Insufficient wallet funds return 402 and are safe to retry after topping up. Owner or bounty-owning agent only.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the enterprise bounty to pay
- `conversationId` (optional) — string; Conversation for the completed application. Required when the bounty has more than one conversation.
- `acknowledgeRelease` (optional) — boolean; Required for ordinary bounty jobs in the evidence review flow: pass true to confirm the release pays the worker and is final. Without it the API answers HTTP 409 release_acknowledgement_required with the amount and the worker.

---

### `book_sign_campaign`

Book people to hold your sign on San Francisco (or New York) street corners through the RentAHuman Signs API. Use this instead of create_bounty for any sign-holding, sign-spinning or human-billboard job: you give the design, we print it and handle pickup, and you get approved sign holders, a shift briefing and check-ins. Requires RENTAHUMAN_API_KEY. Always call with dryRun omitted or true first: it validates and prices the campaign and checks capacity without booking or charging, and returns earliestStart (shift dates must be at least the minimum lead time ahead). Show the user the price and dates. Then call again with dryRun: false, confirm: true, an operationId and the artwork (url or base64; PNG, JPEG or PDF): it uploads the design, books the campaign and pays from the wallet first; if the wallet is short it returns a hosted checkout URL for a human to pay. Card details are never taken. Reuse the operationId to retry. Track the campaign at statusPath (GET).

**Parameters:**

- `dryRun` (optional) — boolean; Defaults to true: quote only. Pass false (with confirm: true) to book and pay.
- `confirm` (optional) — boolean; Required true for a live booking, which pays from the wallet first.
- `operationId` (optional) — string; Idempotency key and campaign ID (16-64 letters, digits, _ or -). Reuse it to retry a booking safely; a booked campaign is returned instead of booked twice.; pattern `^[A-Za-z0-9_-]{16,64}$`
- `city` (optional) — `"sf"` | `"nyc"`
- `spots` (required) — array of object; One public-sidewalk point per sign holder, inside the city (max 20).; min items 1, max items 20
- `dates` (required) — array of string; an array of at least 1 item(s); min items 1
- `startHour` (required) — integer; an integer
- `endHour` (required) — integer; an integer
- `signReturn` (optional) — object { location: string, instructions: string }; Where the crew leaves the printed signs after the last day, and what to do.
- `specialInstructions` (optional) — string
- `laborCentsPerHour` (optional) — integer; an integer
- `artwork` (optional) — object { url?: string, base64?: string, contentType: `"image/png"` | `"image/jpeg"` | `"application/pdf"`, orientation?: `"portrait"` | `"landscape"` }; The sign design. Required to book; optional for a quote.

---

### `get_cake_quote`

Check Daymaker cake delivery coverage and get per-size pricing before ordering. Prices are the Daymaker base price plus the 18% RentAHuman service fee and are paid from the authenticated agent wallet. contact_name is the person the courier asks for, not the company name. For NYC deliveries provide address2 or a recipient phone. A recipient phone is often the difference between a successful delivery and a returned cake.

**Parameters:**

- `address` (optional) — string; a string at most 500 character(s) long; min length 1, max length 500, pattern `\S`
- `address2` (optional) — string; a string at most 500 character(s) long; min length 1, max length 500, pattern `\S`
- `city` (optional) — string; a string at most 200 character(s) long; min length 1, max length 200, pattern `\S`
- `state` (optional) — string; a string at most 100 character(s) long; min length 1, max length 100, pattern `\S`
- `zip` (optional) — string; a string at most 20 character(s) long; min length 1, max length 20, pattern `\S`
- `website_url` (optional) — string; a string matching the pattern ^https?:\/\/; min length 1, max length 2000, pattern `^https?:\/\/`
- `quantity` (optional) — integer; a number less than or equal to 100; min 1, max 100

---

### `send_cake`

Send a custom cake through Daymaker. Prices are the Daymaker base price plus the 18% RentAHuman service fee and are paid from the authenticated agent wallet. contact_name is the person the courier asks for, not the company name. For NYC deliveries provide address2 or a recipient phone. A recipient phone is often the difference between a successful delivery and a returned cake. The design must contain exactly one of message_text, image_svg, image_url, or image_base64. idempotency_key must be a fresh UUID for each distinct order; reuse that exact UUID verbatim when retrying the same order so neither the wallet nor Daymaker is charged twice.

**Parameters:**

- `recipient` (required) — object { company: string, contact_name: string, address?: string, address2?: string, city?: string, state?: string, zip?: string, website_url?: string, phone?: string, notes?: string, delivery_date?: string }
- `cake_size` (required) — `"6in"` | `"8in"` | `"10in"` | `"12in"` | `"half_sheet"` | `"sheet"`
- `cake_shape` (optional) — `"round"` | `"square"`
- `design` (required) — object { message_text?: string, image_svg?: string, image_url?: string, image_base64?: string, image_mime?: `"image/png"` | `"image/jpeg"` | `"image/webp"` }
- `card_message` (optional) — string; a string at most 2000 character(s) long; min length 1, max length 2000, pattern `\S`
- `idempotency_key` (required) — string; a string at most 200 character(s) long; min length 1, max length 200, pattern `\S`
- `metadata` (optional) — object

---

### `get_cake_status`

Get the current status of one cake order owned by the authenticated agent. This reconciles an ambiguous provider submission when safe and refreshes Daymaker delivery state and delivery photos for placed orders.

**Parameters:**

- `order_id` (required) — string; a string matching the pattern ^cake_[a-f0-9]{40}$; min length 1, max length 100, pattern `^cake_[a-f0-9]{40}$`

---

### `create_negotiation`

Retired for new orders: it now returns karen_orders_are_bounties and creates nothing. To hire a human negotiator (RentAKaren), call create_bounty with karen: true, priceType "hourly" (at least $5/h, $10/h with an English languageProficiencyRequirement), a deadline at least 4 days out, a general public title and description that calls the worker "the caller", and every personal detail (names, numbers, the full story) in startInstructions. Only approved callers can apply, and they record every call. The other negotiation tools still manage negotiations created before this change.

**Parameters:**

- `title` (required) — string; Short title, e.g. "Lower my Comcast bill"; min length 1, max length 120, pattern `\S`
- `category` (required) — `"bill"` | `"refund"` | `"rent"` | `"car"` | `"subscription"` | `"vendor"` | `"travel"` | `"other"`
- `counterparty` (required) — string; Who the negotiator will deal with, e.g. "Comcast"; min length 1, max length 120, pattern `\S`
- `context` (required) — string; Background the negotiator needs: account situation, history, leverage, deadlines.; min length 1, max length 4000, pattern `\S`
- `documentUrls` (optional) — array of string; Up to 10 https links to supporting documents.; max items 10
- `objectives` (required) — array of object; 1-5 objectives, each { description, target, bonusCents }. Objective IDs (obj_1, obj_2, ...) follow this order.; min items 1, max items 5
- `hourlyRateCents` (optional) — integer; Hourly rate in cents. Defaults to 2500.; min 1500, max 50000
- `capMinutes` (required) — integer; Maximum billable minutes (30-2400, multiple of 15). Billing never exceeds this cap.; min 30, max 2400
- `authorization` (required) — object { rightsConfirmed: `true`, mayDisclose: string, mayAgreeTo: string, neverCommitTo?: array of string, recordingAllowed?: boolean }

---

### `get_negotiation`

Get one of your negotiations: status, brief, authorization, objectives with submitted evidence, logged and approved minutes, escrow breakdown, assigned negotiator, recorded calls (date, duration, outcome, negotiator notes, a 2–3 line summary and the full transcript; transcriptStatus is transcribing until it is ready), and settlement once settled. Calls are only recorded when authorization.recordingAllowed is true. Use it to find objective IDs for approve_objective. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `negotiationId` (required) — string; Negotiation ID returned by create_negotiation; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`

---

### `list_negotiations`

List the negotiations you have posted with status, rate, cap, logged and approved minutes, escrowed amount, service fee and total wallet charge, and objective progress. Requires RENTAHUMAN_API_KEY.

**Parameters:**

None

---

### `approve_hours`

Approve every time entry your negotiator has logged so far. Approved minutes are paid at settlement at the hourly rate, never beyond the cap; unapproved minutes are not paid. Idempotent. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `negotiationId` (required) — string; Negotiation ID returned by create_negotiation; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`

---

### `approve_objective`

Approve an objective the negotiator marked as met, so its flat bonus is paid at settlement. Review the evidence from get_negotiation first. Pass rejectReason instead to reject the evidence; the negotiator can resubmit, and a bonus that is never approved is refunded at settlement. Approval is idempotent. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `negotiationId` (required) — string; Negotiation ID returned by create_negotiation; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`
- `objectiveId` (required) — string; Objective ID from get_negotiation, e.g. "obj_1"; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`
- `rejectReason` (optional) — string; Omit to approve. Provide a reason to reject the submitted evidence instead; the negotiator can resubmit.; min length 1, max length 1000, pattern `\S`

---

### `message_negotiator`

Send a message to the negotiator assigned to your negotiation, for example to answer a question or adjust instructions within your authorization. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `negotiationId` (required) — string; Negotiation ID returned by create_negotiation; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`
- `content` (required) — string; a string matching the pattern \S; min length 1, max length 4000, pattern `\S`

---

### `settle_negotiation`

Finish a negotiation: approved hours and approved objective bonuses are released to the negotiator from escrow, and everything unused is refunded to your wallet. Approve hours and objectives first; anything unapproved at settlement is not paid. Irreversible, but safe to retry. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `negotiationId` (required) — string; Negotiation ID returned by create_negotiation; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`

---

### `fund_negotiation`

Retry funding a pending_funding negotiation's escrow from your wallet after a top-up. Returns the shortfall when the wallet still cannot cover it. If the wallet is short, top it up (get_wallet_balance and deposit_wallet where those tools exist; otherwise the person adds funds at https://rentahuman.ai/account/wallet), then call fund_negotiation. Idempotent once funded. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `negotiationId` (required) — string; Negotiation ID returned by create_negotiation; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`

---

### `cancel_negotiation`

Cancel before a negotiator is hired; the whole escrow returns to the wallet. Fails once someone is hired. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `negotiationId` (required) — string; Negotiation ID returned by create_negotiation; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`

---

### `create_humanization`

Hire one human to rewrite private text without generative AI. Requires a fixed worker price, turnaround, transformation goal, and stable idempotencyKey. Provide a short `subject` (PUBLIC — shown in the listing title, e.g. "essay on AI infrastructure"; never put private content in it) so workers know what kind of text they are applying to rewrite. Optionally provide applicantScreening.aiGeneratedSourceText to require a proportional pre-acceptance rewrite sample (capped at 500 words) with its own document, continuous screen recording, and Pangram analysis. The sample is reviewed automatically, and some samples go to manual review. A resume upload can also be required. The main source is revealed only to the accepted worker. Pangram scores are evidence, not proof of authorship, and never release payment by themselves. Do not use this tool to falsify credentials, impersonate recommendation authors, violate academic-integrity rules, or evade required AI disclosure. BETA: pass aiManaged: true to have the platform recruit and vet writers, accept one, review the delivered rewrite and its Pangram analysis, release payment for approved work, refund unused budget, and report back. Requires USD and turnaroundMinutes >= 120; poll get_humanization for progress and the final report.

**Parameters:**

- `format` (required) — `"text"`
- `sourceText` (required) — string; a string matching the pattern \S; min length 1, max length 100000, pattern `\S`
- `transformation` (required) — `"paraphrase"` | `"tone"` | `"clarity"` | `"shorten"` | `"expand"` | `"general_rewrite"`
- `subject` (optional) — string; a string matching the pattern \S; min length 3, max length 80, pattern `\S`
- `instructions` (optional) — string; a string at most 5000 character(s) long; min length 1, max length 5000
- `turnaroundMinutes` (required) — integer; a number less than or equal to 10080; min 5, max 10080
- `priceCents` (required) — integer; a number less than or equal to 100000000; min 100, max 100000000
- `currency` (optional) — `"USD"`
- `applicantScreening` (optional) — object { aiGeneratedSourceText: string, percentage?: integer, maximumWords?: integer, instructions?: string }
- `requireResume` (optional) — boolean
- `aiManaged` (optional) — `true`
- `idempotencyKey` (required) — string; a string matching the pattern ^[A-Za-z0-9._:-]+$; min length 8, max length 128, pattern `^[A-Za-z0-9._:-]+$`

---

### `get_humanization`

Get an owned humanization bounty, including funding and assignment state, deadline attempts, submitted document and screen recording, applicant screening and delivery review status, and Pangram results.

**Parameters:**

- `humanizationId` (required) — string; a string matching the pattern ^[A-Za-z0-9_-]+$; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`

---

### `get_bounty_submissions`

List the evidence submissions workers have submitted for one of your bounties. Each finalized submission includes advisory automated checks with `checkCoverage`, a neutral `recommendation`, structured `findings`, and per-file check results. A recommendation does not decide whether the work is valid and does not release or block payment. Filter by review status (pending_review, approved, rejected, redo_requested). Owner only.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty whose evidence submissions to list
- `status` (optional) — `"pending_review"` | `"approved"` | `"rejected"` | `"redo_requested"`; Filter submissions by review status: pending_review, approved, rejected, or redo_requested.

---

### `get_submission`

Get a single evidence submission for one of your bounties, including its uploaded files and advisory automated-check report. Before deciding, use get_bounty for the completion and evidence criteria and inspect every uploaded file directly. If your host cannot open a file type or URL, disclose that limitation instead of deciding from metadata or automated findings. Owner only.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty the submission belongs to
- `submissionId` (required) — string; The unique ID of the evidence submission to retrieve

---

### `get_submission_context`

Get everything needed to decide on one evidence submission for one of your bounties, in one call: the listing (title, description, requirements, start instructions, and whether it was edited after the worker was accepted), the evidence types and completion questions agreed at acceptance, the submission's files typed photo/video/document, notes, links, completion answers, review cycle and advisory checks, earlier redo reasons, and the last messages of this worker's job chat labelled worker/owner/platform. Inspect every file before deciding with review_submission. Owner only.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty the submission belongs to
- `submissionId` (required) — string; The unique ID of the evidence submission to retrieve

---

### `review_submission`

Record a decision on a worker's evidence submission. Only call after the user explicitly chooses a decision or explicitly delegates criteria-based evidence decisions to you. First call get_bounty and get_submission, compare the stated completion/evidence criteria with every uploaded file, and do not decide if you cannot inspect a file. `action` is 'approve', 'reject', or 'request_redo'; `response` is required for reject and request_redo. Available while the job is evidence_in_review (the worker marked the task complete with evidence); other states return HTTP 409 job_state_conflict. Successful responses include `jobState` (state, allowed next actions, `attempt` {used, max}, `redoDueAt`, `isRedoOverdue`), and so do 409 refusals about the evidence state when it can be read; other 409s do not. request_redo is capped at 3 cycles per job, after which HTTP 409 redo_limit_reached leaves only approve or reject. request_redo may set a redo deadline with `redoWindowMinutes` (15-10080) or an absolute `redoDueAt`; the worker's resubmission appends to the earlier evidence and every deliverable the bounty declared (each evidence type and each required completion question) must be present before it is accepted. While the deadline has not passed, reject from changes_requested returns HTTP 409 redo_deadline_pending; after it passes (`isRedoOverdue: true`) reject becomes available there too. Pass `expectedState` (the jobState you last saw) so a worker resubmitting in the meantime turns your reject into HTTP 409 job_state_conflict instead of landing on the new evidence. reject is final and files no dispute: the worker has 48 hours to appeal (rejection.disputeDeadline). Payment and seat stay held, then are refunded and released if no appeal. If reject returns HTTP 409 dispute_unavailable, retry, or use request_redo instead. Automated `recommendation` and findings are advisory only and must never be treated as the verdict. This tool does not move money: after approve, use release_payment with acknowledgeRelease: true. Owner only.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty the submission belongs to
- `submissionId` (required) — string; The unique ID of the evidence submission to review
- `action` (required) — `"approve"` | `"reject"` | `"request_redo"`; Review decision: 'approve' accepts the evidence, 'reject' declines it, 'request_redo' asks the worker to resubmit corrected evidence.
- `response` (optional) — string; Message shown to the worker. Required and non-blank for reject and request_redo; optional for approve.; max length 1000
- `redoWindowMinutes` (optional) — unknown; request_redo only: how long the worker has to add the requested evidence, in minutes (15-10080). Sets the redo deadline; once it passes, reject becomes available on the job. Mutually exclusive with redoDueAt.
- `redoDueAt` (optional) — string; request_redo only: absolute ISO-8601 redo deadline, between 15 minutes and 7 days from now. Mutually exclusive with redoWindowMinutes.
- `expectedState` (optional) — `"in_progress"` | `"evidence_in_review"` | `"changes_requested"` | `"rejected"` | `"rejected_disputed"` | `"approved_awaiting_release"` | `"released"` | `"completed"` | `"disputed"` | `"resolved"` | `"refunded"` | `"cancelled"`; Optional optimistic-concurrency guard: the job state you last observed (e.g. 'changes_requested' when rejecting after a redo deadline). The review is refused with HTTP 409 job_state_conflict if the job has since moved, such as the worker resubmitting.

---

### `create_escrow_checkout`

Fund an escrow, wallet-first: when your wallet balance covers the total the escrow is funded instantly (status 'funded', fundingSource 'wallet') with no checkout step; otherwise a hosted checkout session is returned to deposit the difference. Supports two flows: (1) bounty: provide bountyId + applicationId, (2) conversation: provide conversationId (uses the latest payment_offer amount). Pass an optional `idempotencyKey` to make funding safe to retry — replaying the same key returns the original result instead of creating a duplicate escrow. When status is requires_payment, tell the operator checkoutTotal (what checkout will charge; it includes a service fee) before they pay. Once paid, the webhook transitions the escrow to 'funded'. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `bountyId` (optional) — string; a string at least 1 character(s) long; min length 1
- `applicationId` (optional) — string; a string at least 1 character(s) long; min length 1
- `conversationId` (optional) — string; a string at least 1 character(s) long; min length 1
- `idempotencyKey` (optional) — string

---

### `get_escrow`

Get details of a specific escrow by ID. Returns status, amounts, fees, parties, and status history (auditLog). Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `escrowId` (required) — string; a string at least 1 character(s) long; min length 1

---

### `list_escrows`

List your escrows as a poster. Returns escrows you've created, with optional status filter. You can look up escrow(s) for a specific application via `applicationId`, or by `bountyId` with optional `humanId`. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `status` (optional) — string
- `applicationId` (optional) — string
- `bountyId` (optional) — string
- `humanId` (optional) — string

---

### `get_earnings_balance`

Check the authenticated account's withdrawable earnings from released escrows, direct payments, and wallet balance, plus held/disputed/withdrawn totals. Use this before withdraw_earnings. Requires RENTAHUMAN_API_KEY.

**Parameters:**

None

---

### `withdraw_earnings`

Withdraw all pending earnings to the authenticated account's linked payout account. This processes released escrow payouts, completed direct-transfer payouts, and wallet balance together. Requires completed payout account setup and RENTAHUMAN_API_KEY.

**Parameters:**

None

---

### `confirm_delivery`

Confirm that a worker has satisfactorily completed the task. Transitions the escrow from 'delivered' to 'completed' (or 'warranty_hold' if a warranty plan is active). Refused with HTTP 409 unless the escrow is bound to an accepted application or a live booking and, for ordinary bounties, finalized evidence exists. This is separate from release_payment. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `escrowId` (required) — string; a string at least 1 character(s) long; min length 1

---

### `release_payment`

Pay the worker for a job: release escrow funds to them and complete the task. This is an irreversible financial action: call it only when the user has explicitly decided to pay. If the API needs more before it can pay (for example an acknowledgement, a funded escrow, or a review step), it returns an error explaining what is missing. A successful explicit release approves the canonical pending submission; use review_submission first only for a redo or rejection. For ordinary bounty jobs pass acknowledgeRelease: true after confirming the amount and worker with the user; without it HTTP 409 release_acknowledgement_required returns the next action, amountCents, workerPayoutCents and worker. If evidence approval needs retry after payment commits, HTTP 503 evidence_approval_pending returns paymentReleased: true; retrying cannot pay twice, and the retry answers HTTP 409 "Funds have already been released", which means approval finished. For managed chat work, status approving_payment with released false means approval is saved but payment is still queued; poll get_escrow before reporting that the worker was paid. If the job has no funded escrow yet, pass bountyId + applicationId (or conversationId): the tool funds the escrow from your wallet balance automatically and then releases. If that application is still pending, the funding step also accepts the applicant, so use this only for a worker the user has hired and decided to pay. When the wallet cannot cover it, it returns status deposit_required: have the operator pay checkoutUrl when one is returned, otherwise add funds with deposit_wallet, then call release_payment again. Optionally pass `applicationId` alongside escrowId to assert the intended application; a mismatch is refused to prevent paying the wrong worker. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `escrowId` (optional) — string; The escrow to release. Optional when bountyId + applicationId (or conversationId) identify the job.; min length 1
- `applicationId` (optional) — string; The application this payment is for. With escrowId, a mismatch is refused (HTTP 409 escrow_application_mismatch). With bountyId, it also identifies the job to fund.
- `acknowledgeRelease` (optional) — boolean; Required for ordinary bounty jobs in the evidence review flow: pass true to confirm the release pays the worker and is final. Without it the API answers HTTP 409 release_acknowledgement_required with the amount and the worker.
- `idempotencyKey` (optional) — string; Optional. Used only when bountyId + applicationId or conversationId fund the job first; reusing it replays the same funding result instead of funding twice.
- `bountyId` (optional) — string; With applicationId: identifies the job so an unfunded escrow is funded from your wallet balance before release. If the wallet is short, the tool returns status deposit_required with a checkout link or a deposit_wallet step.; min length 1
- `conversationId` (optional) — string; Identifies a conversation job (uses its latest payment_offer) to fund from your wallet and release when no funded escrow exists yet.; min length 1

---

### `cancel_escrow`

Cancel an escrow and refund the amount. Can only cancel escrows that haven't been completed yet (status: funding or funded). Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `escrowId` (required) — string; a string at least 1 character(s) long; min length 1

---

### `rent_human`

Hire a specific human. Pass fundingMethod: wallet and a stable idempotencyKey to reserve existing wallet funds including fees, without checkout or auto-top-up. A short wallet returns insufficient_wallet_funds and required/available/shortfall cents; add funds and retry the same key. Wallet retries with the same key return the same hire, including after cancellation; changed inputs need a new key. Omit fundingMethod for a hosted checkout: it returns checkoutUrl for the account owner to pay, and the hire is funded and the human assigned only after payment. Without wallet funding, each call starts a new hire and checkout link. If checkout returns status insufficient_funds, add wallet funds and retry with fundingMethod: wallet and a new idempotencyKey; profile_country_required means set your country at setupUrl first. Funding holds escrow and does not pay the worker. After work, use confirm_delivery and release_payment. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `fundingMethod` (optional) — `"wallet"` | `"checkout"`; wallet spends existing wallet funds; omit it (or pass checkout) for a hosted checkout link.
- `idempotencyKey` (optional) — string; 1-200 characters; required with fundingMethod wallet. Reuse it only to retry the same hire.; min length 1, max length 200
- `humanId` (required) — string; Profile ID of the human to hire; min length 1
- `taskTitle` (required) — string; Task title, 5-200 characters; min length 5, max length 200
- `taskDescription` (required) — string; What to do, at least 10 characters; min length 10
- `price` (required) — number; Worker pay in USD, 1-10,000; fees are added on top; min 1, max 10000
- `estimatedHours` (optional) — number; Hours of work, at least 0.083 (5 minutes); defaults to 1; min 0.08333333333333333

---

### `get_my_rentals`

List all your active and past rentals. Returns rental status, next action needed, human info, and amounts. Use this to track the progress of your rentals and know what to do next (e.g., confirm delivery, release payment). Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `status` (optional) — string

---

### `create_personal_bounty`

Commission a specific human after agreeing on terms, deadline and completion criteria. Pass fundingMethod: wallet with a stable idempotencyKey to reserve existing wallet funds including fees; insufficient_wallet_funds returns required/available/shortfall cents without checkout or auto-top-up. Retry the same key for the same hire; changed inputs or a new hire need a new key. Omit fundingMethod for a hosted checkout. Funding does not complete work or pay the worker. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `fundingMethod` (optional) — `"wallet"` | `"checkout"`; wallet spends existing wallet funds; omit it (or pass checkout) for a hosted checkout link.
- `idempotencyKey` (optional) — string; 1-200 characters; required with fundingMethod wallet. Reuse it only to retry the same hire.; min length 1, max length 200
- `humanId` (required) — string; a string at least 1 character(s) long; min length 1
- `title` (required) — string; a string at most 200 character(s) long; min length 5, max length 200
- `description` (required) — string; a string at most 5000 character(s) long; min length 20, max length 5000
- `completionCriteria` (required) — string; a string at most 2000 character(s) long; min length 20, max length 2000
- `price` (required) — number; a number less than or equal to 10000; min 1, max 10000
- `deadline` (required) — string; a string at least 1 character(s) long; min length 1
- `estimatedHours` (optional) — number; a number greater than or equal to 0.08333333333333333; min 0.08333333333333333
- `category` (optional) — `"computer-gigs"` | `"creative-gigs"` | `"crew-gigs"` | `"domestic-gigs"` | `"event-gigs"` | `"labor-gigs"` | `"talent-gigs"` | `"writing-gigs"`
- `conversationId` (optional) — string

---

### `open_dispute`

Open a dispute on an escrow you funded. Only the buyer who funded the escrow may dispute it; a call on an escrow where you are the assigned human is refused with HTTP 403. Use this when you believe the work was not completed satisfactorily or the terms were not met. Can be used on escrows in locked, delivered, completed, or warranty_hold status. For personal bounties, opening a dispute before the auto-release date prevents the automatic payment. The escrow is held until the dispute is resolved. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `escrowId` (required) — string; a string at least 1 character(s) long; min length 1
- `category` (required) — `"not_delivered"` | `"poor_quality"` | `"not_as_described"` | `"communication_issue"` | `"non_payment"` | `"fraud"` | `"other"`
- `description` (required) — string; a string at least 20 character(s) long; min length 20
- `urls` (optional) — array of string

---

### `browse_services`

Browse and search services offered by humans. Use this to find services to book. Returns services with provider info, pricing, and estimated duration. Each result includes the humanId and serviceId needed to book.

**Parameters:**

- `search` (optional) — string; Search by service title, description, or provider name
- `category` (optional) — string; Filter by service category
- `sort` (optional) — `"newest"` | `"price-low"` | `"price-high"`; Sort order (default: newest)
- `limit` (optional) — integer; Max results per page (default: 10, max: 48); min 1, max 48
- `page` (optional) — integer; Page number for pagination (default: 1); min 1

---

### `get_service_availability`

Get booked time slots for a human's services on a specific date. Use this to check which times are already booked before making a service booking. Returns an array of booked time slots.

**Parameters:**

- `humanId` (required) — string; The unique ID of the human offering the service; min length 1
- `date` (required) — string; The date to check availability for (YYYY-MM-DD format)

---

### `book_service`

New service bookings are temporarily paused. Calls return 403 with code service_bookings_unavailable before funds or booking state change; use create_bounty to request the work instead. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `humanId` (required) — string; The unique ID of the human offering the service; min length 1
- `serviceId` (required) — string; The unique ID of the service to book
- `date` (required) — string; The date for the booking (YYYY-MM-DD format)
- `startTime` (required) — string; The start time for the booking (HH:mm format)

---

### `list_my_service_bookings`

List service bookings made by this agent. Returns bookings where this agent (via API key) has booked services from humans. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `status` (optional) — `"pending_payment"` | `"pending_approval"` | `"confirmed"` | `"declined"` | `"auto_declined"` | `"completed"` | `"cancelled"` | `"expired"`; Filter by booking status

---

### `check_account_status`

Check whether RENTAHUMAN_API_KEY is configured and which account-scoped actions are available.

**Parameters:**

None

---

### `list_api_keys`

List every API key on your account, newest first, including revoked ones (isActive false, revokedAt set). Each item has id (pass it to revoke_api_key), keyPrefix, name, isActive, createdAt, lastUsedAt, revokedAt, isSlackProvision, and nullable slackWorkspaceName, slackWorkspaceDomain, slackUserRealName, and slackUserHandle. Never returns the raw key value. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

None

---

### `create_api_key`

Create a new API key for your account. The raw key is returned once in the `key` field — store it securely, it cannot be retrieved later. Get the new key's id from list_api_keys. This session keeps using the current key until you change RENTAHUMAN_API_KEY or rerun `rentahuman-mcp setup`. Maximum 25 active keys per account; revoke one first if you hit the limit. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `name` (required) — string; A descriptive name for this key (e.g., 'production', 'dev-testing', 'backup'). Max 50 characters.

---

### `revoke_api_key`

Revoke an API key by its ID, permanently deactivating it. WARNING: If you revoke the key this server is using, it loses API access until you set a different valid key (RENTAHUMAN_API_KEY or `rentahuman-mcp setup`). Use list_api_keys first to see key IDs. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `keyId` (required) — string; The ID of the API key to revoke (from list_api_keys).

---

### `send_money`

Tip or reimburse a worker after their work on a bounty you own is released. Pass that `bountyId`, or the API refuses with bounty_required, bounty_not_owned, or work_not_released. Tips and reimbursements on a bounty are limited per worker; if a payment would go over the limit, the API refuses with tip_cap_exceeded. The API uses wallet balance first and otherwise returns a hosted checkout URL (no checkout when idempotencyKey is set); tell the operator checkoutTotal (what checkout will charge, including the service fee) before they pay. Other refusals carry an error message; show it to the operator. Use `description` as a free-text memo. If the authenticated account has blocked the recipient, the API refuses unless override is true. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `recipientId` (optional) — string; a string at least 1 character(s) long; min length 1
- `recipientEmail` (optional) — string; a string matching the pattern ^[^\s@]+@[^\s@]+\.[^\s@]+$; pattern `^[^\s@]+@[^\s@]+\.[^\s@]+$`
- `amount` (required) — number; a number less than or equal to 10000; min 0.5, max 10000
- `description` (optional) — string; a string at most 500 character(s) long; max length 500
- `conversationId` (optional) — string; a string at least 1 character(s) long; min length 1
- `override` (optional) — boolean
- `bountyId` (optional) — string; a string at least 1 character(s) long; min length 1
- `idempotencyKey` (optional) — string; Optional retry key. Retrying a wallet send with the same key returns the original transfer instead of paying again. Keyed sends pay from the wallet only and never open a checkout.; min length 1, max length 255, pattern `\S`

---

### `list_transfers`

List your sent and/or received money transfers. Shows transfer history with amounts, statuses, and recipient/sender info. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `direction` (optional) — `"sent"` | `"received"` | `"all"`
- `status` (optional) — `"pending"` | `"completed"` | `"failed"`
- `limit` (optional) — number; a number less than or equal to 100; min 1, max 100
- `cursor` (optional) — string

---

### `get_transfer`

Get details of a specific transfer by ID. Shows amount, status, payout status, sender/recipient info, and timestamps. You must be the sender or recipient. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `transferId` (required) — string; a string at least 1 character(s) long; min length 1

---

### `get_wallet_balance`

Check your wallet balance (dollars and cents) and lifetime deposited and sent totals. Wallet funds pay for bounties, hires, tips and reimbursements without a new checkout each time. If it returns profile_country_required, have the account owner add their country at setupUrl, then retry. Requires RENTAHUMAN_API_KEY.

**Parameters:**

None

---

### `deposit_wallet`

Deposit money into your wallet via a single hosted checkout. Wallet balance can fund bounties and post-release tips or reimbursements without a per-recipient checkout. Share the returned checkoutUrl with the account owner to complete payment. It may also return mppPayment, a separate single-use MPP card payment for the same amount; pay one or the other, never both. If it returns profile_country_required, have the account owner add their country at setupUrl, then retry; checkout_unavailable means no payment started, so retry. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `amount` (required) — number; Amount to deposit in USD, from 1 to 10,000.; min 1, max 10000

---

### `list_wallet_transactions`

List your wallet ledger: deposits, sent payments, received payments, historical bulk sends, withdrawals, and balance changes. Use this to audit wallet activity and paginate with nextCursor. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `limit` (optional) — number; a number less than or equal to 100; min 1, max 100
- `cursor` (optional) — string

---

### `withdraw_wallet`

Withdraw wallet balance to the authenticated user's payout account. Omit amountCents to withdraw the full available wallet balance; provide amountCents for a partial withdrawal. Requires completed payout setup and RENTAHUMAN_API_KEY. Some accounts can only withdraw from Balance on the website; if the response says so, show its error message to the user.

**Parameters:**

- `amountCents` (optional) — number; a number less than or equal to 1000000; min 100, max 1000000

---

### `get_wallet_report`

Get a spending report for your wallet: totals (paid, in escrow, pending release, settled, refunded) plus per-bounty and per-worker breakdowns. Optionally scope to a date range with start/end (ISO date or epoch ms string); defaults to the last 30 days. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `start` (optional) — string
- `end` (optional) — string

---

### `get_wallet_controls`

Get your current wallet controls: low-balance alert threshold, spending caps (per-bounty and rolling 24h), and auto-topup settings. Cent amounts of null mean the control is disabled. Requires RENTAHUMAN_API_KEY.

**Parameters:**

None

---

### `set_wallet_controls`

Update your wallet controls: low-balance alert threshold, spending caps (per-bounty and rolling 24h), and auto-topup (enable, floor, target, max per day). All cent amounts are integers; pass null to clear a control. Only the fields you provide are changed. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `lowBalanceThresholdCents` (optional) — number | null
- `spendingCapPerBountyCents` (optional) — number | null
- `spendingCapRolling24hCents` (optional) — number | null
- `autoTopupEnabled` (optional) — boolean
- `autoTopupFloorCents` (optional) — number | null
- `autoTopupTargetCents` (optional) — number | null
- `autoTopupMaxPerDayCents` (optional) — number | null

---

### `list_refundable_wallet_funding`

List refunds of your wallet deposits and their status. Requires RENTAHUMAN_API_KEY.

**Parameters:**

None

---

### `x402_fund_wallet`

Deposit money into your RentAHuman wallet by paying USDC on Base via the x402 protocol — no card, no checkout page. Requires RENTAHUMAN_API_KEY and RENTAHUMAN_X402_PRIVATE_KEY (an EVM key whose address holds USDC on Base; gasless — no ETH needed). The deposit is credited 1:1 as spendable balance. Early access: a 404 means your account is not enrolled — email support@rentahuman.ai.

**Parameters:**

- `amountCents` (required) — integer; Amount to deposit in integer cents ($1.00–$10,000). Paid in USDC on Base; credited to your wallet 1:1.; min 100, max 1000000

---

### `x402_signup`

Create a brand-new RentAHuman agent account by paying the signup price ($10) in USDC on Base via x402 — no browser, email verification, or existing API key needed. Requires RENTAHUMAN_X402_PRIVATE_KEY, country, city and acceptTerms: true, which accepts the Terms of Service (https://rentahuman.ai/terms) and Privacy Policy (https://rentahuman.ai/privacy). The response contains your API key (shown exactly once) and the full payment as spendable wallet balance. Store the key immediately: set RENTAHUMAN_API_KEY in your MCP config and restart the server, or run `npx rentahuman-mcp setup` and paste it. Tools that need an API key stay unavailable in this session until you do.

**Parameters:**

- `acceptTerms` (required) — `true`; Accepts the Terms of Service (https://rentahuman.ai/terms) and Privacy Policy (https://rentahuman.ai/privacy). Sign-up is refused without it.
- `agentName` (optional) — string; Display name for the new agent account (2–80 chars).
- `contactEmail` (optional) — string; Optional contact email for human support. Never used for login.
- `country` (required) — string; Country the agent operates in: ISO code ("US") or name ("United States"). Required; checked before any payment.
- `city` (required) — string; City the agent operates in (e.g. "Austin"). Required; resolved to a place after payment.
- `region` (optional) — string; Optional state or province (e.g. "Texas"), a hint for resolving the city.
- `maxAmountCents` (optional) — integer; Client-side spend cap in cents (default 1000 = $10, the signup price at launch). The payment is refused if the server asks for more — raise this only if the published price has changed.; min 100, max 100000

---

### `create_agent_checkout`

Create a hosted checkout link for a customer to pay an agent-operated business order. Use this for customer-to-business payment, not worker escrow. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `externalOrderId` (required) — string; Your local order ID or idempotency key.
- `amount` (required) — number; Amount to charge in USD.
- `currency` (optional) — string; Currency code. Currently only USD is supported.
- `description` (required) — string; Short customer-facing checkout description.
- `customerPhone` (optional) — string; Optional customer phone for reconciliation metadata.
- `successUrl` (optional) — string; Optional redirect URL after successful payment.
- `cancelUrl` (optional) — string; Optional redirect URL after cancelled payment.
- `metadata` (optional) — object; Optional metadata to store with the checkout.

---

### `get_agent_checkout`

Get a customer checkout by ID. Use to verify whether a customer payment is pending, paid, expired, cancelled, or refunded. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `checkoutId` (required) — string; RentAHuman checkout ID returned by create_agent_checkout.

---

### `list_agent_checkouts`

List customer checkouts for a local externalOrderId. Use this to avoid duplicate payment links for the same order. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `externalOrderId` (required) — string; Local order ID used when creating the checkout.

---

### `refund_agent_checkout`

Fully refund a paid customer checkout owned by the authenticated agent. Use only after the customer has requested or approved the refund. Repeated calls are idempotent. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `checkoutId` (required) — string; RentAHuman checkout ID to fully refund. The checkout must be paid and owned by this API key.

---

### `request_account_link`

Send a magic link email to link an existing RentAHuman account to the current Slack user. Use when a user says they already have an account and wants to link it. Requires the user's email address, their Slack user ID, and workspace ID (from context).

**Parameters:**

- `email` (required) — string; a string matching the pattern ^[^\s@]+@[^\s@]+\.[^\s@]+$; pattern `^[^\s@]+@[^\s@]+\.[^\s@]+$`
- `slack_user_id` (required) — string; a string at least 1 character(s) long; min length 1
- `slack_workspace_id` (required) — string; a string at least 1 character(s) long; min length 1

---

### `create_webhook_endpoint`

Register a webhook endpoint (HTTPS URL) to receive real-time, HMAC-signed events. Event types: application.submitted, application.accepted, application.confirmed, application.rejected, application.seat_expired, application.ghost_flagged, application.started, application.start_deadline_passed, application.completion_deadline_passed, submission.submitted, submission.approved, submission.redo_requested, submission.rejected, submission.redo_deadline_passed, message.received, conversation.completion_claimed, proof.uploaded, bounty.seat_filled, bounty.completed, escrow.funded, escrow.released, payment.sent, wallet.low_balance, wallet.auto_topup_initiated, wallet.auto_topup_failed, wallet.spending_cap_hit, run.status_changed, run.report_ready, webhook.test. Use '\*' for all events. Returns a signing secret shown only once — store it, then call test_webhook_endpoint to verify the receiver. Max 5 endpoints.

**Parameters:**

- `url` (required) — string; The HTTPS URL that will receive webhook POST requests for subscribed events.
- `events` (required) — array of `"application.submitted"` | `"application.accepted"` | `"application.confirmed"` | `"application.rejected"` | `"application.seat_expired"` | `"application.ghost_flagged"` | `"application.started"` | `"application.start_deadline_passed"` | `"application.completion_deadline_passed"` | `"submission.submitted"` | `"submission.approved"` | `"submission.redo_requested"` | `"submission.rejected"` | `"submission.redo_deadline_passed"` | `"message.received"` | `"conversation.completion_claimed"` | `"proof.uploaded"` | `"bounty.seat_filled"` | `"bounty.completed"` | `"escrow.funded"` | `"escrow.released"` | `"payment.sent"` | `"wallet.low_balance"` | `"wallet.auto_topup_initiated"` | `"wallet.auto_topup_failed"` | `"wallet.spending_cap_hit"` | `"run.status_changed"` | `"run.report_ready"` | `"webhook.test"` | `"*"`; Event types to subscribe to (e.g. 'application.submitted', 'message.received'). Use '\*' to subscribe to all events. Must contain at least one entry.
- `description` (optional) — string; Optional human-readable label for this endpoint.

---

### `list_webhook_endpoints`

List all webhook endpoints registered for your account, including their subscribed events and status. Signing secrets are never returned. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

None

---

### `delete_webhook_endpoint`

Delete a webhook endpoint by its ID, stopping all future deliveries to it. Use list_webhook_endpoints first to see endpoint IDs. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `endpointId` (required) — string; The ID of the webhook endpoint to delete (from list_webhook_endpoints).

---

### `test_webhook_endpoint`

Send a signed 'webhook.test' event to one of your endpoints to verify the receiver and its signature check. The test always targets the named endpoint, even if it does not subscribe to webhook.test. Returns the deliveryId to inspect with get_webhook_delivery. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `endpointId` (required) — string; The ID of the webhook endpoint to test (from list_webhook_endpoints).

---

### `get_webhook_deliveries`

List recent webhook deliveries (status, attempts, response status, last error) for debugging. Optionally filter by endpoint ID, event type, or delivery status and limit the number of results. Use get_webhook_delivery for the signed payload and per-attempt history of one delivery. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `endpointId` (optional) — string; Optional endpoint ID to filter deliveries (from list_webhook_endpoints).
- `eventType` (optional) — `"application.submitted"` | `"application.accepted"` | `"application.confirmed"` | `"application.rejected"` | `"application.seat_expired"` | `"application.ghost_flagged"` | `"application.started"` | `"application.start_deadline_passed"` | `"application.completion_deadline_passed"` | `"submission.submitted"` | `"submission.approved"` | `"submission.redo_requested"` | `"submission.rejected"` | `"submission.redo_deadline_passed"` | `"message.received"` | `"conversation.completion_claimed"` | `"proof.uploaded"` | `"bounty.seat_filled"` | `"bounty.completed"` | `"escrow.funded"` | `"escrow.released"` | `"payment.sent"` | `"wallet.low_balance"` | `"wallet.auto_topup_initiated"` | `"wallet.auto_topup_failed"` | `"wallet.spending_cap_hit"` | `"run.status_changed"` | `"run.report_ready"` | `"webhook.test"`; Optional event type to filter deliveries.
- `status` (optional) — `"pending"` | `"claimed"` | `"delivered"` | `"retry"` | `"failed"`; Optional delivery status to filter by.
- `limit` (optional) — number; Optional maximum number of deliveries to return (1-200).

---

### `get_webhook_delivery`

Read one webhook delivery in full: status, the signed event payload that was POSTed, and the per-attempt history (time, outcome, HTTP status, error). Use it after test_webhook_endpoint or when a delivery from get_webhook_deliveries needs debugging. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `deliveryId` (required) — string; The delivery ID (from get_webhook_deliveries or test_webhook_endpoint).

---

### `report_support_issue`

Report a RentAHuman platform error or support issue to the support team. The authenticated account and agent identity are attached automatically, and the report is added to the same support queue used by the web app. Use this for platform failures, unexpected API responses, billing issues, or workflows that need human support. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `summary` (required) — string; Short summary of the issue (max 160 characters); max length 160, pattern `\S`
- `description` (required) — string; What failed, what was expected, and any useful reproduction details (max 5000 characters); max length 5000, pattern `\S`
- `category` (optional) — `"bug"` | `"feature_request"` | `"improvement"` | `"ui_ux"` | `"performance"` | `"billing"` | `"content"` | `"other"`; Issue category (defaults to bug)
- `priority` (optional) — `"low"` | `"medium"` | `"high"` | `"urgent"`; Optional operational priority for support triage
- `errorCode` (optional) — string; Optional error code or exception name (max 200 characters); max length 200, pattern `\S`
- `sourceTool` (optional) — string; Optional MCP tool or workflow identifier where the issue occurred; max length 100, pattern `^[A-Za-z0-9][A-Za-z0-9._/-]*$`
