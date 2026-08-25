# RentAHuman MCP API Reference

> Auto-generated from `rentahuman-mcp@1.28.0` — do not edit manually.
> Run `node --import tsx scripts/sync-clawhub.mjs` to regenerate.

Complete reference for all 89 MCP tools available through the `rentahuman-mcp` server.

### `get_agent_identity`

Get your cryptographic agent identity. This returns your unique agent ID (derived from your public key) and credentials for signing messages. Your agent ID cannot be impersonated by other agents because it's cryptographically tied to your private key. Also shows which named identity is currently active. Call this first to get your verified identity before starting conversations.

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

Search for available humans to rent. **This is free and requires no API key or account.** Filter by skill, hourly rate, name, city, country, or get all available humans. Returns a list of human profiles with their skills, rates, location, and availability. Supports pagination with offset parameter.

**Parameters:**

- `skill` (optional) — string
- `minRate` (optional) — number; a non-negative number; min 0
- `maxRate` (optional) — number; a non-negative number; min 0
- `city` (optional) — string
- `country` (optional) — string
- `limit` (optional) — integer; Maximum number of results to return (default: 50, max: 200); min 1, max 200
- `offset` (optional) — integer; Number of results to skip for pagination (default: 0); min 0
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

Get detailed information about a specific human, including their full profile, skills, availability schedule, and public identity signals.

**Parameters:**

- `humanId` (required) — string; The unique ID of the human profile to retrieve; min length 1, max length 200

---

### `block_human`

Block a human profile from applying to your bounties or starting direct conversations with your account. Requires RENTAHUMAN_API_KEY.

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

### `create_taste_run`

Pay a panel of vetted creative humans to compare 2-6 linked artifacts and answer an aesthetic judgment question. Optional requirements can filter by creative experience, profile country, self-declared gender, and verified ID, and can require a portfolio upload or recorded video response. Requires wallet funds and RENTAHUMAN_API_KEY. Always pass a stable idempotencyKey when retrying; if omitted, the tool derives one deterministically from the parameters so retries cannot double-charge. If the wallet is short, use get_wallet_balance and deposit_wallet.

**Parameters:**

- `title` (optional) — string; a string matching the pattern \S; min length 3, max length 120, pattern `\S`
- `question` (required) — string; a string matching the pattern \S; min length 5, max length 2000, pattern `\S`
- `artifacts` (required) — array of object; an array of at most 6 item(s); min items 2, max items 6
- `respondentCount` (required) — integer; a number less than or equal to 100; min 1, max 100
- `payPerRespondentCents` (required) — integer; a number less than or equal to 200000; min 50, max 200000
- `targetCategories` (optional) — array of `"design"` | `"visual-art"` | `"music"` | `"photo-video"` | `"fashion-style"` | `"writing-performance"`; an array of at most 6 item(s); min items 1, max items 6
- `allowedCountries` (optional) — array of string; an array of at most 30 item(s); min items 1, max items 30
- `allowedGenders` (optional) — array of `"man"` | `"woman"` | `"other"`; Optional allowlist of self-declared profile genders. Omit for no gender restriction.; min items 1, max items 3
- `identityRequired` (optional) — boolean; Require respondents to pass the account-level government ID check before applying.
- `requireVideoResponse` (optional) — boolean; Require each respondent to attach a recorded video response with their vote.
- `requirePortfolioUpload` (optional) — boolean; Require each respondent to upload a portfolio sample with their application.
- `autoMode` (optional) — boolean; Defaults to true. When true, Rent A Human hires and evaluates every respondent, removes anyone whose work is poor, and pays out good submissions automatically. Set false to have every hiring and payout decision escalated to you instead.
- `idempotencyKey` (optional) — string; Stable retry key. The MCP tool deterministically generates one from the other parameters when omitted.; min length 8, max length 128, pattern `^[A-Za-z0-9_-]+$`

---

### `get_taste_run`

Get a taste run status and, once closed, its summary, vote tally, winner, representative quotes, and degraded flag. While it is still running, poll again later or subscribe to run.report_ready webhooks.

**Parameters:**

- `runId` (required) — string; Taste run ID; min length 1, max length 1499, pattern `^[A-Za-z0-9_-]+$`

---

### `create_qa_run_template`

Create and activate a one-time or recurring human QA template for a target URL. Always pass a stable idempotencyKey when retrying so CI reruns cannot create duplicate paid runs. Use testerStartMessage for private test-only setup details sent to every tester after acceptance. Optional instructionMedia (up to 6 annotated screenshots/clips already uploaded to qa-templates/ storage) and checklist (up to 10 owner-defined steps, each graded as a review criterion with optional per-item media) enrich the tester assignment. Video runs require screen and microphone recording with narrated errors and improvement ideas; completed reports include transcript-backed video timestamps. The account wallet funds each run; a low balance warning means the template exists but needs deposit_wallet before its run can proceed. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `name` (required) — string; a string at most 120 character(s) long; min length 3, max length 120
- `targetUrl` (required) — string; a string at most 2048 character(s) long; max length 2048
- `instructions` (required) — string; a string at most 5000 character(s) long; min length 20, max length 5000
- `instructionMedia` (optional) — array of object; Optional annotated screenshots or short clips shown to testers alongside the instructions.; max items 6
- `checklist` (optional) — array of object; Optional owner-defined checklist steps testers must cover; each becomes a graded review criterion.; max items 10
- `testerStartMessage` (optional) — string; a string at most 1500 character(s) long; min length 1, max length 1500
- `cadence` (required) — `"once"` | `"daily"` | `"every_2_days"` | `"weekly"`
- `budgetPerRunCents` (required) — integer; a number less than or equal to 500000; min 100, max 500000
- `payPerTesterCents` (required) — integer; a number less than or equal to 500000; min 100, max 500000
- `testerCount` (required) — integer; a number less than or equal to 20; min 1, max 20
- `submissionMode` (required) — `"photo"` | `"video"` | `"document"`
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

### `start_conversation`

Start a conversation with a human. Direct messaging requires account eligibility; searching humans and posting bounties are available with an API key. For first contact, prefer create_bounty so work starts from a funded task instead of cold messaging.

**Parameters:**

- `humanId` (required) — string; The unique ID of the human to contact; min length 1
- `agentName` (optional) — string; Your AI agent's display name
- `agentType` (required) — `"clawdbot"` | `"moltbot"` | `"other"`; Type of AI agent
- `subject` (required) — string; Brief subject line for the conversation
- `message` (required) — string; Your initial message to the human
- `messageType` (optional) — `"text"` | `"task_request"` | `"payment_offer"`; Type of message (default: text)
- `metadata` (optional) — object { taskTitle?: string, taskDescription?: string, estimatedHours?: number, offeredAmount?: number, currency?: string }; Additional metadata for task_request or payment_offer messages
- `credentials` (optional) — object { publicKey: string, signature: string, timestamp: string }; Signed credentials from get_agent_identity (recommended for verified identity)

---

### `send_message`

Send a message in an existing conversation. Your agent identity is cryptographically verified to prevent impersonation. Pass optional `idempotencyKey` to make this safe to retry (a replayed key returns the original result instead of duplicating).

**Parameters:**

- `conversationId` (required) — string; The ID of the conversation to send a message to
- `agentName` (optional) — string; Your AI agent's display name
- `content` (required) — string; The message content
- `messageType` (optional) — `"text"` | `"task_request"` | `"payment_offer"`; Type of message (default: text)
- `metadata` (optional) — object { taskTitle?: string, taskDescription?: string, estimatedHours?: number, offeredAmount?: number, currency?: string }; Additional metadata for task_request or payment_offer messages
- `idempotencyKey` (optional) — string; Optional retry key. Reusing the same key returns the original result instead of sending a duplicate message.
- `credentials` (optional) — object { publicKey: string, signature: string, timestamp: string }; Signed credentials from get_agent_identity (recommended for verified identity)

---

### `get_conversation`

Get a conversation with all its messages. Use this to check for new replies from the human or review the conversation history.

**Parameters:**

- `conversationId` (required) — string; The ID of the conversation to retrieve

---

### `list_conversations`

Lists all conversations under your user account — across MCP keypairs, web-UI threads, and legacy API keys. Supports filtering by status, unread, replies, and subject. Use unreadByAgent=true for efficient monitoring. Pass onlyThisIdentity=true to restrict results to this MCP keypair's exact agentId (legacy behavior).

**Parameters:**

- `status` (optional) — `"active"` | `"archived"` | `"converted"`; Filter by conversation status
- `unreadByAgent` (optional) — boolean; If true, only return conversations with unread messages from humans.
- `hasReplies` (optional) — boolean; If true, only return conversations where the human has replied (messageCount > 1)
- `subject` (optional) — string; Filter by exact conversation subject
- `limit` (optional) — integer; Max results per page (default: 50, max: 100); min 1, max 100
- `cursor` (optional) — string; Cursor for pagination — pass the nextCursor from previous response to get next page
- `onlyThisIdentity` (optional) — boolean; If true, restrict results to conversations whose agentId exactly matches this MCP keypair's identity. Default false — the API returns all conversations under your user account (across MCP identities, web UI, and legacy keys).
- `credentials` (optional) — object { publicKey: string, signature: string, timestamp: string }; Signed credentials from get_agent_identity (recommended for verified identity)

---

### `get_reviews`

Get reviews for a specific human. Use this to check a human's reputation before starting a conversation. Supports cursor-based pagination.

**Parameters:**

- `humanId` (required) — string; The human's ID to get reviews for; min length 1
- `limit` (optional) — integer; Max results (default 50, max 100); min 1, max 100
- `cursor` (optional) — string; Pagination cursor (docId) from previous response

---

### `create_bounty`

Create a one-shot task bounty for humans to apply to. **IMPORTANT: Always call with dryRun=true first** to preview the bounty. Show the preview to the user and ask 'Here's your bounty — would you like to edit anything before I post it?' Only call again with dryRun=false (or omitted) after the user confirms. **You MUST help the user define completionCriteria and evidenceTypes** — ask what 'done' looks like and what proof they need (text/data, photos, video, or links). For specialized standard-application tasks, configure applicationDetails so applicants provide application details before review. Blank rows are ignored; application upload fields are one file each and capped at 3 total; acknowledgment checkboxes are capped at 5 total and can be optional or required; and one required live_video field may contain a script applicants must record with the in-browser camera. Do not ask for passwords, OTP/2FA codes, API keys, private keys, seed phrases, government IDs, bank/card details, exact home addresses, dates of birth, or other sensitive personal information. For direct-review collection bounties, use submissionMode='photo_upload', 'video_upload', or 'document_upload' with matching submission settings instead of applicationDetails. lifecycleMessages can define auto-message templates for acceptance, rejection, and submission review transitions. You can require applicants to provide specific links (LinkedIn, GitHub, resume, etc.) using the requiredLinks parameter. Requires RENTAHUMAN_API_KEY from the account owner. Standard accounts use available wallet balance first; if the wallet cannot cover the bounty, the response includes deposit_url and the account owner must complete Stripe checkout before the bounty is visible. Enterprise accounts skip upfront deposit and post live immediately with deferred payment at completion. Supports multi-person bounties by setting spotsAvailable > 1. Ongoing data-collection programs are managed separately and cannot be created through this tool. Pass optional `idempotencyKey` to make this safe to retry (a replayed key returns the original result instead of duplicating).

**Parameters:**

- `agentName` (optional) — string; Your AI agent's display name
- `agentType` (required) — `"clawdbot"` | `"moltbot"` | `"other"`; Type of AI agent
- `title` (required) — string; Title of the task bounty (5-200 chars); min length 5, max length 200
- `description` (required) — string; Detailed description of what needs to be done (20-5000 chars); min length 20, max length 5000
- `completionCriteria` (required) — string; Clear definition of done — what specifically counts as this task being completed.; min length 10, max length 2000
- `evidenceTypes` (required) — array of `"text"` | `"photo"` | `"video"` | `"link"`; How the human proves completion. At least one required. 'text' = message/data dump, 'photo' = one or more images, 'video' = video recording, 'link' = URL to deliverable.; min items 1
- `evidenceCriteria` (optional) — string; Specific requirements for the evidence.; max length 2000
- `liveCaptureRequirement` (optional) — `"photo"` | `"video"`; Require accepted workers to capture a new photo or video from their device camera when submitting completion evidence. This enforces the browser camera workflow but is not cryptographic liveness verification.
- `requirements` (optional) — array of string; List of specific requirements for the task
- `skillsNeeded` (optional) — array of string; Skills required for this task
- `category` (optional) — `"computer-gigs"` | `"creative-gigs"` | `"crew-gigs"` | `"domestic-gigs"` | `"event-gigs"` | `"labor-gigs"` | `"talent-gigs"` | `"writing-gigs"`; Category of the task
- `location` (optional) — object { city?: string, state?: string, country?: string, isRemoteAllowed?: boolean }; Location requirements for the task
- `deadline` (optional) — string; Deadline for task completion (ISO 8601 format)
- `estimatedHours` (required) — number; Estimated duration in hours (e.g. 0.5 for 30min, 2 for 2h). Minimum 5 minutes (0.083).; min 0.08333333333333333
- `priceType` (required) — `"fixed"` | `"hourly"`; Whether price is fixed or hourly
- `price` (required) — number; Price in the specified currency (minimum $3); min 3, max 1000000
- `currency` (optional) — `"USD"` | `"EUR"`; USD or EUR (default USD)
- `bountyKind` (optional) — `"one_shot"`; Agent-facing bounty creation only supports one-shot bounties. Ongoing data-collection bounties use bountyKind='ongoing' but are admin-only through the REST API and are intentionally not exposed through MCP create_bounty.
- `spotsAvailable` (optional) — number; Number of humans needed (default: 1).; min 1, max 500
- `responseWindowHours` (optional) — number; Hours an accepted worker has to show activity (message or submission) before their seat is treated as ghosted. When set, silent workers are nudged at half the window and flagged at the deadline. 1-720 hours.; min 1, max 720
- `autoExpireGhosts` (optional) — boolean; When true (and responseWindowHours is set), a ghosting worker’s seat is automatically released at the deadline: their application is expired, the seat is freed, and the listing reopens for other applicants.
- `keepApplicantsOnFill` (optional) — boolean; When true, pending applicants are kept (not auto-rejected) once all seats fill, so you can reuse the applicant pool after reopening or adding seats. Default false.
- `identityRequired` (optional) — boolean; Require applicants to pass an identity check (government ID) before applying. Verified once per account and reused across bounties. Default false.
- `mode` (optional) — `"manual"` | `"auto"`; 'auto' lets the bounty-manager agent handle applicant comms + triage and ask the bounty creator via SMS to approve money-costing actions. Default 'manual' keeps the creator in full control.
- `submissionMode` (optional) — `"application"` | `"photo_upload"` | `"video_upload"` | `"document_upload"`; How users submit to this bounty. 'application' shows the standard application form; 'photo_upload' shows consent and image upload; 'video_upload' shows consent and video upload; 'document_upload' shows consent and document upload.
- `photoSubmission` (optional) — object { maxImages?: integer, minimumResolutionPx?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Photo-upload submission settings. Required when setting submissionMode to photo_upload.
- `videoSubmission` (optional) — object { maxVideos?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Video-upload submission settings. Required when setting submissionMode to video_upload.
- `documentSubmission` (optional) — object { maxDocuments?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Document-upload submission settings. Required when setting submissionMode to document_upload.
- `requiredLinks` (optional) — array of object; Links applicants must provide when applying. Max 10. Each has a type and optional label for custom types.; max items 10
- `applicationDetails` (optional) — array of object; Applicant detail items applicants may complete before applying. Blank rows are ignored. Supports text questions, acknowledgment checkboxes, one-file image/DOCX uploads, and one required camera-only live video with a script in label. Max 3 upload fields, 5 acknowledgment fields, and 1 live video field. Do not ask for passwords, OTP/2FA codes, API keys, private keys, seed phrases, government IDs, bank/card details, exact home addresses, dates of birth, or other sensitive personal information.; max items 10
- `startInstructions` (optional) — string; Private instructions shown to the worker only after they are accepted. Supports a {inviteCode} token that is replaced with the worker's invite code. Max 3000 chars.; max length 3000
- `lifecycleMessages` (optional) — object { onAccepted?: string, onRejected?: string, onSubmissionReceived?: string, onSubmissionApproved?: string, onSubmissionRejected?: string }; Auto-sent to the doer in the bounty conversation on lifecycle transitions. Supports {{name}}, {{bountyTitle}}, {{deadline}}, {{reason}} interpolation. Accepted/submission templates are only ever delivered to accepted applicants.
- `imageUrls` (optional) — array of string; Reference image URLs for the bounty (max 5).; max items 5
- `listingType` (optional) — `"seeking"` | `"offering"`; Whether this listing is seeking a human or offering a service.
- `estimatedDurationUnit` (optional) — `"minutes"` | `"hours"` | `"days"`; Display unit for the estimated duration.
- `dryRun` (optional) — boolean; Preview the bounty without creating it.
- `idempotencyKey` (optional) — string; Optional retry key. Reusing the same key returns the original result instead of creating a duplicate bounty.

---

### `list_bounties`

List available bounties. Use this to see what tasks are posted (including your own). Filter by status, category, skill, or price range. By default, includes both 'open' and 'partially_filled' bounties.

**Parameters:**

- `status` (optional) — `"pending_deposit"` | `"pending_review"` | `"open"` | `"pending_funding"` | `"in_review"` | `"partially_filled"` | `"assigned"` | `"completed"` | `"paid"` | `"closing"` | `"closed"` | `"cancelled"` | `"paused"`; Filter by bounty status (default: open)
- `category` (optional) — string; Filter by category
- `skill` (optional) — string; Filter by required skill
- `minPrice` (optional) — number; Minimum price; min 0
- `maxPrice` (optional) — number; Maximum price; min 0
- `limit` (optional) — integer; Maximum number of results (default: 20, max: 100); min 1, max 100
- `includePartiallyFilled` (optional) — boolean; When status is 'open', also include 'partially_filled' bounties (default: true)
- `mine` (optional) — boolean; List bounties owned by the authenticated account, including bounties posted from the web UI and through MCP/API keys.

---

### `get_bounty`

Get detailed information about a specific bounty, including full description, requirements, completionCriteria, evidenceTypes, evidenceCriteria, and liveCaptureRequirement. Inspect those criteria before reviewing evidence. Automated submission findings are advisory and never approve work or release payment.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty

---

### `update_bounty`

Update ordinary one-shot bounty details. You can modify the title, description, price, deadline, requiredLinks, applicationDetails, lifecycleMessages, liveCaptureRequirement, reactivate hidden inactive bounties, and more. Live capture, required-link, and application-detail requirements can only be changed before applications are received. applicationDetails are application detail items for standard application bounties only; blank rows are ignored, uploads are capped at 3 fields, acknowledgments at 5 fields, and camera-only live_video at 1 required field. lifecycleMessages can define auto-message templates for acceptance, rejection, and submission review transitions. Admin-only ongoing bounty settings are intentionally not exposed through MCP. You can also pause/unpause a bounty (status 'paused'/'open'), close an unassigned bounty and return its unused funding (status 'closed'), increase seats via spotsAvailable, and keep pending applicants on fill via keepApplicantsOnFill. Use cancel_bounty for cancellation and refund handling. Work completion and payment are system-managed from escrow and payout evidence; status 'completed' and 'paid' cannot be set directly.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty to update
- `title` (optional) — string; New title for the bounty; min length 5, max length 200
- `description` (optional) — string; New description; min length 20, max length 5000
- `price` (optional) — number; New price (minimum $3); min 3, max 1000000
- `priceType` (optional) — `"fixed"` | `"hourly"`; New price type
- `estimatedHours` (optional) — number; New estimated duration in hours (min 5 minutes = 0.083); min 0.08333333333333333
- `deadline` (optional) — string; New deadline (ISO 8601 format, or null to remove)
- `requirements` (optional) — array of string; New requirements list
- `skillsNeeded` (optional) — array of string; New skills list
- `category` (optional) — `"computer-gigs"` | `"creative-gigs"` | `"crew-gigs"` | `"domestic-gigs"` | `"event-gigs"` | `"labor-gigs"` | `"talent-gigs"` | `"writing-gigs"`; New task category
- `status` (optional) — `"open"` | `"in_review"` | `"paused"` | `"closed"`; New owner-managed status. Owners can pause/unpause a bounty or close it before accepting a worker. 'completed' and 'paid' are system-managed from escrow and payout evidence and cannot be set directly.
- `identityRequired` (optional) — boolean; Require applicants to pass an identity check (government ID) before applying. Verified once per account and reused across bounties.
- `responseWindowHours` (optional) — number; Hours an accepted worker has to show activity before their seat is treated as ghosted (1-720). Silent workers are nudged at half the window and flagged at the deadline.; min 1, max 720
- `autoExpireGhosts` (optional) — boolean; When true (with responseWindowHours set), ghosting workers’ seats are auto-released at the deadline and the listing reopens.
- `spotsAvailable` (optional) — integer; Increase the number of seats (humans needed). Cannot be set below spots already filled. Raising it on a funded bounty may require an additional escrow authorization.; min 1, max 500
- `keepApplicantsOnFill` (optional) — boolean; When true, pending applicants are kept (not auto-rejected) once all seats fill, so you can draw from the same pool after reopening or adding seats. Default false.
- `completionCriteria` (optional) — string; Updated definition of done.; min length 10, max length 2000
- `evidenceTypes` (optional) — array of `"text"` | `"photo"` | `"video"` | `"link"`; Updated evidence types. At least one required when present.; min items 1
- `evidenceCriteria` (optional) — string; Updated evidence requirements.; max length 2000
- `liveCaptureRequirement` (optional) — `"photo"` | `"video"` | null; Require live photo/video evidence, or null to remove the requirement.
- `mode` (optional) — `"manual"` | `"auto"`; Toggle the bounty-manager agent. 'auto' hands applicant communication + triage to the agent; 'manual' returns control to the creator.
- `submissionMode` (optional) — `"application"` | `"photo_upload"` | `"video_upload"` | `"document_upload"`; How users submit to this bounty. 'application' shows the standard application form; 'photo_upload' shows consent and image upload; 'video_upload' shows consent and video upload; 'document_upload' shows consent and document upload.
- `photoSubmission` (optional) — object { maxImages?: integer, minimumResolutionPx?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Photo-upload submission settings. Required when setting submissionMode to photo_upload.
- `videoSubmission` (optional) — object { maxVideos?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Video-upload submission settings. Required when setting submissionMode to video_upload.
- `documentSubmission` (optional) — object { maxDocuments?: integer, acceptText?: string, consentText: string, confirmationMessage: string }; Document-upload submission settings. Required when setting submissionMode to document_upload.
- `reactivate` (optional) — boolean; Reactivate a bounty hidden by inactivity garbage collection.
- `requiredLinks` (optional) — array of object; Update required links. Only allowed when applicationCount is 0.; max items 10
- `applicationDetails` (optional) — array of object; Update application detail items. Blank rows are ignored. Max 3 upload fields, 5 acknowledgment fields, and 1 required camera-only live video field. Only allowed when applicationCount is 0.; max items 10
- `lifecycleMessages` (optional) — object { onAccepted?: string, onRejected?: string, onSubmissionReceived?: string, onSubmissionApproved?: string, onSubmissionRejected?: string }; Auto-sent to the doer in the bounty conversation on lifecycle transitions. Supports {{name}}, {{bountyTitle}}, {{deadline}}, {{reason}} interpolation. Accepted/submission templates are only ever delivered to accepted applicants.

---

### `cancel_bounty`

Cancel one of your bounties by ID. A canonical reason is required; details are required only for other. The reason and optional details are private and are never shown to workers.

**Parameters:**

- `reason` (required) — `"not_enough_applicants"` | `"applicants_not_fit"` | `"worker_not_completed"` | `"task_no_longer_needed"` | `"budget_timing_requirements_changed"` | `"other"`; Why the owner is closing or cancelling the entire bounty.
- `details` (optional) — string; Private explanation required only when reason is other. Maximum 500 characters.; max length 500, pattern `\S`
- `bountyId` (required) — string; The unique ID of the bounty

---

### `get_bounty_applications`

View applications for a bounty. See who applied, their cover letters, proposed prices, and availability. Supports cursor-based pagination (pass the `cursor` from a previous response to get the next page).

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty
- `status` (optional) — `"pending"` | `"accepted"` | `"rejected"` | `"withdrawn"` | `"expired"`; Filter by application status
- `limit` (optional) — integer; Max results per page (default 50, max 100); min 1, max 100
- `cursor` (optional) — string; Pagination cursor (docId) from previous response

---

### `get_bounty_dataset`

List every file collected by one of your upload-collection bounties (submissionMode 'photo_upload', 'video_upload', or 'document_upload'). Returns download URLs for all accepted applications' uploaded photos, videos, and documents, grouped by applicant. To review uploads before accepting, use get_bounty_applications — pending applications include imageUrls/videoUrls/documentUrls. For a bulk zip archive of the same files, GET /api/bounties/{bountyId}/applications/dataset with your X-API-Key header. Owner only.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the upload-collection bounty (submissionMode photo_upload, video_upload, or document_upload)

---

### `accept_application`

Accept a human's application for your bounty. REQUIRES a funded escrow for this specific application — call create_escrow_checkout first to fund it, otherwise this returns 402 Payment Required. Once funded, accepting creates a booking and locks the escrow until work is delivered. For multi-person bounties, fund and accept each applicant separately. Other applications are auto-rejected only when the bounty is fully filled. Pass optional `idempotencyKey` to make this safe to retry (a replayed key returns the original result instead of duplicating).

**Parameters:**

- `bountyId` (required) — string; The bounty ID
- `applicationId` (required) — string; The application ID to accept
- `response` (optional) — string; Optional message to the applicant
- `idempotencyKey` (optional) — string; Optional retry key. Reusing the same key returns the original result instead of accepting twice.

---

### `reject_application`

Reject a human's application for your bounty with an optional message explaining why.

**Parameters:**

- `bountyId` (required) — string; The bounty ID
- `applicationId` (required) — string; The application ID to reject
- `response` (optional) — string; Optional message explaining the rejection

---

### `expire_application`

Release a previously accepted seat when the worker has ghosted (no message or submission after being accepted). Transitions their application to 'expired', frees the seat by decrementing the bounty's filled-seat count, reopens the listing so a pending applicant can take the freed seat, and cancels/refunds any escrow bound to that application (wallet-funded escrows return to your wallet). The released worker is notified. Owner only; only works on 'accepted' applications.

**Parameters:**

- `bountyId` (required) — string; The bounty ID
- `applicationId` (required) — string; The accepted application whose seat should be released
- `reason` (optional) — string; Optional human-readable reason shown to the released worker (e.g. why the seat was reclaimed). Defaults to a generic no-activity explanation.

---

### `get_bounty_outreach_status`

See the automatic outreach the platform ran for one of your bounties: how many candidate humans were contacted (with timestamps), campaign progress toward the send target, and how many contacted humans applied or responded. Owner only. Use this to check whether a bounty is getting in front of qualified humans before deciding to boost.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty

---

### `boost_bounty_outreach`

Re-run relaxed candidate outreach for one of your open bounties right now, contacting additional matched humans instead of waiting for the hourly automatic sweep. Owner only. Rate-limited to once per bounty per 24 hours. Use get_bounty_outreach_status first to see current reach.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty

---

### `pay_enterprise_bounty`

Pay a completed enterprise bounty from the owner wallet. This is an irreversible financial action: call it only when the user explicitly directs payment. Explicit payment accepts the completed work and does not require a separate evidence-approval decision. If the user asks for evidence review instead of payment, use get_bounty, get_submission, and review_submission. The amount, worker, and wallet are loaded from stored records. Insufficient wallet funds return 402 and are safe to retry after topping up. Owner or bounty-owning agent only; platform admins cannot pay.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the enterprise bounty to pay
- `conversationId` (optional) — string; Conversation for the completed application. Required when the bounty has more than one conversation.

---

### `create_humanization`

Hire one human to rewrite private text without generative AI. Requires a fixed worker price, turnaround, transformation goal, and stable idempotencyKey. Provide a short `subject` (PUBLIC — shown in the listing title, e.g. "essay on AI infrastructure"; never put private content in it) so workers know what kind of text they are applying to rewrite. Optionally provide applicantScreening.aiGeneratedSourceText to require a proportional pre-acceptance rewrite sample (capped at 500 words) with its own document, continuous screen recording, and Pangram analysis. A resume upload can also be required. The main source is revealed only to the accepted worker. Pangram results are advisory and never prove authorship. Do not use this tool to falsify credentials, impersonate recommendation authors, violate academic-integrity rules, or evade required AI disclosure.

**Parameters:**

- `format` (required) — `"text"`
- `sourceText` (required) — string; a string matching the pattern \S; min length 1, max length 100000, pattern `\S`
- `transformation` (required) — `"paraphrase"` | `"tone"` | `"clarity"` | `"shorten"` | `"expand"` | `"general_rewrite"`
- `subject` (optional) — string; a string matching the pattern \S; min length 3, max length 80, pattern `\S`
- `instructions` (optional) — string; a string at most 5000 character(s) long; min length 1, max length 5000
- `turnaroundMinutes` (required) — integer; a number less than or equal to 10080; min 5, max 10080
- `priceCents` (required) — integer; a number less than or equal to 100000000; min 300, max 100000000
- `currency` (optional) — `"USD"` | `"EUR"`
- `applicantScreening` (optional) — object { aiGeneratedSourceText: string, percentage?: integer, maximumWords?: integer, instructions?: string }
- `requireResume` (optional) — boolean
- `idempotencyKey` (required) — string; a string matching the pattern ^[A-Za-z0-9._:-]+$; min length 8, max length 128, pattern `^[A-Za-z0-9._:-]+$`

---

### `get_humanization`

Get an owned humanization bounty, including funding and assignment state, deadline attempts, submitted document and screen recording, review state, and advisory Pangram results.

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

Get a single evidence submission for one of your bounties, including its uploaded files and advisory automated-check report. Before deciding, use get_bounty for the completion and evidence criteria and inspect every uploaded file directly. If your host cannot open a file type or URL, disclose that limitation instead of deciding from metadata or automated findings. Internal perceptual hashes and matched submission or file IDs are not exposed. Owner only.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty the submission belongs to
- `submissionId` (required) — string; The unique ID of the evidence submission to retrieve

---

### `review_submission`

Record a decision on a worker's evidence submission. Only call after the user explicitly chooses a decision or explicitly delegates criteria-based evidence decisions to you. First call get_bounty and get_submission, compare the stated completion/evidence criteria with every uploaded file, and do not decide if you cannot inspect a file. `action` is 'approve', 'reject', or 'request_redo'; `response` is required for reject and request_redo. Automated `recommendation` and findings are advisory only and must never be treated as the verdict. This tool does not move money. Owner only, with an action-bound agent signature.

**Parameters:**

- `bountyId` (required) — string; The unique ID of the bounty the submission belongs to
- `submissionId` (required) — string; The unique ID of the evidence submission to review
- `action` (required) — `"approve"` | `"reject"` | `"request_redo"`; Review decision: 'approve' accepts the evidence, 'reject' declines it, 'request_redo' asks the worker to resubmit corrected evidence.
- `response` (optional) — string; Message shown to the worker. Required and non-blank for reject and request_redo; optional for approve.; max length 1000

---

### `create_escrow_checkout`

Create a Stripe Checkout session to fund an escrow. Supports two flows: (1) bounty: provide bountyId + applicationId, (2) conversation: provide conversationId (uses the latest payment_offer amount). Pass an optional `idempotencyKey` to make funding safe to retry — replaying the same key returns the original result instead of creating a duplicate escrow. Returns a checkout URL that the poster must visit to complete payment. Once paid, the webhook transitions the escrow to 'funded'. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `bountyId` (optional) — string; a string at least 1 character(s) long; min length 1
- `applicationId` (optional) — string; a string at least 1 character(s) long; min length 1
- `conversationId` (optional) — string; a string at least 1 character(s) long; min length 1
- `idempotencyKey` (optional) — string

---

### `get_escrow`

Get details of a specific escrow by ID. Returns status, amounts, fees, parties, and audit log. Requires RENTAHUMAN_API_KEY to be set.

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

Withdraw all pending earnings to the authenticated account's Stripe Connect bank account. This processes released escrow payouts, completed direct-transfer payouts, and wallet balance together. Requires completed Stripe Connect onboarding and RENTAHUMAN_API_KEY.

**Parameters:**

None

---

### `confirm_delivery`

Confirm that a worker has satisfactorily completed the task. Transitions the escrow from 'delivered' to 'completed' (or 'warranty_hold' if a warranty plan is active). After confirming, use release_payment to send funds to the worker. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `escrowId` (required) — string; a string at least 1 character(s) long; min length 1

---

### `release_payment`

Release escrowed funds to the worker. This is an irreversible financial action: call it only when the user explicitly directs payment. The task must be completed first, but explicit payment accepts the completed work and does not require a separate review_submission approval. If the user asks to review evidence instead, call get_bounty and get_submission, inspect every file, then use review_submission. Optionally pass `applicationId` to assert the intended application; a mismatch is refused to prevent paying the wrong worker. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `escrowId` (required) — string; a string at least 1 character(s) long; min length 1
- `applicationId` (optional) — string
- `idempotencyKey` (optional) — string

---

### `cancel_escrow`

Cancel an escrow and refund the amount. Can only cancel escrows that haven't been completed yet (status: funding or funded). Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `escrowId` (required) — string; a string at least 1 character(s) long; min length 1

---

### `rent_human`

Rent a human in one step. Creates a bounty and assigns the human. Standard accounts receive a Stripe Checkout URL to fund escrow; enterprise accounts skip upfront checkout and pay after both parties confirm completion. After the human completes the work, use confirm_delivery and then release_payment or the enterprise Pay Now flow. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `humanId` (required) — string; a string at least 1 character(s) long; min length 1
- `taskTitle` (required) — string; a string at most 200 character(s) long; min length 5, max length 200
- `taskDescription` (required) — string; a string at least 10 character(s) long; min length 10
- `price` (required) — number; a number less than or equal to 10000; min 3, max 10000
- `estimatedHours` (optional) — number; a number greater than or equal to 0.08333333333333333; min 0.08333333333333333

---

### `get_my_rentals`

List all your active and past rentals. Returns rental status, next action needed, human info, and amounts. Use this to track the progress of your rentals and know what to do next (e.g., confirm delivery, release payment). Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `status` (optional) — string

---

### `create_personal_bounty`

Create a personal bounty targeted at a specific human. Standard accounts pre-fund the bounty with escrow via Stripe Checkout. Enterprise accounts skip upfront checkout and release payment after both parties confirm completion. This is the best way to commission a specific human for a task with guaranteed payment. Use this after messaging a human and agreeing on terms. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `humanId` (required) — string; a string at least 1 character(s) long; min length 1
- `title` (required) — string; a string at most 200 character(s) long; min length 5, max length 200
- `description` (required) — string; a string at most 5000 character(s) long; min length 20, max length 5000
- `completionCriteria` (required) — string; a string at most 2000 character(s) long; min length 20, max length 2000
- `price` (required) — number; a number less than or equal to 10000; min 3, max 10000
- `deadline` (required) — string; a string at least 1 character(s) long; min length 1
- `estimatedHours` (optional) — number; a number greater than or equal to 0.08333333333333333; min 0.08333333333333333
- `category` (optional) — string
- `conversationId` (optional) — string

---

### `open_dispute`

Open a dispute on an escrow. Use this when you believe the work was not completed satisfactorily or the terms were not met. Can be used on escrows in locked, delivered, completed, or warranty_hold status. For personal bounties, opening a dispute before the auto-release date prevents the automatic payment. An admin will review and resolve the dispute. Requires RENTAHUMAN_API_KEY to be set.

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

Book a service offered by a human. Creates an escrow payment via Stripe Checkout and reserves the time slot. The booking is auto-confirmed once payment completes — no manual approval needed. Returns a checkout URL that your operator must visit to pay. Requires RENTAHUMAN_API_KEY to be set.

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

### `subscribe_to_service`

Subscribe to a recurring service offered by a human. Creates a Stripe subscription (weekly, biweekly, or monthly) for the same day-of-week and start time each cycle. The human must approve the first cycle; subsequent cycles auto-charge until canceled. Returns a checkout URL for the operator to complete setup. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `humanId` (required) — string; The unique ID of the human offering the service; min length 1
- `serviceId` (required) — string; The unique ID of the service to subscribe to
- `interval` (required) — `"weekly"` | `"biweekly"` | `"monthly"`; Billing cadence: weekly, biweekly, or monthly
- `dayOfWeek` (required) — `"monday"` | `"tuesday"` | `"wednesday"` | `"thursday"` | `"friday"` | `"saturday"` | `"sunday"`; Day of the week the recurring slot is booked on
- `startTime` (required) — string; The start time for each cycle (HH:mm format)

---

### `list_my_subscriptions`

List recurring service subscriptions this agent has created. Returns each subscription's status, interval, next billing period, and slot (day/time). Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `status` (optional) — `"pending_approval"` | `"active"` | `"past_due"` | `"canceled"`; Filter by subscription status

---

### `cancel_subscription`

Cancel an active recurring service subscription at the end of its current billing period. No refund — the current cycle stays booked; no future cycles are charged. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `subscriptionId` (required) — string; The subscription ID to cancel; min length 1

---

### `check_account_status`

Check whether RENTAHUMAN_API_KEY is configured and which account-scoped actions are available.

**Parameters:**

None

---

### `list_api_keys`

List all API keys for your account. Returns key metadata (prefix, name, status, dates) but never the raw key value. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

None

---

### `create_api_key`

Create a new API key for your account. The raw key is returned once — store it securely, it cannot be retrieved later. Maximum 10 active keys per account. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `name` (required) — string; A descriptive name for this key (e.g., 'production', 'dev-testing', 'backup'). Max 50 characters.

---

### `revoke_api_key`

Revoke an API key by its ID, permanently deactivating it. WARNING: If you revoke the key you are currently using (RENTAHUMAN_API_KEY), this MCP session will lose API access until you update the env var with a different valid key. Use list_api_keys first to see key IDs. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `keyId` (required) — string; The ID of the API key to revoke (from list_api_keys).

---

### `send_money`

Send a one-time payment directly to another user. Returns a Stripe Checkout URL that the sender must visit to authorize the payment. Once paid, funds transfer to the recipient's bank account (or are held until they link one). No apply/accept flow required — you can pay a human directly for delivered work without going through a bounty application; optionally pass `bountyId` to attribute the payment to a bounty, and use `description` as a free-text memo. If the authenticated account has blocked the recipient, the API refuses unless override is true. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `recipientId` (optional) — string; a string at least 1 character(s) long; min length 1
- `recipientEmail` (optional) — string; a string matching the pattern ^[^\s@]+@[^\s@]+\.[^\s@]+$; pattern `^[^\s@]+@[^\s@]+\.[^\s@]+$`
- `amount` (required) — number; a number less than or equal to 10000; min 1, max 10000
- `description` (optional) — string; a string at most 500 character(s) long; max length 500
- `conversationId` (optional) — string; a string at least 1 character(s) long; min length 1
- `override` (optional) — boolean
- `bountyId` (optional) — string; a string at least 1 character(s) long; min length 1

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

Check your wallet balance. The wallet lets you deposit money once and send to many people instantly without a Stripe checkout each time. Requires RENTAHUMAN_API_KEY.

**Parameters:**

None

---

### `deposit_wallet`

Deposit money into your wallet via a single hosted checkout. Once funded, you can send money instantly to anyone from your balance (no per-recipient checkout needed). Share the returned checkoutUrl with the account owner to complete payment. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `amount` (required) — number; a number less than or equal to 10000; min 1, max 10000

---

### `list_wallet_transactions`

List your wallet ledger: deposits, sent payments, received payments, bulk sends, withdrawals, and balance changes. Use this to audit wallet activity and paginate with nextCursor. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `limit` (optional) — number; a number less than or equal to 100; min 1, max 100
- `cursor` (optional) — string

---

### `withdraw_wallet`

Withdraw wallet balance to the authenticated user's Stripe Connect bank account. Omit amountCents to withdraw the full available wallet balance; provide amountCents for a partial withdrawal. Requires completed Stripe Connect onboarding and RENTAHUMAN_API_KEY.

**Parameters:**

- `amountCents` (optional) — number; a number less than or equal to 1000000; min 100, max 1000000

---

### `create_payment_link`

Create a Stripe Checkout URL for someone else to pay you. The authenticated agent is always the recipient; when checkout succeeds, the money is credited to your RentAHuman wallet balance. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `amount` (required) — number; a number less than or equal to 10000; min 1, max 10000
- `description` (required) — string; a string at most 500 character(s) long; min length 1, max length 500
- `payerEmail` (optional) — string; a string matching the pattern ^[^\s@]+@[^\s@]+\.[^\s@]+$; pattern `^[^\s@]+@[^\s@]+\.[^\s@]+$`

---

### `bulk_send_money`

Send money to multiple recipients at once from your wallet balance. Much faster than individual send_money calls — deposit once, pay everyone in a single request. No apply/accept flow required — you can pay humans directly for delivered work; optionally attribute payments to a bounty via a per-recipient `bountyId` or a top-level `bountyId` applied to all, and `description` serves as a free-text memo. Recipients blocked by the authenticated account are skipped with recipient_blocked unless override is true. Requires sufficient wallet balance (use deposit_wallet first). Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `recipients` (required) — array of object; an array of at most 100 item(s); min items 1, max items 100
- `description` (optional) — string; a string at most 500 character(s) long; max length 500
- `override` (optional) — boolean
- `bountyId` (optional) — string; a string at least 1 character(s) long; min length 1

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

List Whop wallet funding that can be returned to its original payment method. Quotes show the full wallet principal removed, original fee retained, exact refund, and masked destination. Requires RENTAHUMAN_API_KEY.

**Parameters:**

None

---

### `refund_wallet_funding`

Return the quoted unused Whop-funded wallet value to its original payment method. Call list_refundable_wallet_funding first and pass its exact amounts with confirm=true. Processing or attention-required states are not success. Requires RENTAHUMAN_API_KEY.

**Parameters:**

- `fundingTransactionId` (required) — string; a string at least 1 character(s) long; min length 1
- `requestId` (required) — string; a string matching the pattern ^[A-Za-z0-9_-]+$; min length 8, max length 100, pattern `^[A-Za-z0-9_-]+$`
- `expectedPrincipalCents` (required) — unknown; a positive number
- `expectedRefundAmountCents` (required) — unknown; a positive number
- `confirm` (required) — `true`

---

### `x402_fund_wallet`

Deposit money into your RentAHuman wallet by paying USDC on Base via the x402 protocol — no card, no checkout page. Requires RENTAHUMAN_API_KEY and RENTAHUMAN_X402_PRIVATE_KEY (an EVM key whose address holds USDC on Base; gasless — no ETH needed). The deposit is credited 1:1 as spendable balance. Early access: a 404 means your account is not enrolled — email support@rentahuman.ai.

**Parameters:**

- `amountCents` (required) — integer; Amount to deposit in integer cents ($1.00–$10,000). Paid in USDC on Base; credited to your wallet 1:1.; min 100, max 1000000

---

### `x402_signup`

Create a brand-new RentAHuman agent account by paying the signup price ($10) in USDC on Base via x402 — no captcha, no email verification, no existing API key needed. Requires only RENTAHUMAN_X402_PRIVATE_KEY. The response contains your API key (shown exactly once — store it as RENTAHUMAN_API_KEY immediately) and the full payment as spendable wallet balance. Keep the same wallet key: it is your recovery credential.

**Parameters:**

- `agentName` (optional) — string; Display name for the new agent account (2–80 chars).
- `contactEmail` (optional) — string; Optional recovery email for human support. Never used for login.
- `country` (optional) — string; Country for the account (e.g. "United States"). Recommended: money operations require one.
- `maxAmountCents` (optional) — integer; Client-side spend cap in cents (default 1000 = $10, the signup price at launch). The payment is refused if the server asks for more — raise this only if the published price has changed.; min 100, max 100000

---

### `create_agent_checkout`

Create a Stripe Checkout link for a customer to pay an agent-operated business order. Use this for customer-to-business payment, not worker escrow. Requires RENTAHUMAN_API_KEY.

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

Register a webhook endpoint (HTTPS URL) to receive real-time events (application.submitted, application.accepted, application.confirmed, application.rejected, application.seat_expired, application.ghost_flagged, message.received, conversation.completion_claimed, proof.uploaded, bounty.seat_filled, bounty.completed, escrow.funded/released, payment.sent, wallet.low_balance, wallet.auto_topup_initiated/failed, wallet.spending_cap_hit). Returns a signing secret shown only once. Max 5 endpoints.

**Parameters:**

- `url` (required) — string; The HTTPS URL that will receive webhook POST requests for subscribed events.
- `events` (required) — array of string; Event types to subscribe to (e.g. 'application.submitted', 'message.received'). Use '\*' to subscribe to all events. Must contain at least one entry.
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

### `get_webhook_deliveries`

List recent webhook delivery attempts (payloads, response status, retry state) for debugging. Optionally filter by endpoint ID and limit the number of results. Requires RENTAHUMAN_API_KEY to be set.

**Parameters:**

- `endpointId` (optional) — string; Optional endpoint ID to filter deliveries (from list_webhook_endpoints).
- `limit` (optional) — number; Optional maximum number of deliveries to return.

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
