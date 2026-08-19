## Description:

Build or refresh the CGIS code graph for this repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zaebee](https://clawhub.ai/user/zaebee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build or refresh a local CGIS semantic graph for a repository so code graph tools can answer structural questions about Python and TypeScript code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill indexes the selected repository into a local graph.db file, which can include private or sensitive code structure.

Mitigation: Review the selected source path before running the skill on sensitive repositories and keep graph.db out of version control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zaebee/skills/ingest)
- [Server-resolved GitHub provenance](https://github.com/zaebee/codegraph-brain/tree/main/plugin/skills/ingest)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports ingestion results, unresolved-edge interpretation, unsupported language coverage, and graph.db maintenance guidance.]

## Skill Version(s):

0.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
