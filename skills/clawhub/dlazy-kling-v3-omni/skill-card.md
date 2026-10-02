## Description:

Helps agents generate Kling V3 Omni videos from prompts and optional reference media through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from text prompts and optional image or video references, then retrieve the generated asset link or save the result locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media can be sent to the dLazy service.

Mitigation: Review prompts and file paths before use; only submit media approved for third-party processing.

Risk: The CLI can store an API key locally.

Mitigation: Protect the local credential and rotate or revoke it if exposed.

Risk: Installing the third-party CLI and using --save can affect the local environment.

Mitigation: Review the pinned package before installation and choose an appropriate output path.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI source (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text guidance and CLI JSON responses with generated asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID; --save can download an asset to a selected local path.]

## Skill Version(s):

1.3.23 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
