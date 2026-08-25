## Description:

Automates parallel dispatching of independent development tasks with structured input/output, error recovery, and multi-format support for workflow efficiency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-focused teams use this skill to dispatch two or more independent development tasks that can proceed without shared state or sequential dependencies, then collect structured results or error states.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad read and shell execution automation may access files or run commands outside the intended dispatching workflow.

Mitigation: Limit activation to explicit parallel-agent dispatch tasks and require user approval before shell commands or broad file reads.

Risk: Credential handling is vague for a skill that may initialize API connections or use external services.

Mitigation: Document required credentials, store secrets in environment variables or platform secret stores, and avoid logging sensitive values.

Risk: The artifact includes unsupported security assurances and broad data-security claims.

Mitigation: Remove or substantiate security claims before relying on the skill in production.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dispatching-parallel-agents)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON-style structured results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include execution status, result metadata, and error details for dispatched tasks.]

## Skill Version(s):

1.0.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
