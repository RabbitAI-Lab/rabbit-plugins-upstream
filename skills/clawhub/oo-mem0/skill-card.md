## Description:

Helps agents manage and search Mem0 memories through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents with a connected Mem0 account use this skill to add, find, inspect, update, and delete memories, and to view related events and users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute an unverified remote installer script.

Mitigation: Use a trusted package or verified download; run a remote installer only after explicit approval and source review.

Risk: Write and delete actions can change or remove stored memories.

Mitigation: Confirm the exact memory ID, payload, and intended effect before executing changes.

## Reference(s):

- [Mem0 homepage](https://mem0.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Mem0 skill](https://clawhub.ai/oomol/skills/oo-mem0)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text and structured JSON action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected Mem0 action and connected account.]

## Skill Version(s):

1.0.4 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
