## Description:

Qdrant Cloud lets agents operate Qdrant Cloud through the OOMOL oo CLI connector for reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Qdrant Cloud schemas, run Qdrant connector actions, and manage collections and dense-vector points through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI through a verified method where the source, version, and integrity can be inspected before execution.

Risk: Qdrant requests and responses pass through the OOMOL connector.

Mitigation: Use the skill only when the user trusts OOMOL and is comfortable with that connector path for the relevant Qdrant data.

Risk: Write actions can change Qdrant Cloud collections or points.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write or destructive.

## Reference(s):

- [Qdrant Cloud homepage](https://qdrant.tech/cloud/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qdrant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit oo connector schema and oo connector run commands and interpret JSON connector responses.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
