## Description:

Use when designing, writing, building, diagnosing, or revising NodeCoda Source through the authenticated NodeCoda MCP service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nodecoda](https://clawhub.ai/user/nodecoda)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and workflow builders use this skill to author versioned NodeCoda Source, build it into Dify workflow artifacts, interpret diagnostics, and iterate on workflow generation through NodeCoda MCP or CLI paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends .ncoda Source to NodeCoda or try.nodecoda.com for workflow builds.

Mitigation: Do not put secrets in Source or prompts; use environment-based credentials and review source content before building.

Risk: Generated Dify workflows can include model providers, tools, knowledge retrieval, and HTTP endpoints that affect runtime behavior.

Mitigation: Review generated workflow providers, tools, HTTP endpoints, and external dependencies before deploying in Dify.

Risk: Build commands can write workflow artifacts and build records beside the source file.

Mitigation: Inspect generated files and version-control diffs before sharing or deploying artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nodecoda/skills/nodecoda-workflow)
- [Server-resolved GitHub provenance](https://github.com/nodecoda/nodecoda-skill/tree/main/skills/nodecoda-workflow)
- [References index](references/README.md)
- [NodeCoda Workflow Language reference](references/language-reference.md)
- [NodeCoda MCP Workflow Build Contract](references/mcp-contract.md)
- [NodeCoda Public Service Procedure](references/public-service.md)
- [Target capability matrix for dify-1.16-graphon-0.6](references/target-capabilities.md)
- [Diagnostics and repair map](references/diagnostics-map.md)
- [Failure modes and handling](references/failure-modes.md)
- [NodeCoda website](https://www.nodecoda.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with NodeCoda Source snippets, JSON tool calls, shell commands, and file output paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce .ncoda source, Dify workflow artifacts, build records, diagnostics summaries, and review guidance.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
