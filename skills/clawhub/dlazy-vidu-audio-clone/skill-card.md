## Description:

Uses a reference voice recording to generate speech reading new text with Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to clone an authorized voice from reference audio and generate spoken audio for new text through dLazy's hosted Vidu service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning without the speaker's consent or rights.

Mitigation: Use only reference recordings for which you have the speaker's consent and necessary rights.

Risk: Reference media and prompts are sent to dLazy's cloud service, and an API key is required.

Mitigation: Share only intended media and prompts; protect the API key and review the service before use.

Risk: The documented example describes image/png output for an audio-cloning skill.

Mitigation: Check the actual response and media type before relying on the example or sharing a result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses include generated media URLs or asynchronous task IDs.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
