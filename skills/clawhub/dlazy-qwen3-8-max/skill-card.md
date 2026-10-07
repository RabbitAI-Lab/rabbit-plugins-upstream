## Description:

Generates reasoning, code, and long-context responses from text prompts and optional images through dLazy's Qwen 3.8 Max service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users use this skill for complex reasoning, coding assistance, and long-context analysis with text prompts and optional images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local images are sent to dLazy's cloud service.

Mitigation: Review inputs before submission and avoid sending sensitive content without approval.

Risk: The dLazy CLI requires an API key that may be saved locally.

Mitigation: Protect the key and rotate or revoke it if exposed.

Risk: Using a third-party CLI adds installation and dependency exposure.

Mitigation: Use the pinned on-demand npx invocation or review the CLI source before a global install.

## Reference(s):

- [dLazy CLI project (skill metadata homepage)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [JSON response containing generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID; generated results may include hosted URLs.]

## Skill Version(s):

1.2.21 (source: ClawHub release evidence; skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
