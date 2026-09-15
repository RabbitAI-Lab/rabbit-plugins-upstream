## Description:

Forem (forem.com). Use this skill for Forem requests that read, create, or update data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Forem through OOMOL's connected account flow, including inspecting live action schemas, reading Forem content, and creating or updating articles with explicit confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run an unverified remote installer script for the oo CLI.

Mitigation: Review official installation instructions or use a pinned, verifiable package before running setup commands.

Risk: Forem write actions can create or update published content.

Mitigation: Confirm the exact payload and expected effect with the user before running state-changing actions.

Risk: The skill depends on OOMOL's oo CLI and server-side credential handling.

Mitigation: Install only if the publisher, CLI, and connected account flow are acceptable for the deployment environment.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Forem homepage](https://www.forem.com)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before requests and requires user confirmation before write or destructive actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
