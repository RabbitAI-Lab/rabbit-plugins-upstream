## Description:

Synthesizes text into natural speech using Doubao text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators can turn text into spoken audio using Chinese or English voices for narration and voice broadcasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text and any supplied media are sent to dLazy's hosted service for processing.

Mitigation: Send only text and media you are comfortable sharing with dLazy.

Risk: CLI login saves an organization API key locally, and the pinned CLI's credential protections were not verified.

Mitigation: Use the documented DLAZY_API_KEY environment-variable option when you want to avoid saving the key through CLI login, and review the pinned CLI before installation.

Risk: Speech generation may incur service charges.

Mitigation: Consider service charges before generating speech.

## Reference(s):

- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [Generated audio asset URL or saved audio file, with JSON task and result details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice language, voice, and speaking speed can be selected.]

## Skill Version(s):

1.3.37 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
