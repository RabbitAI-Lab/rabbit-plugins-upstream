## Description:

Provides 18 local, deterministic development tools over stdio MCP for repository mapping, architecture and change analysis, verification, code review, security checks, release readiness, and workflow support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to map unfamiliar repositories, review architecture and code changes, track verification evidence, and check secrets, dependencies, or release readiness. Execution and write operations require explicit opt-in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Linked workflow reads on untrusted repositories may expose private text, and incomplete checks may appear clean.

Mitigation: Avoid workflow reads on untrusted repositories until link containment is fixed, or isolate the tool from private files. Do not treat empty secret findings or configuration all-clear flags as proof that checks completed; keep execution disabled unless the project and adapters are trusted.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-dev-mcp)
- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-dev-mcp)
- [Tool reference](references/tools.md)
- [Architecture contract](references/architecture-contract.md)
- [Adapter reference](references/adapters.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Structured JSON tool responses with concise text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [File and line evidence where available; findings can be UNKNOWN when evidence or required tools are unavailable.]

## Skill Version(s):

0.2.7 (source: frontmatter; confirmed by server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
