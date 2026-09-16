## Description:

This skill manages Gleap data through OOMOL's oo CLI, including reading, creating, updating, and deleting contacts and tickets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Gleap contacts and tickets through an OOMOL-connected account. It supports reading, creating, updating, and deleting Gleap data after inspecting live action schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review and use an official, versioned, verifiable oo CLI installation path before installing.

Risk: Write and destructive actions can create, update, or delete Gleap contacts and tickets.

Mitigation: Inspect the live action schema first and confirm the exact target, payload, and expected effect before approving write or delete operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gleap)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Gleap Homepage](https://www.gleap.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI connector responses containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
