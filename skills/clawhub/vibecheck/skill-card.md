## Description:

Vibecheck helps developers work on psyb0t/vibecheck, an early Go service scaffold for typed classification, scoring, and policy decisions backed by TypeSafe Jev.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, review, and verify the Vibecheck repository's policy engine, Jev adapter, persistence, HTTP API, MCP surface, Docker image, and tests while respecting the scaffold's current implementation boundary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repeatable or trusted runs may drift if they use the `latest` Docker image tag.

Mitigation: Use a pinned Vibecheck image tag or digest in repeatable environments.

Risk: Provider keys, API tokens, credentials, or real request data could be exposed through tracked files or logs.

Mitigation: Keep secrets and real request data out of prompts, examples, fixtures, tracked files, and logs.

Risk: The current scaffold does not yet implement the policy compiler, TypeSafe Jev adapter, persistence, HTTP API, or MCP server.

Mitigation: Verify each endpoint, tool, configuration value, or response field against implemented code and behavioral tests before relying on it.

## Reference(s):

- [Vibecheck setup and current boundary](references/setup.md)
- [Vibecheck ClawHub skill page](https://clawhub.ai/psyb0t/skills/vibecheck)
- [Vibecheck project homepage declared by the skill](https://github.com/psyb0t/vibecheck)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and code or configuration edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require Docker and Make; current API, runtime provider, and MCP surfaces must be verified before use.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
