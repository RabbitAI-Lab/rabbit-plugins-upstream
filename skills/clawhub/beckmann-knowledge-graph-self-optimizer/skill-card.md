## Description:

Iterative self-optimization for knowledge graphs in 5 phases with 3 review gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[matthiasbeckmann987-spec](https://clawhub.ai/user/matthiasbeckmann987-spec)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge-graph maintainers use this skill to run a guided, review-gated optimization cycle over an existing graph. It helps generate graph overviews, topic selections, new subgraphs, bridge relations, and a merged optimized graph artifact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private graph content may be exposed when prompt templates and graph-derived files are shared with an external AI model.

Mitigation: Use trusted graph files, treat generated overview, split, report, relation, and merged files as sensitive, and use an approved model or local workflow for private data.

Risk: Untrusted graph JSON opened in browser-based HTML tools could present unsafe graph-supplied text if rendering is not hardened.

Mitigation: Open only graph files from trusted sources, or harden the HTML tools to escape graph-supplied text before use with untrusted data.

Risk: The final rename and cleanup step can overwrite or remove the prior graph state.

Mitigation: Keep backups before renaming graph_vNEXT_optimized.json to graph.json and before cleanup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/matthiasbeckmann987-spec/skills/beckmann-knowledge-graph-self-optimizer)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, JSON, text, configuration]

**Output Format:** [Markdown instructions and prompt templates that guide creation of JSON, Markdown, and text files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-operated offline HTML tools, trusted graph inputs, and explicit review-gate decisions before merge steps.]

## Skill Version(s):

1.0.0 (source: server release metadata, SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
