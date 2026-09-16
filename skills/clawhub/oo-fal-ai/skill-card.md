## Description:

This skill lets agents operate fal.ai through the OOMOL-managed oo CLI connector for model discovery, pricing, queue submission, status monitoring, cancellation, and result retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access fal.ai through an OOMOL-connected account, inspect live connector schemas, and run read or queued model actions with user review for write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an existing oo CLI session and includes setup paths that execute remote installation commands.

Mitigation: Install only after trusting OOMOL, verify official oo CLI installation instructions, and avoid piping remote scripts into a shell without review.

Risk: Queue submission and cancellation actions can change fal.ai state or incur cost.

Mitigation: Review the live action schema and exact JSON payload before approving write actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-fal-ai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [fal.ai homepage](https://fal.ai)
- [OOMOL connection settings](https://console.oomol.com/app-connections?provider=fal_ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses that include data payloads and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
