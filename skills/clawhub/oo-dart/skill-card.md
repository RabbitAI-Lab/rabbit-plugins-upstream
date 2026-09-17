## Description:

Dart (dartai.com). Use this skill for ANY Dart request: reading, creating, updating, and deleting data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external agents use this skill to manage Dart tasks through an OOMOL-connected account. It supports task creation, retrieval, listing, update, deletion, and workspace configuration lookup while requiring live schema inspection before building action payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer commands that could execute unverified remote scripts.

Mitigation: Use a verified, pinned official installation path and inspect or validate installers before execution.

Risk: The skill can create, update, or delete Dart tasks when write or destructive actions are requested.

Mitigation: Confirm the exact payload, target item, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Dart homepage](https://www.dartai.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dart)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payload construction; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
