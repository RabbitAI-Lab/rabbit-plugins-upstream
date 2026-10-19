## Description:

Searches the ElevenLabs voice library by keyword, source, and category to help users choose a voice for text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers search available voices and listen to previews before choosing one for text-to-speech narration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the dLazy CLI requires an API key stored locally, and searches send prompts to dLazy.

Mitigation: Install only if comfortable with the CLI and hosted service; protect the key and avoid sensitive search prompts.

Risk: The broader CLI documentation describes uploading local media paths to dLazy.

Mitigation: Do not pass local file paths unless you intend to upload those files.

Risk: The documented image output and save options do not clearly match the voice-search preview use case.

Mitigation: Confirm the voice-search output and save behavior with the publisher before relying on previews or downloads.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown describing voice matches and preview links from CLI JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview and download behavior is not fully clear from the supplied documentation.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
