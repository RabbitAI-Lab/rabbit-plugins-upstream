## Description:

Uses the dLazy-hosted Qwen model for reasoning, code generation, and analysis of text and images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask the dLazy-hosted Qwen model to reason through complex questions, generate code, or analyze text and images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service.

Mitigation: Share only content you are comfortable sending to a third-party service; review local paths before submission.

Risk: A dLazy API key may be saved in local CLI configuration.

Mitigation: Protect the key and rotate or revoke it through the dLazy dashboard if needed.

Risk: Using the skill runs a third-party CLI.

Mitigation: Review the package before installing; use the pinned npx invocation if a global install is undesirable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [JSON response containing generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of immediate output.]

## Skill Version(s):

1.2.27 (source: ClawHub release; bundled skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
