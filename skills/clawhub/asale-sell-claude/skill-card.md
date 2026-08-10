## Description:

Helps an agent import a Claude Code or Claude subscription into asale, set a price floor and concurrency cap, and check which models are selling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Claude subscription holders use this skill to manage selling a Claude account through a local asale daemon while preserving account limits and requiring confirmation for price-floor reductions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to offer a Claude subscription on a market and imports local Claude credentials into the asale daemon.

Mitigation: Install and use it only when the user intentionally wants to sell that subscription, confirm the exact account before import, and verify that selling can be disabled in the asale UI.

Risk: The install path uses a remote installer and a local daemon that reads a token from ~/.asale/daemon.token.

Mitigation: Review the installer or use a verified manual install when available, keep daemon access on loopback, and avoid exposing the daemon token.

Risk: Changing price floors, concurrency, or daily limits can affect spending, revenue, and account behavior.

Mitigation: Run account discovery before sell-setting changes, set conservative limits, and require explicit user approval before lowering minRatio.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/asale-sell-claude)
- [asale homepage](https://asale.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance should require account discovery before sell-setting changes, ask before lowering price floors, and stop on sign-in or daemon connection errors.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
