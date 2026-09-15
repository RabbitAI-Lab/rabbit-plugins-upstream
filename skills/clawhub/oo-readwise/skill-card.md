## Description:

Readwise access skill for reading, creating, and updating highlights, books, sources, and Reader documents through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to work with Readwise data from an agent, including exporting highlights, listing books or documents, saving URLs, and creating or updating highlights and documents after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly.

Mitigation: Review and use a verified oo CLI installation path before installing; avoid running pipe-to-shell commands blindly.

Risk: Write actions can modify Readwise highlights or Reader documents.

Mitigation: Inspect the live action schema and confirm the exact JSON payload and expected effect with the user before running write actions.

## Reference(s):

- [Readwise homepage](https://readwise.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Readwise skill page](https://clawhub.ai/oomol/skills/oo-readwise)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Readwise connector schemas before running actions; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
