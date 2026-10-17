## Description:

Synthesize text into natural-sounding speech with Doubao TTS through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can generate spoken narration from supplied text using Doubao voices through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text submitted for synthesis is sent to dLazy's hosted service.

Mitigation: Do not submit sensitive text unless its disclosure to dLazy is acceptable.

Risk: Using the skill requires a dLazy API key and third-party CLI.

Mitigation: Review the pinned CLI package before installation and keep the API key private.

Risk: Broad speech-generation requests can activate this skill unintentionally; its default voice is Chinese.

Mitigation: Request Doubao TTS explicitly and specify the voice language when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns a generated speech asset URL; the CLI can optionally save the result locally.]

## Skill Version(s):

1.3.29 (source: ClawHub release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
