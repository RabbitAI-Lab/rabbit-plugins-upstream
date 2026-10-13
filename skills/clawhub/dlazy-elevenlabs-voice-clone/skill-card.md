## Description:

Guides an agent to clone a custom voice from a clean audio sample for use with ElevenLabs text-to-speech through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to prepare a voice-cloning request from an authorized audio sample and use the resulting custom voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented commands and example output are inconsistent with the voice-cloning workflow.

Mitigation: Check the actual command options with dlazy elevenlabs-voice-clone -h and review the response before relying on it.

Risk: Voice samples supplied as local paths or pipe references may be uploaded to dLazy's hosted service.

Mitigation: Use only voice samples you are authorized to share, and avoid local paths or pipe references unless you intend to upload that data.

Risk: Using the skill requires a third-party CLI, hosted service, and API credentials.

Mitigation: Install only if you trust dLazy and the pinned CLI package, and use revocable API keys.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses may contain hosted result URLs or asynchronous task IDs; verify actual output because the documented example does not match the voice-cloning task.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
