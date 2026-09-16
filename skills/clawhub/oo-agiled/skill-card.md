## Description:

Agiled (agiled.app). Use this skill for Agiled requests to read, create, update, and delete contacts, projects, and tasks through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Agiled CRM, project, and task records through an OOMOL-connected account. It supports read actions directly and requires confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands, and the security summary marks the release suspicious pending review before installation.

Mitigation: Review and trust the OOMOL installer source before executing it; prefer a verified, pinned, or package-manager installation method when available.

Risk: The skill can create, update, and delete Agiled records.

Mitigation: Confirm exact payloads and effects before write actions, and obtain explicit approval before destructive actions.

## Reference(s):

- [Agiled homepage](https://agiled.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-agiled)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI to inspect live connector schemas before running Agiled actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
