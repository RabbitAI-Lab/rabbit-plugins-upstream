## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy CLI for Jimeng Dream Actor image-to-video generation from prompts and supported media references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy cloud services for generation.

Mitigation: Only submit media and prompts that are appropriate to upload to dLazy.

Risk: Using dlazy login or dlazy auth set stores an API key in the local dLazy CLI configuration.

Mitigation: Treat ~/.dlazy/config.json as sensitive, prefer npx when avoiding a persistent global install, and rotate or revoke keys if needed.

Risk: The skill depends on a third-party CLI and hosted API.

Mitigation: Review the dLazy CLI source or package before installing and use the pinned @dlazy/cli version declared by the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs or an async generateId; selected local media inputs are uploaded to dLazy.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
