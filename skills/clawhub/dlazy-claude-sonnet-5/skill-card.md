## Description:

Runs prompts through dLazy's hosted Claude Sonnet 5 CLI for reasoning, code generation, complex tool orchestration, with support for text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to send prompts and optional image or video inputs to dLazy's hosted Claude Sonnet 5 service and receive generated responses for reasoning, coding, and planning tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided media files are sent to dLazy's hosted service.

Mitigation: Review content sensitivity before use and avoid sending confidential or regulated data unless covered by the user's organization policy and dLazy terms.

Risk: The skill requires a dLazy API key that may be stored in the local CLI configuration or passed through an environment variable.

Mitigation: Use per-user credentials, restrict local config access, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Use depends on installing or invoking the pinned dLazy npm CLI.

Mitigation: Install the pinned package version from the declared metadata and review the linked package or source before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [JSON envelope containing generated output values; content may be text, Markdown, or code.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async invocations may return a generateId for polling; optional saved outputs are written through the dLazy CLI.]

## Skill Version(s):

1.2.12 (source: server release metadata; artifact frontmatter reports 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
