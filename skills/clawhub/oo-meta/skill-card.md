## Description:

Meta (business.meta.com) helps agents search and read Meta Graph and Ads data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Meta connector schemas, list available ad accounts and campaigns, retrieve the current Meta Graph user, and get Meta Ads insights without handling raw access tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute arbitrary code if followed without verification.

Mitigation: Review and independently verify the installer source before running curl or PowerShell installer pipelines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-meta)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Meta for Business](https://business.meta.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
