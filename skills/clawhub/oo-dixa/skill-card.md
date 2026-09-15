## Description:

Dixa lets agents read Dixa agents, conversations, end users, messages, and presence through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support operations users, and agents use this skill to retrieve Dixa support data from a connected account, including agents, conversations, messages, end users, and presence status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path tells users or agents to execute a remote installer directly.

Mitigation: Review the setup path before installation, prefer a verified or manually inspected OOMOL CLI installation method, and avoid running installer commands as administrator or root.

Risk: Future versions could add write or destructive Dixa actions beyond the listed read actions.

Mitigation: Use only the listed read actions unless a future version clearly declares and scopes write permissions, and confirm exact payloads before any state-changing action.

## Reference(s):

- [Dixa Homepage](https://www.dixa.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
