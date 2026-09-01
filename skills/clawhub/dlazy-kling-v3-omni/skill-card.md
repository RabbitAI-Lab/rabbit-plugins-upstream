## Description:

Versatile video generation with Kling v3 Omni, supporting prompt and media inputs for dynamic video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy Kling v3 Omni CLI for text-to-video and image-to-video generation, including asynchronous generation and optional result download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media inputs are sent to dLazy services for generation.

Mitigation: Use the skill only with media and prompts you are comfortable uploading to dLazy, and review dLazy service terms before use.

Risk: A persistent API key may remain in the local dLazy CLI configuration on shared machines.

Mitigation: Prefer per-invocation DLAZY_API_KEY on shared systems, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party CLI and hosted generation endpoints.

Mitigation: Confirm the pinned CLI package and publisher before installation, and use dry-run or async status checks where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI can return hosted media URLs, task identifiers for asynchronous jobs, and optional saved local result files.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
