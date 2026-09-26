## Description:

Develop and verify psyb0t/vibecheck, a Go service for typed classification, scoring, and policy decisions backed by TypeSafe Jev.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill while implementing, reviewing, testing, and documenting the Vibecheck policy engine, TypeSafe Jev adapter, persistence layer, REST API, MCP server, Docker image, and related repository workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to run Docker and Make commands or use a Vibecheck Docker image.

Mitigation: Review commands before execution, run them in the intended repository, and prefer a pinned release tag or image digest instead of latest for repeatable use.

Risk: Real TypeSafe credentials, API tokens, encryption keys, request data, or provider responses could be exposed if placed in tracked files, prompts, examples, fixtures, or logs.

Mitigation: Keep real credentials and sensitive data in gitignored local environment files, and use local fakes for tests when possible.

Risk: The skill concerns a decision service, so incorrect route, MCP tool, policy, or configuration claims could mislead downstream integrations.

Mitigation: Verify routes, MCP tools, response fields, and behavior against the implementation and behavioral tests before documenting or using them.

## Reference(s):

- [Vibecheck setup and current boundary](references/setup.md)
- [Vibecheck repository](https://github.com/psyb0t/vibecheck)
- [Vibecheck ClawHub skill page](https://clawhub.ai/psyb0t/skills/vibecheck)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include repository-specific verification steps, Make targets, Docker commands, endpoint names, MCP tool names, and configuration guidance.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
