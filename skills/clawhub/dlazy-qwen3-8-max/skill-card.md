## Description:

Uses dLazy's Qwen 3.8 Max service for reasoning, coding, and analysis with text and image inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can use this skill to request reasoning, code, and long-context analysis from dLazy's hosted Qwen model, optionally with image inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached local media may be sent to dLazy's cloud services.

Mitigation: Review content and attachments before submission; avoid sharing sensitive information unless authorized.

Risk: Logging in may store an API key on the local machine.

Mitigation: Use per-invocation credentials when local persistence is undesirable, and rotate or revoke exposed keys.

Risk: The English skill instructions describe a different video-generation workflow than the advertised Qwen model.

Mitigation: Confirm the intended dLazy command with the user and CLI help before executing an unrelated workflow.

## Reference(s):

- [dLazy CLI repository (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code]

**Output Format:** [JSON response containing generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; asynchronous requests may return a task ID instead of immediate content.]

## Skill Version(s):

1.2.19 (source: ClawHub release metadata; bundled skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
