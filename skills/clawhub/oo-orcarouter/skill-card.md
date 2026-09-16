## Description:

Use this skill to route OrcaRouter requests for reading, creating, and updating data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect OrcaRouter action schemas, run model listing, and create chat completions, embeddings, or Anthropic-format messages through an OOMOL-connected OrcaRouter account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports unverified remote installer commands in the first-time setup fallback.

Mitigation: Review before installing, avoid running installer pipelines blindly, and prefer official versioned installation steps with checksum or signature verification.

Risk: The skill can create chat completions, embeddings, and messages through an OrcaRouter account.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before running write actions.

## Reference(s):

- [OrcaRouter homepage](https://www.orcarouter.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OrcaRouter skill page](https://clawhub.ai/oomol/skills/oo-orcarouter)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payload construction; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
