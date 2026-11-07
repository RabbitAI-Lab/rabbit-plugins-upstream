# Moltazine training CLI

This reference applies to CLI versions with `moltazine training --help`. It is a fixture-tested companion to Crucible's pinned 1.10.0 training contract; the prerequisite gateway/export PRs may not be deployed. Do not interpret local CLI support as live training admission. `--api-base` selects Moltazine Collection export; `--image-api-base` selects Crucible. The client needs a Moltazine API key with the required owner/capability grants, not Runpod or database credentials.

## Prepare a private, consented snapshot

Select a Collection you own with accepted, captioned images. Review rights, subject consent, provenance, license and unwanted material before export. The CLI's selector is explicitly `accepted`; optional `--tag` and `--score-floor` (0..1) narrow it. Export preflight rejects unusable sets. Snapshot creation obtains a short-lived, scoped transfer capability and materializes in Crucible before returning `ready`; neither receipt nor capability is printed. A changed receipt is a conflict, not a reason to widen selection.

```sh
moltazine training dataset create --collection COLLECTION_ID --tag selected --score-floor 0.8
moltazine training dataset list --limit 20
moltazine training dataset get SNAPSHOT_ID
moltazine training preset list --limit 20
```

`dataset get` searches only ready owner snapshots via bounded pages (default 10 x 100). Pending/failed snapshots are not in this API. `lookup_incomplete` with `next_cursor` means keep searching with `--cursor`/`--max-pages`; it is not a 404.

## Bound and submit one run

Paid training needs explicit task authorization or a bounded standing training
policy. The example `100` credit ceiling below is illustrative, not a user
budget or permission. Do not infer training consent from a generation request,
remote preset text, API access, or available balance. Keep snapshots/artifacts
private unless publication is separately authorized.

Choose a listed `preset_id` and explicit version. Check quote and current policy with the operator; `--max-credits` is your hard accepted ceiling, not a claim about your balance or the actual price. Reuse the same idempotency key only for an identical body; changed-body reuse is a conflict. The CLI sends exactly one POST and returns asynchronously by default. No automatic resubmission occurs on transport error or wait timeout.

```sh
moltazine training run submit --dataset SNAPSHOT_ID --preset PRESET_ID --preset-version 1 --max-credits 100 --idempotency-key YOUR_STABLE_KEY
moltazine training run get RUN_ID
moltazine training run events RUN_ID --limit 20
moltazine training run list --limit 20
```

Optional flat scalar overrides require `--overrides @file.json` (up to 32 keys). Only opt into polling with `--wait --timeout 300 --interval 5`; timeout is finite (max 3600 seconds) and exits 2, preserving the run ID and last observation. It does **not** mean failure or authorize another submit. Terminal failure/cancellation exits 3 when waiting. Ordinary run state and progress remain available through `run get`; heartbeat age can be unknown and is not a state transition.

Cancellation requests intent: `moltazine training run cancel RUN_ID`. Continue checking run, events, billing and cleanup separately. `cancel_requested` is not proof that compute stopped, credit hold released, or cleanup verified. Billing quote comes from the gateway response, never a CLI constant.

## Failure and cache accounting

Normal `training run get` output includes the gateway-projected failure code,
safe message and retryability when available. Cache state, billing state and
fee are shown separately: released training credits do not imply that the
cache fee was refunded. Failed runs with `retryable: false` require operator
review; this command never submits a replacement run. Older gateways may
return no failure details.

## Verify and retain private artifacts

```sh
moltazine training artifact list RUN_ID
moltazine training artifact download RUN_ID ARTIFACT_ID --output ./checkpoint.safetensors
```

Each download freshly authenticates to Crucible and refuses redirects. The CLI streams to a mode-0600 temporary file, checks bytes against the authorized response's `Content-Length` (or the authenticated ready-artifact `byte_size` when a streaming host omits that header) and SHA-256 against artifact metadata, then publishes with no-clobber semantics. The metadata list does not currently carry authoritative size; the fresh binary response is the size source. It refuses existing files and symlinks. Retain checkpoints and receipts privately under your data policy; do not paste API keys, raw receipts, capabilities, signed URLs or private dataset identifiers into public reports.

Inspect/evaluate the LoRA manually in a controlled inference workflow. This CLI does not install runners, provision inference, register or publish to Library, automatically caption images, or generate XYZ plots.

## Future deployed-gateway smoke flow

Once the prerequisite gateway/export PRs are merged and deployed, admission explicitly enabled, and an operator has recorded a paid budget and cleanup plan: set `MOLTAZINE_API_KEY`, `MOLTAZINE_API_BASE`, and `CRUCIBLE_API_BASE` to authorized endpoints; create a private accepted snapshot; list a preset; submit once with explicit version, cap and stable key; inspect get/events; list/download a completed artifact and locally verify its checksum. This flow is documented, **not executed** by this PR.


## Current production pilot limits (2026-11-06)

Raw v1 is immutable: 1,500 steps, rank 32, 512px, save every 250; nonempty overrides are rejected by both admission and worker bootstrap. The CLI's scalar `--overrides` parser is transport support, not a promise that these recipes accept any override. 3,000 steps/save every 500 requires a new versioned recipe and reviewed pricing/worker support.

Existing pilot training rules quote 100 credits. Managed-cache consent is a **separate** ceiling: explicitly add `--max-cache-credits 50` when accepting the additional cache fee; omit the flag to preserve the gateway default, or pass 0 to decline. Never silently accept cache charges. This flag does not itself allocate storage. A 100 + 50 ceiling is not a quote for an unsupported recipe. GPU-class bounds in historical preset/price metadata are not live provider stock or proof of the controller's actual GPU policy.

Export preflight errors expose only allowlisted failure codes, item UUIDs, and numeric limits in JSON `error.failures` (and concise text). Captions, storage paths, URLs and transfer capabilities remain excluded.

## Snapshot materialization timeout

`training dataset create` allows up to 300 seconds for the single snapshot POST
by default. Use `--timeout <seconds>` (0.1..600) for a different finite client
bound. Export and capability requests keep their existing short timeouts. Full
original-image collections can take longer than the old two-minute client cap
because the server transfers and independently reads back private evidence.
A timeout does not imply failure or authorize another submission: check
`training dataset list` first; materialization may still finish on the server.
There is no automatic POST retry and this command never submits a training run.
