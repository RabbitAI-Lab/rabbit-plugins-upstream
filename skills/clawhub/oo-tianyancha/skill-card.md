## Description:

Provides Tianyancha company search and data retrieval workflows through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and retrieve Tianyancha company records, ownership relationships, risk, judicial, intellectual property, news, tender, and identity verification data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands executed directly in a shell.

Mitigation: Prefer a versioned package or manually download, inspect, and verify the installer before running it.

Risk: Company intelligence responses may contain sensitive or consequential business data.

Mitigation: Review returned data before acting on it and confirm payloads for any action that the skill marks as write or destructive.

## Reference(s):

- [ClawHub Tianyancha skill page](https://clawhub.ai/oomol/skills/oo-tianyancha)
- [Tianyancha data homepage](https://www.tianyancha.com/data)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
