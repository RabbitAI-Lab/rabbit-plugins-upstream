---
name: publish-skills
description: Publish approved skills to ClawHub through GitHub Actions. Use for skill publication, scoped release previews, registry verification, and publish failures.
---

# ClawHub Skill Publish

Publish one approved skill through GitHub Actions. Select all skills only with explicit approval.

## Approval and scope

- Get explicit approval before a commit, push, or registry publication.
- Keep publication manual through `workflow_dispatch`.
- Keep `dry_run` enabled by default.
- Never add a push or schedule trigger.
- Publish only from a `j3ffyang/*` repository.
- Keep the `github.repository_owner == 'j3ffyang'` job guards.
- Push approved commits to both `j3ffyang` and `negtivspace`.
- Treat a push as source publication only. It does not authorize a registry publication.
- Never use a local publish command as a second release path.

The private global rules require manual publication. Older instructions that described automatic publication on push are obsolete.

## Scope selection in ai-thoughts

The publisher requires one scope:

```sh
python scripts/clawhub_publish.py --skill md-to-medium --dry-run
python scripts/clawhub_publish.py --skill md-to-medium
python scripts/clawhub_publish.py --all --dry-run
```

The script rejects a missing scope. It also rejects unknown skill names before it accesses ClawHub.

The workflow accepts these inputs:

| Input | Meaning |
| --- | --- |
| `skill` | One exact folder name under `.opencode/skills/`, or `ALL` for an approved bulk release |
| `source_sha` | Full source commit SHA |
| `dry_run` | Preview only, defaults to `true` |

Use the same scope and source SHA for preview and publication. If either changes, run a new preview.

The workflow checks out the specified commit. It verifies that the checkout matches the requested SHA.

The concurrency group serializes workflow runs. A new run does not cancel an active publish.

## Release procedure

1. Read the live workflow and publisher.
2. Inspect the selected skill's diff.
3. Check the staged files for credentials.
4. Run the checks appropriate to the changes.
5. Commit only the approved files.
6. Push to both remotes.
7. Record the full commit SHA.
8. Dispatch a preview for the selected skill and SHA.
9. Wait for the preview to finish.
10. Read the scope, source SHA, current version, and proposed version in the log.
11. If the preview selects another skill, stop.
12. If publication is approved, dispatch the same scope and SHA with `dry_run=false`.
13. Wait for publication to finish.
14. Read the registry verification result.

Example preview:

```sh
SHA=$(git rev-parse HEAD)
gh workflow run clawhub-skill-sync.yml \
  --repo j3ffyang/ai-thoughts --ref main \
  -f skill=md-to-medium -f source_sha="$SHA" -f dry_run=true
```

Example publication after a successful preview:

```sh
gh workflow run clawhub-skill-sync.yml \
  --repo j3ffyang/ai-thoughts --ref main \
  -f skill=md-to-medium -f source_sha="$SHA" -f dry_run=false
```

Use the run URL returned by GitHub:

```sh
gh run watch RUN_ID --repo j3ffyang/ai-thoughts --exit-status
gh run view RUN_ID --repo j3ffyang/ai-thoughts --log
```

## Results and verification

The pinned CLI calculates the version from the registry fingerprint. The publisher preserves that version in its report.

| Result | Meaning | Action |
| --- | --- | --- |
| `would-publish` | Preview found a change | Check the proposed version |
| `unchanged` | Fingerprint matches | Report that no upload was needed |
| `published` | CLI reported publication | Check `verification` |
| `submitted` or `pending-publication` | CLI accepted the upload asynchronously | Check `verification` |
| `verified` | Public API owner and latest version match | Report the verified version |
| `verification-pending` | Public visibility is not confirmed | Recheck the API without uploading again |
| `pending-moderation` | A known moderation collision reserved the version | Wait for moderation |
| `owner-mismatch` | Registry owner differs | Stop |
| `cli-error`, `registry-error`, or invalid output | The operation failed | Inspect the error |

The publisher retries public visibility checks four times. It waits ten seconds between checks.

It never retries an upload during verification. Pending results appear separately from verified results.

A successful workflow can contain a pending result. Do not call that result live.

Read the public API:

```sh
curl --fail --silent --show-error \
  https://clawhub.ai/api/v1/skills/md-to-medium
```

Confirm `owner.handle` is `j3ffyang`. Confirm `latestVersion.version` matches the version reported by the CLI.

If visibility is delayed, inspect the API again later. Do not upload the same version again.

## Repository-specific pipelines

These repositories are siblings under `~/pool/git/`. Read each live workflow before dispatch.

| Repository | Skill source | Publisher |
| --- | --- | --- |
| `ai-thoughts` | `.opencode/skills/<slug>/` | Scoped in-repo `scripts/clawhub_publish.py` |
| `history` | `.opencode/skills/chinese-history-literature-culture` | Repository workflow |
| `ai-custom-skills` | `openclaw/`, `hermes/`, `claude-code/` | Repository workflow |

Only `ai-thoughts` implements the scope and SHA inputs described above. Do not assume that another repository accepts them.

The `ai-thoughts` workflow uses ClawHub CLI tag `v0.23.3`. It needs `contents: read` and the `clawhub_token` repository secret.

The reusable upstream workflow can also require `id-token: write`. Check the caller's permissions if startup fails.

The `negtivspace` repositories are mirrors. Their owner guards prevent duplicate uploads to the same ClawHub account.

The canonical `simplified-to-traditional` skill lives in `ai-thoughts`. Never publish its local-only `history` copy.

The `history` copy of `character-name-literary-origins` is also local-only.

Some `ai-custom-skills` paths are double-nested. Use the folder that contains `SKILL.md`.

## Failure handling

- If the registry reports an existing version, inspect its public state before retrying.
- If the CLI returns `pending-publication`, treat it as accepted rather than verified.
- If a known moderation collision occurs, keep it in `KNOWN_PENDING` until the skill becomes public.
- If a different error occurs for a known pending skill, report a failure.
- If a skill becomes public, remove its obsolete `KNOWN_PENDING` entry through an approved change.
- If the token is missing, configure the `clawhub_token` repository secret.
- If the slug starts with `clawhub-` or ends with `-clawhub`, choose an allowed name.

`publish-skills` is the canonical slug for this skill. Do not revive the legacy `skill-publish` release path.
