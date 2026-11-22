## Description:

Build and query AST summaries and call graphs for codebases when exploring project structure, finding definitions, tracing call chains, understanding imports, or navigating unfamiliar code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sg345662365-oss](https://clawhub.ai/user/sg345662365-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use CodeGraph to build a local structural cache for Python, JavaScript, TypeScript, and Ruby projects, then query functions, classes, imports, file summaries, calls, callers, and project statistics before reading or modifying code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the analyzer writes a local .code-graph.json cache containing structural information about the selected project.

Mitigation: Use --output to place the cache deliberately, review the cache before sharing it, and avoid running it on projects whose structure should not be persisted.

Risk: The analyzer scans Ruby files in addition to the Python and JavaScript/TypeScript support emphasized in the skill description.

Mitigation: Use --exclude to omit directories or file areas that should not be scanned.

## Reference(s):

- [ClawHub CodeGraph skill page](https://clawhub.ai/sg345662365-oss/skills/codegraph)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON query output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or reads a local .code-graph.json cache unless a custom --output path is supplied.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
