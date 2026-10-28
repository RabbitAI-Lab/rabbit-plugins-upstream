## Description:

Clone a reusable custom voice for Qwen3-TTS by uploading a clean voice sample.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to create a reusable custom voice from a clean sample for later Qwen3-TTS synthesis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The voice sample is uploaded to dLazy for processing.

Mitigation: Use only a sample you have permission to clone and are comfortable uploading to dLazy.

Risk: Login saves an API key in the local CLI configuration, and requests may consume credits.

Mitigation: Protect the local configuration, rotate or revoke the key when needed, and use --dry-run to inspect the estimated cost before a request.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [CLI invocation and JSON response with output references or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a custom voice for later TTS use; asynchronous runs may initially return a task ID.]

## Skill Version(s):

1.3.34 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
