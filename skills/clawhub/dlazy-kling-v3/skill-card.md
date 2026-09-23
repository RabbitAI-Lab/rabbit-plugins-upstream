## Description:

Powerful video generation with Kling v3, supporting high-quality text-to-video and image-to-video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy Kling v3 hosted video-generation service for text-to-video and image-to-video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording could route ordinary video requests to a paid external API.

Mitigation: Use explicit provider requests and dry runs where possible before making paid generation calls.

Risk: Prompts and referenced local media files may be sent to dLazy cloud services.

Mitigation: Install and invoke the skill only when cloud video generation through dLazy/Kling is intended.

Risk: The API key may be stored in local CLI configuration.

Mitigation: Use DLAZY_API_KEY per run when persistent local credential storage is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted generated media URLs, async task identifiers, and optional saved local files.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
