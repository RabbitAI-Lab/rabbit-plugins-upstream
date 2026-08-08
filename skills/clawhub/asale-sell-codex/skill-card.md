## Description:

Put a Codex or ChatGPT subscription on the asale market by importing it, setting a price floor and concurrency cap, and checking which models are selling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage selling a Codex or ChatGPT subscription through the asale marketplace, including account import, selling terms, lane status, and error handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can import Codex or ChatGPT subscription credentials into a third-party marketplace daemon.

Mitigation: Install only when intentionally selling through asale; review the asale source and installer first, understand credential revocation, and set conservative concurrency, price floor, and daily limits.

Risk: The skill documents remote installer commands for the asale daemon.

Mitigation: Review the installer and source repository before running the install command or updates.

Risk: Changing selling settings from stale account data can overwrite user-selected price floor or concurrency values.

Mitigation: Run list_accounts before set_account_sell, do not lower minRatio without explicit user approval, and verify lane status before resuming paused lanes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/asale-sell-codex)
- [asale homepage](https://asale.ai)
- [asale source repository](https://github.com/asale-ai/asale)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require a local asale daemon, its local token, and user confirmation before lowering price floors.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 0.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
