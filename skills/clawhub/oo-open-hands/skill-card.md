## Description:

OpenHands enables agents to operate OpenHands Cloud conversations through the OOMOL-connected open_hands connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to list, retrieve, start, and monitor OpenHands Cloud conversations and send follow-up messages through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup tells users to run remote installer scripts directly in a shell.

Mitigation: Review the installer path before installing, and prefer a pinned, verifiable package or download and inspect the installer before running it.

Risk: OpenHands write actions can change OpenHands Cloud state by starting conversations or sending follow-up messages.

Mitigation: Confirm the exact payload and intended effect with the user before running any write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-open-hands)
- [OpenHands Homepage](https://www.all-hands.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses include data and meta.executionId when actions run.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
