## Description:

Use this skill for Ortto requests that read, create, or update data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve, list, create, and update Ortto people records through an OOMOL-connected Ortto account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that execute downloaded scripts.

Mitigation: Use official, verifiable installation steps and inspect downloaded installers before running them.

Risk: The Ortto connector can access an Ortto account through OOMOL-managed credentials.

Mitigation: Install only when that access model is acceptable and connect the minimum appropriate Ortto account or scope.

Risk: The merge_people action can create or update Ortto people records.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Ortto homepage](https://ortto.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Ortto skill on ClawHub](https://clawhub.ai/oomol/skills/oo-ortto)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON connector responses.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
