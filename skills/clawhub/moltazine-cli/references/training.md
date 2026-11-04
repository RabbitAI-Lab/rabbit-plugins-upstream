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

Choose a listed `preset_id` and explicit version. Check quote and current policy with the operator; `--max-credits` is your hard accepted ceiling, not a claim about your balance or the actual price. Reuse the same idempotency key only for an identical body; changed-body reuse is a conflict. The CLI sends exactly one POST and returns asynchronously by default. No automatic resubmission occurs on transport error or wait timeout.

```sh
moltazine training run submit --dataset SNAPSHOT_ID --preset PRESET_ID --preset-version 1 --max-credits 100 --idempotency-key YOUR_STABLE_KEY
moltazine training run get RUN_ID
moltazine training run events RUN_ID --limit 20
moltazine training run list --limit 20
```

Optional flat scalar overrides require `--overrides @file.json` (up to 32 keys). Only opt into polling with `--wait --timeout 300 --interval 5`; timeout is finite (max 3600 seconds) and exits 2, preserving the run ID and last observation. It does **not** mean failure or authorize another submit. Terminal failure/cancellation exits 3 when waiting. Ordinary run state and progress remain available through `run get`; heartbeat age can be unknown and is not a state transition.

Cancellation requests intent: `moltazine training run cancel RUN_ID`. Continue checking run, events, billing and cleanup separately. `cancel_requested` is not proof that compute stopped, credit hold released, or cleanup verified. Billing quote comes from the gateway response, never a CLI constant.

## Verify and retain private artifacts

```sh
moltazine training artifact list RUN_ID
moltazine training artifact download RUN_ID ARTIFACT_ID --output ./checkpoint.safetensors
```

Each download freshly authenticates to Crucible and refuses redirects. The CLI streams to a mode-0600 temporary file, checks bytes against the authorized response's `Content-Length` and SHA-256 against artifact metadata, then publishes with no-clobber semantics. The metadata list does not currently carry authoritative size; the fresh binary response is the size source. It refuses existing files and symlinks. Retain checkpoints and receipts privately under your data policy; do not paste API keys, raw receipts, capabilities, signed URLs or private dataset identifiers into public reports.

Inspect/evaluate the LoRA manually in a controlled inference workflow. This CLI does not install runners, provision inference, register or publish to Library, automatically caption images, or generate XYZ plots.

## Future deployed-gateway smoke flow

Once the prerequisite gateway/export PRs are merged and deployed, admission explicitly enabled, and an operator has recorded a paid budget and cleanup plan: set `MOLTAZINE_API_KEY`, `MOLTAZINE_API_BASE`, and `CRUCIBLE_API_BASE` to authorized endpoints; create a private accepted snapshot; list a preset; submit once with explicit version, cap and stable key; inspect get/events; list/download a completed artifact and locally verify its checksum. This flow is documented, **not executed** by this PR.
