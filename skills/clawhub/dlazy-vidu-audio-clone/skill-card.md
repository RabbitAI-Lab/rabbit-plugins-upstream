## Description:

Helps agents clone a voice from reference audio and generate speech reading new text with Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to generate spoken audio from supplied text and reference audio through dLazy's Vidu Audio Clone service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local reference audio may be uploaded to dLazy's cloud service.

Mitigation: Review the material and service terms before submitting sensitive content.

Risk: The dLazy CLI can persist an API key in local configuration.

Mitigation: Use a per-run DLAZY_API_KEY when persistent key storage is unwanted.

Risk: Voice cloning can impersonate a person without consent.

Mitigation: Clone only voices for which you have appropriate consent.

## Reference(s):

- [dLazy CLI source (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with shell commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent may relay a hosted result URL or an asynchronous task ID.]

## Skill Version(s):

1.3.24 (source: server-resolved ClawHub release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
