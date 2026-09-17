## Description:

Encodian (encodian.com). Use this skill for ANY Encodian request: reading, creating, and updating data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Encodian PDF actions through an OOMOL-connected account, including PDF compression, page extraction, text-layer extraction, encryption, and unlocking. It guides schema inspection, JSON payload construction, and confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Use a verified package, pinned release, checksum, or official installation path with integrity checks before installing the oo CLI.

Risk: The skill can run Encodian connector actions that alter document protection state.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before running actions tagged as write or destructive.

## Reference(s):

- [ClawHub Encodian Skill](https://clawhub.ai/oomol/skills/oo-encodian)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Encodian Homepage](https://www.encodian.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce base64-encoded PDF results through Encodian connector responses.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
