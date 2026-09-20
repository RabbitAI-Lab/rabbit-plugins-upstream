## Description:

StackAI (stack-ai.com). Use this skill for StackAI requests that read, create, or update data through the OOMOL-connected StackAI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect StackAI connector schemas, run deployed StackAI flows with JSON variables, and retrieve metadata for previously started StackAI runs through the OOMOL CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance may lead an agent to run remote installer scripts without verification.

Mitigation: Review setup commands before installation, prefer official documentation with pinned releases or verification steps, and run StackAI actions only after the oo CLI is intentionally installed and authenticated.

Risk: The skill can run StackAI write actions such as deployed flow execution.

Mitigation: Confirm the exact payload and expected effect with the user before running actions marked as write.

## Reference(s):

- [StackAI homepage](https://www.stack-ai.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [StackAI skill page](https://clawhub.ai/oomol/skills/oo-stack-ai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to inspect live connector schemas before action execution and to confirm write or destructive actions with the user.]

## Skill Version(s):

1.0.4 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
