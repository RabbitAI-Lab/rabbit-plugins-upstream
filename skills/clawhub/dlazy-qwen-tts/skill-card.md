## Description:

Alibaba Bailian qwen3-tts text-to-speech. Choose from curated system voices (including dialects) or design a custom voice from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators can synthesize speech from text with a curated voice, including dialects, or describe a custom voice. They can select a language and receive generated speech through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generation parameters are sent to dLazy, and generation may use account credits.

Mitigation: Avoid sending confidential content unless the service's data terms are acceptable; use --dry-run to review the payload and cost estimate before generation.

Risk: Login stores a reusable API key in the local CLI configuration.

Mitigation: Keep the configuration private and rotate or revoke the key from the account dashboard if it is exposed.

## Reference(s):

- [CLI project link declared in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON, Shell commands]

**Output Format:** [Generated speech audio with a JSON result or task status, invoked through shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs may return a task ID before the audio is ready.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
