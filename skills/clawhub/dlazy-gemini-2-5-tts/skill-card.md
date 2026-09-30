## Description:

Generates natural-sounding speech from Chinese or English text using Gemini 2.5 TTS through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn Chinese or English text into spoken audio through the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive content without reviewing the service and CLI first.

Risk: Installing an external npm CLI executes third-party software.

Mitigation: Review the CLI package before installation; use the documented version-pinned npx command to avoid a global install.

Risk: A stored dLazy API key could be exposed if the user's credentials are mishandled.

Mitigation: Protect the CLI configuration and manage the key as a credential; rotate or revoke it if exposed.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Audio links]

**Output Format:** [Markdown guidance with shell commands and links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and access to the dLazy hosted service.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; bundled SKILL.md says 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
