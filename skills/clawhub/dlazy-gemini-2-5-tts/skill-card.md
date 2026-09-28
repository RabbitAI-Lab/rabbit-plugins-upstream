## Description:

Helps agents generate multilingual speech from text using Gemini 2.5 TTS through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can guide an agent to turn text into speech with selectable language and voice through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generated outputs pass through dLazy's hosted service.

Mitigation: Confirm that sending input to dLazy and hosting results there is acceptable before use.

Risk: Signing in stores an API key in the local CLI configuration.

Mitigation: Protect the user configuration and rotate or revoke the key if compromised.

Risk: The sample output describes an image instead of speech and may not match actual results.

Mitigation: Verify the actual output format rather than relying on the sample.

Risk: Global CLI installation persists on the user's system.

Mitigation: Prefer the documented pinned npx invocation when a persistent installation is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI source (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked service returns hosted result URLs; the documented sample response depicts an image rather than speech and may be outdated.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata; skill frontmatter says 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
