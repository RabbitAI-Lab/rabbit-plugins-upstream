## Description:

Turns a script, screenplay, or shot list into a storyboarded, shot-by-shot video by breaking down scenes, generating shots, assembling, and validating the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to drive the dLazy storyboard agent from scripts or scene breakdowns and produce multi-shot animated videos with consistent characters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to api.dlazy.com and files explicitly attached with --files are uploaded to files.dlazy.com.

Mitigation: Avoid sending sensitive scripts or private media unless the dLazy service terms and organizational data-handling requirements are acceptable.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-run credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill relies on a pinned third-party npm CLI and hosted service.

Mitigation: Review the pinned package and source before installation, especially for workflows involving paid credits or private assets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts and explicitly attached files are passed through the dLazy CLI; generated media is produced by the external dLazy hosted service.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
