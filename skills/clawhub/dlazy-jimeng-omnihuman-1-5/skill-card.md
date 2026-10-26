## Description:

Generate realistic digital human broadcast videos from portrait images and audio/text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to generate digital-human broadcast videos from a portrait image and audio or text with Jimeng OmniHuman 1.5.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portraits, audio, and prompts are sent to dLazy for cloud processing, and generation can consume account credits.

Mitigation: Use only media you are comfortable uploading, review the service terms, and check the cost estimate before generation when appropriate.

Risk: Logging in stores an organization API key in the local CLI configuration, including when using the on-demand CLI option.

Mitigation: Protect the local configuration file, review the pinned CLI before installing or running it, and revoke or rotate the key if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI repository (listed in skill documentation; provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands, Guidance]

**Output Format:** [Generated video asset URL in a JSON response; optionally downloaded as a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation; a portrait image and audio or text prompt are supplied as inputs.]

## Skill Version(s):

1.3.32 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
