## Description:

Qdrant Cloud enables agents to read, create, and update Qdrant Cloud data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Qdrant Cloud schemas, manage collections, retrieve and search points, scroll point data, and upsert dense-vector points through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands could execute changed external code on a user's machine.

Mitigation: Review the installer source and prefer a pinned, verifiable installation method; do not allow an agent to run the installer automatically from an elevated shell.

Risk: Write actions can change Qdrant Cloud collections or point data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write actions.

## Reference(s):

- [Qdrant Cloud homepage](https://qdrant.tech/cloud/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qdrant)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI and may return JSON responses with execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
