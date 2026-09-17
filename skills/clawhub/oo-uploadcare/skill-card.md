## Description:

Operate Uploadcare through an OOMOL-connected account using the oo CLI for file, group, and project actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Uploadcare files, groups, and project details through an OOMOL-connected account. It supports listing files and groups, retrieving metadata, storing files permanently, and deleting files after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote oo CLI installer commands could execute changing code on a user's machine.

Mitigation: Prefer installing the oo CLI manually from a reviewed, verified source before using the skill.

Risk: Uploadcare write and delete actions can change or remove user data.

Mitigation: Confirm the exact action payload and effect with the user, and require explicit approval before destructive delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-uploadcare)
- [Uploadcare Homepage](https://uploadcare.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before each action; destructive delete actions require explicit user approval.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
