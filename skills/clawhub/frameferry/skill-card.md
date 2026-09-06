## Description:

Archive public Instagram media through InstaCognito with bounded archive/sync runs, section-aware outcomes, durable receipts, and optional local ZIP export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[saju01](https://clawhub.ai/user/saju01)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use FrameFerry to archive or periodically sync public Instagram media they are allowed to keep, using bounded local CLI runs with receipts, status reporting, and optional ZIP export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Archiving public social media can violate rights, privacy expectations, or provider terms if used outside an authorized scope.

Mitigation: Use FrameFerry only for public profiles the user is allowed to archive, avoid commercial-scale scraping, and preserve the skill's bounded run limits.

Risk: The skill needs local npm, Playwright, browser, filesystem, and network access for archive runs.

Mitigation: Install only in an environment where that access is acceptable, run `node ./bin/frameferry.js doctor`, and write exports to a dedicated non-sensitive output folder.

Risk: CDP attachment can interact with an existing local browser session if intentionally enabled.

Mitigation: Avoid CDP attachment unless the user explicitly approves it; when used, keep it loopback-only and do not provide cookies, tokens, or private session data.

Risk: A partial archive or successful ZIP export can be mistaken for a complete archive.

Mitigation: Check FrameFerry status and section outcomes after each run; treat COMPLETE as the only complete archive outcome and keep PARTIAL, BLOCKED, DEFERRED, and ACTION_REQUIRED visible.

## Reference(s):

- [FrameFerry ClawHub Skill Page](https://clawhub.ai/saju01/skills/frameferry)
- [FrameFerry Repository](https://github.com/saju01/frameferry)
- [InstaCognito Public Photo Page](https://instacognito.com/en/photo)
- [Model-tiered orchestration](references/orchestration.md)
- [OpenClaw sub-agents](https://docs.openclaw.ai/tools/subagents)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and compact JSON/status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide a local Node CLI that writes media files, JSON receipts, manifests, status files, and optional ZIP exports to a user-selected output directory.]

## Skill Version(s):

0.2.0 (source: CHANGELOG.md and package.json, released 2026-09-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
