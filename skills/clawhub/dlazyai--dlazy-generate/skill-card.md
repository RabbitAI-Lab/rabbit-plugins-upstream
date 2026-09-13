## Description:

A comprehensive generation skill that can generate images, videos, and audio by automatically selecting the appropriate dlazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to route image, video, and audio generation requests to an appropriate dLazy CLI model and run the corresponding command. It supports multimodal generation workflows that may use prompts, local media inputs, and command piping between generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media may be sent to dLazy's hosted API and media storage.

Mitigation: Review the generated dlazy command before execution and avoid passing private media unless uploading it to the dLazy service is intended.

Risk: Broad trigger phrases and auto-execution behavior may run generation requests without enough user confirmation.

Mitigation: Confirm the requested media type, selected model, and command arguments before running dlazy commands.

Risk: Use of the hosted service can consume dLazy credits and depends on a valid API key.

Mitigation: Prefer per-run API keys where practical, rotate or revoke keys from the dLazy dashboard when needed, and make credit use explicit before long or costly generation runs.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with inline shell commands and dlazy CLI JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media results are returned as hosted URLs from the dLazy service when commands complete successfully.]

## Skill Version(s):

1.3.14 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
