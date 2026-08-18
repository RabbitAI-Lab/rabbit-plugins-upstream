## Description:

Use when a question is about how code connects rather than what a single file says: finding every caller of a symbol, judging whether a rename or signature change is safe, tracing an execution path, mapping an unfamiliar module, or checking architectural drift.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zaebee](https://clawhub.ai/user/zaebee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use CGIS to answer structural codebase questions with a deterministic code graph, including caller impact, execution flow, symbol location, module structure, reachability, and architecture drift checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CGIS may create or update a local graph.db from the source paths selected during ingestion.

Mitigation: Point ingestion at the intended source directory rather than the whole repository, especially when dependency, generated, or virtual environment folders are present.

Risk: A stale graph can produce confident but outdated structural answers after code changes.

Mitigation: Re-run cgis_ingest after substantial changes so the graph reflects the current source tree.

Risk: Static graph results can miss dynamic dispatch, registries, framework decorators, and languages outside the documented Python and TypeScript coverage.

Mitigation: Treat empty impact results as no static callers found, check unresolved-edge levels with cgis_validate when relevant, and inspect unsupported language files directly.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/zaebee/codegraph-brain/tree/main/plugin/skills/cgis)
- [Guardian README section](https://github.com/zaebee/codegraph-brain#-guardian-graph-aware-code-review)
- [ClawHub skill page](https://clawhub.ai/zaebee/skills/cgis)
- [Publisher profile](https://clawhub.ai/user/zaebee)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline tool and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include code graph query guidance, source coverage notes, and static-analysis caveats.]

## Skill Version(s):

0.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
