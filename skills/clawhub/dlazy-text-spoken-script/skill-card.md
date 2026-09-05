## Description:

Generate high-contrast, resonant, and story-driven spoken scripts for short videos, character stories, and personal IP scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to draft short-video spoken scripts with a contrast hook, story development, viewpoint, persona tie-in, and punchline ending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact combines spoken-script guidance with instructions to install and run a third-party CLI.

Mitigation: Review the skill before installation and remove dLazy CLI execution sections if only spoken-script drafting is needed.

Risk: Prompts, parameters, and selected local media files may be sent to dLazy services after user confirmation.

Mitigation: Use only non-sensitive inputs, review upload behavior with the service owner, and rotate or revoke dLazy API keys when access is no longer required.

Risk: API-key storage is part of the documented workflow.

Mitigation: Prefer environment-scoped credentials where possible and verify local configuration file permissions before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown prose with optional bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include staged workflow guidance and generated script paragraphs; artifact guidance also references dLazy CLI commands.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
