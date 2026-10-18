## Description:

Uses a reference voice recording to generate spoken audio for new text through Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use a permitted reference voice to produce spoken audio for new text using the dLazy-hosted Vidu Audio Clone service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloned voices can be used without consent or for impersonation.

Mitigation: Use only voices you own or have explicit permission to clone, and avoid deceptive impersonation.

Risk: Voice samples and prompts are sent to dLazy cloud services.

Mitigation: Obtain permission to upload the recording and review its sensitivity before sending it.

Risk: The skill's sample output shows an image even though it describes audio generation.

Mitigation: Verify the actual result type and URL before presenting or using generated media.

Risk: CLI login saves an API key locally.

Mitigation: Use a per-run DLAZY_API_KEY when persistent storage is unwanted; rotate or revoke compromised keys.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and brief usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return result URLs or an asynchronous task ID; the documented image example should not be treated as an audio-output guarantee.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; bundled frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
