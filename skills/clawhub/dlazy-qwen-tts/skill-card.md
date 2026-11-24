## Description:

Generates speech with Alibaba Bailian Qwen3-TTS using a curated system voice or a custom voice description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can turn text into speech, choosing a supported language and system voice or describing a custom voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan had medium confidence because the external CLI and referenced components were not fully inspected, and the CLI login behavior could not be fully verified.

Mitigation: Review the pinned @dlazy/cli@1.2.3 package before installing and use a dedicated, rotatable API key.

Risk: Prompts are sent to dLazy's hosted API, and generated audio is hosted by its media service.

Mitigation: Avoid sending sensitive text and review dLazy's service terms before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio asset or URL with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports selectable language and voice; generation can return asynchronously.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
