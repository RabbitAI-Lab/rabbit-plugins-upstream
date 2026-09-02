## Description:

Generate high-quality cinematic effects videos with Google Veo 3.1, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or extend videos through the dLazy hosted Veo 3.1 integration from prompts, reference images, or source video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy API key can be stored in a local CLI configuration file.

Mitigation: Prefer DLAZY_API_KEY for per-invocation authentication, or review and tighten permissions on ~/.dlazy/config.json after login.

Risk: Prompts and media inputs are sent to dLazy services, and local media paths may be uploaded to dLazy-hosted storage.

Mitigation: Use the skill only with prompts and media files that are appropriate to share with dLazy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can return generated media URLs, asynchronous task IDs, or saved local media files when a save path is provided.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
