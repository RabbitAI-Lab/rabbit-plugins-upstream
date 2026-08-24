## Description:

Searches recent top-conference and top-journal Agentic AI research, screens papers through the H=(E,T,C,S,L,V)+P framework, produces a human-readable literature review, and can optionally build a local project wiki after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and researchers use this skill to investigate a chosen Agentic AI subfield, screen recent venue results with the H framework, and receive a readable Markdown literature review. With explicit confirmation, the skill can convert that review into local wiki pages inside the current project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can browse the web and write local review files as part of its research workflow.

Mitigation: Install it only for the disclosed literature-review use case, and review the generated sources and Markdown before relying on the results.

Risk: Optional wiki conversion writes local files and the helper scripts expose a manual root option.

Mitigation: Approve wiki conversion only after checking the absolute paths shown by the agent and keeping them inside the current project's .wiki-creator directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/neuhanli/skills/agentic-ai-research)
- [wiki-creator README](wiki-creator/README.md)
- [wiki-creator query mode](wiki-creator/references/query-mode.md)
- [wiki-creator page authoring](wiki-creator/references/page-authoring.md)
- [wiki-creator schema guide](wiki-creator/references/schema-guide.md)
- [wiki-creator cascade update](wiki-creator/references/cascade-update.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown literature review, optional local wiki Markdown pages, and JSON or status output from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wiki writing is optional, confirmation-gated, and intended to stay under a project-local .wiki-creator directory.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
