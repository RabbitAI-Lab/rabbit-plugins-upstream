## Description:

Search the ElevenLabs voice library by keyword, source, and category to help select a voice using available previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to search for ElevenLabs voices by keyword, source, or category and review previews before choosing a voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs the pinned dLazy CLI and stores a dLazy API key locally.

Mitigation: Review the CLI before installation, and use an appropriately scoped key that can be rotated or revoked.

Risk: Search prompts and parameters are sent to dLazy; the documentation also describes local-file upload and saving outputs beyond voice search.

Mitigation: Avoid private local files and sensitive --save paths until the publisher clarifies the behavior and confirms the voice-search output format.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown guidance; CLI response documented as JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice previews are claimed, but the documented response example shows an image asset rather than voice-search results.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
