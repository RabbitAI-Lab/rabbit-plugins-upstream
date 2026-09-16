## Description:

Needle helps agents read, create, update, and search Needle collections through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Needle collections through OOMOL, including listing collections, inspecting files and statistics, searching content, creating collections, and importing URL-backed files for indexing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include piping remote installer scripts directly into a shell or elevated PowerShell session.

Mitigation: Install the oo CLI from a verified, versioned source and review installation steps before execution.

Risk: Write actions can create collections or import URL-backed files into Needle for indexing.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Needle homepage](https://needle.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI connector commands and summarize JSON action responses.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
