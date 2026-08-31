## Description:

Video replicate tool: extracts the first frame and audio from a source video, runs video understanding for a prompt, and returns a Seedance 2.0 replicate bundle with first frame, audio, and video outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted video-replication workflow from an agent, using a source video to generate a Seedance 2.0-style replicate bundle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos, prompts, and generated outputs are sent through dLazy's hosted service.

Mitigation: Use only media appropriate for dLazy processing and confirm hosted-service handling is acceptable before invocation.

Risk: Logging in can store a dLazy API key in the local CLI configuration.

Mitigation: Prefer the pinned npx command when avoiding a persistent global CLI, and rotate or revoke the dLazy API key from the dashboard if needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown instructions with bash examples and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs, saved result assets, or a generateId for asynchronous polling.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
