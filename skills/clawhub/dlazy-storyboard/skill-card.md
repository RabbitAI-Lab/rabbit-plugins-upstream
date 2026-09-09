## Description:

Creates multi-shot animated storyboard and video projects with scripts, character and shot prompts, reference sheets, first and last frames, image-to-video shots, voice, music, sound effects, subtitles, and Remotion assembly guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to drive the dLazy storyboard template for consistent-character, multi-shot animated short projects. It helps start or continue project-scoped storyboard/video sessions through the pinned dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files are sent to dLazy-hosted services.

Mitigation: Avoid attaching sensitive local files unless they are required, and use the skill only when the dLazy service is trusted for the project data.

Risk: The skill depends on an external pinned dLazy CLI and service.

Mitigation: Prefer npx or another isolated install path when possible, and review the linked source or package before using a global install.

Risk: A dLazy API key is required and may be saved in local CLI configuration.

Mitigation: Keep the key scoped to the intended organization, protect the local config file, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project-scoped dLazy sessions and explicitly attached user files.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
