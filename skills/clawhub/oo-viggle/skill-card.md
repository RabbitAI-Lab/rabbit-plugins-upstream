## Description:

Viggle enables an agent to read, create, update, and delete Viggle account resources through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Viggle through a connected OOMOL account, including listing resources, creating characters and render jobs, importing templates, checking render status, and managing scenes or characters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer one-liners for the oo CLI.

Mitigation: Do not let an agent run those installer commands automatically; install the oo CLI only from a trusted, verified source.

Risk: Write actions can create Viggle characters, scenes, templates, or render jobs.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

Risk: Destructive actions can soft-delete Viggle characters or scenes.

Mitigation: Confirm the target identifier and obtain explicit user approval before running any destructive action.

## Reference(s):

- [ClawHub Viggle skill page](https://clawhub.ai/oomol/skills/oo-viggle)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Viggle homepage](https://viggle.ai)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetch live action schemas before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
