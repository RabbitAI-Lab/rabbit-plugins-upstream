## Description:

Generates videos with ByteDance's Seedance 2.0 Fast model from text prompts and optional image, video, audio, first-frame, or last-frame references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Seedance 2.0 Fast video-generation API from an agent workflow, using text prompts and optional image, video, audio, first-frame, or last-frame inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and user-selected media can be sent to dLazy hosted services, and authentication can store an API key locally.

Mitigation: Review the hosted-service data flow before use, avoid submitting sensitive media unless approved, rotate or revoke the dLazy API key when needed, and use npx or review the pinned CLI package if avoiding a global install is preferred.

Risk: The skill depends on external dLazy API and media-storage endpoints for generation and result hosting.

Mitigation: Use it only in environments where calls to api.dlazy.com and files.dlazy.com are permitted and monitor service errors, authentication failures, and quota or credit failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [JSON responses with generated media URLs, optional downloaded files, and Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task identifiers when no-wait mode is used; generated assets are hosted through dLazy media storage unless saved locally.]

## Skill Version(s):

1.3.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
