## Description:

OSS Insight lets agents search and read OSS Insight repository analytics through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve OSS Insight analytics for GitHub repositories, collections, trending repositories, and rankings through validated connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes direct shell execution of remote installer scripts.

Mitigation: Review the skill before installing, install the oo CLI only through a trusted source and verification process, and do not allow an agent to run curl-to-bash or PowerShell iex installer commands automatically.

Risk: Authentication and billing setup steps may require user-controlled account actions.

Mitigation: Approve sign-in steps manually and treat HTTP 402 or insufficient-credit errors as a billing stop that should be resolved by the user before retrying.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ossinsight)
- [OSS Insight Homepage](https://ossinsight.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include OSS Insight data and execution metadata when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
