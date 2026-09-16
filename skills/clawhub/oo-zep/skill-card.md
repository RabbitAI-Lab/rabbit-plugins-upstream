## Description:

Use this skill to read, create, update, and delete Zep data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Zep projects, users, conversation threads, messages, and graph memory context through OOMOL-connected credentials without handling raw Zep API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer scripts that can be piped directly into a shell.

Mitigation: Install the oo CLI through a verifiable package or downloaded installer that can be inspected and validated, and avoid running pipe-to-shell commands from an elevated shell.

Risk: Zep write and destructive actions can change or delete users, threads, messages, and memory data.

Mitigation: Confirm the exact target, payload, and effect with the user before allowing write or delete actions to run.

## Reference(s):

- [Zep homepage](https://www.getzep.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zep)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and requires user confirmation for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
