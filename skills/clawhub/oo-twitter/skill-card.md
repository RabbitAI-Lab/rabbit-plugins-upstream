## Description:

Operates X (Twitter) through an OOMOL-connected account for reading, creating, updating, and deleting data via the `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to operate an authenticated X (Twitter) account through OOMOL's connector. It supports public reads plus user-approved state-changing actions such as posting, messaging, bookmarking, following, muting, list management, and media upload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer commands for the `oo` CLI, creating local code-execution and supply-chain exposure.

Mitigation: Use a verified package when available, or inspect and verify the installer before execution.

Risk: The skill can perform write and destructive X (Twitter) actions such as posting, sending DMs, deleting posts, following, muting, and changing lists.

Mitigation: Confirm the exact action, target, and JSON payload with the user before running write or destructive commands.

Risk: Use requires trusting OOMOL's connector with access to the connected X/Twitter account.

Mitigation: Install only for trusted OOMOL accounts and use the connector only with the intended authenticated account and scopes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-twitter)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [X (Twitter) homepage](https://x.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the OOMOL `oo` CLI and connector responses are JSON when executed with `--json`.]

## Skill Version(s):

1.0.4 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
