## Description:

Alibaba Bailian qwen3-tts text-to-speech. Choose from curated system voices (including dialects) or design a custom voice from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill through an agent to generate speech with Alibaba Bailian qwen3-tts, selecting a system voice or describing a custom voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rated the release benign with medium confidence but did not establish the external CLI's connection to its stated text-to-speech purpose.

Mitigation: Before installing or authenticating, review the CLI source and confirm you are comfortable with the external login and authentication flow.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio asset and a JSON response containing result URLs or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task identifier; the --save option downloads the generated asset.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
