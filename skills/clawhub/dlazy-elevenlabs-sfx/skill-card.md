## Description:

Generates 1–22-second sound effects from text descriptions for foley, ambience, alerts, and games using the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to request short sound effects for foley, ambient scenes, notifications, and games through a hosted generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to the third-party dLazy service, and supplied media files may be uploaded.

Mitigation: Avoid sensitive prompts and files unless dLazy's handling meets your requirements.

Risk: Authentication may persist an API key in local CLI configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY option if you do not want a saved key.

Risk: The skill relies on a separately installed third-party CLI and hosted generated files.

Mitigation: Verify the CLI package before use and assess where generated files are hosted before sharing sensitive material.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides generation and retrieval of hosted or locally saved audio; asynchronous requests may require status polling.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; supplied skill files declare 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
