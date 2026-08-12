## Description:

Put a Gemini CLI subscription on the asale market by importing it, setting a price floor and concurrency cap, and checking which models are selling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to sell Gemini CLI subscription capacity through a local asale daemon while keeping account selection, price floors, concurrency, and daily token limits explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Gemini OAuth credentials for resale through the asale daemon.

Mitigation: Review the credential flow before use and proceed only if the user is comfortable allowing the daemon to copy and use the Gemini CLI OAuth credential.

Risk: The skill recommends installing or updating asale through a directly executed remote script.

Mitigation: Prefer a verified installer or inspect the install script before execution.

Risk: Changing sell settings can affect paid marketplace behavior.

Mitigation: Use conservative price, concurrency, and daily-limit settings; list accounts before changing sell status; and require explicit user approval before lowering minRatio.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/asale-sell-gemini)
- [asale homepage](https://asale.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl command examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Assumes a local asale daemon on loopback and a daemon token at ~/.asale/daemon.token.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter is 0.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
