# PR Tracking & Follow-up Workflow

## Session Example (2026-06-18)

Tracked 6 PRs across 4 repositories. Key findings:

### Merged PRs (4)
1. **fastino-ai/GLiNER2 #112** — Merged 2026-06-16, fixes #111
   - Issue: `pip install gliner2[local]` fails because pyproject.toml missing [local] extra
   - Fix: Added torch/transformers/peft to [project.optional-dependencies]
   - **Note**: Fix merged but NOT in release (latest v1.3.1 is from before merge)

2. **nexus-substrate/nexus-toolkit #17** — Merged 2026-06-16, fixes #11
   - Issue: zod in devDependencies but required at runtime
   - Fix: Moved zod from devDependencies to dependencies
   - **Note**: Repository has zero releases/tags

3. **nexus-substrate/memory-bench #17** — Merged 2026-06-16, fixes #15
   - Issue: Missing @types/node causes CI typecheck failure
   - Fix: Added @types/node@^22 to devDependencies
   - **Note**: Repository has zero releases/tags

4. **ott-jax/ott #701** — Merged 2026-06-08, fixes #700
   - Issue: batching.is_vmappable removed from public JAX module in 0.9.0
   - Fix: Changed to submodule import `import jax._src.interpreters.batching as batching`
   - **Note**: Fix merged but NOT in release (latest v0.6.0 is from 7 months ago)

### Stale PRs (2) — Required Action

5. **PostHog/posthog #60979** — OPEN + STALE
   - Issue: MCP tool schema has top-level anyOf, rejected by Anthropic API
   - Fix: Wrap union in z.object({}).passthrough().and(...)
   - **Action taken**: Posted bump comment to prevent auto-closure
   - **Status**: No human review yet, only bot reviews

6. **PostHog/posthog #60976** — OPEN + STALE
   - Issue: split_url_and_private_token() crashes with multiple '?' in URL
   - Fix: Changed url.split("?") to url.split("?", 1)
   - **Action taken**: Posted bump comment to prevent auto-closure
   - **Status**: No human review yet, tests still needed (committed to adding)

## Key Patterns

### Stale Bot Behavior
- Warning appears after ~7 days of inactivity
- Auto-closure happens ~7 days after warning
- Bump comment resets the inactivity timer
- Comment should mention the PR is still relevant and request human review

### Release Gap Detection
- Check latest release: `gh release list --repo OWNER/REPO --limit 5`
- Compare merge date with release date
- If merged after latest release, note "fix not yet released"
- Don't take action (releasing is maintainer's responsibility)

### Obsidian Note Structure
- Date-stamped tracking file: `github-pr-跟踪-YYYYMMDD.md`
- Sections: 已合并 ✅, 需要跟进 ⚠️
- Each PR entry: title, status, author, description, action needed, link
- Summary table at bottom for quick reference

## Commands Reference

```bash
# Check PR status
gh pr view NUMBER --repo OWNER/REPO --json state,title,reviewDecision,createdAt,url,author,comments

# Check linked issue
gh issue view NUMBER --repo OWNER/REPO --json state

# Check releases
gh release list --repo OWNER/REPO --limit 5

# Post bump comment
gh pr comment NUMBER --repo OWNER/REPO --body "@stale-bot This PR is still relevant..."

# List our open PRs
gh pr list --repo OWNER/REPO --author gavin913-lss --state open --json title,url,number,reviewDecision
```
