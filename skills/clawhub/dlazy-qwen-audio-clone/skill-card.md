## Description:

Helps agents submit a voice sample to dLazy's hosted Qwen voice-cloning service for a custom voice usable in later text-to-speech requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other external users can ask an agent to create a reusable custom voice from an authorized voice sample for subsequent text-to-speech use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are sent to dLazy's hosted service and may contain sensitive biometric data.

Mitigation: Upload only voices with the speaker's permission and review the service's retention and deletion terms first.

Risk: Authentication keys can remain saved in the local CLI configuration.

Mitigation: Prefer a per-invocation DLAZY_API_KEY, or revoke and rotate a saved key when no longer needed.

Risk: The documented output and example command contain copy-paste errors.

Mitigation: Check the CLI's current help and validate the actual response before relying on those examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI source (declared in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with CLI examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice-cloning requests may return a task ID or hosted result links; the documented example response is unreliable.]

## Skill Version(s):

1.3.27 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
