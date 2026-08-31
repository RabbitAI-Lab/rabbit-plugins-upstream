## Description:

Generates 1-22 second sound effects from text prompts using the ElevenLabs text-to-sound model through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to generate short foley, ambience, alert, and game sound effects from text prompts via the hosted dLazy API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and optional media files are sent to dLazy cloud services for generation.

Mitigation: Avoid submitting private or sensitive media unless the user explicitly intends to upload it to dLazy.

Risk: The skill depends on a stored or environment-provided dLazy API key.

Mitigation: Use a scoped, revocable key and rotate or revoke it from the dLazy dashboard when access is no longer needed.

Risk: A global CLI install persists tooling on the host system.

Mitigation: Use the pinned npx @dlazy/cli@1.2.3 invocation when a non-global install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI can return generated asset URLs, saved output files, or asynchronous task identifiers.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
