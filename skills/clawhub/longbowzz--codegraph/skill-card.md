## Description:

Generate source-linked Mermaid diagrams and long-form CodeWalkthrough explainer pages from a codebase, with diff-aware review mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longbowzz](https://clawhub.ai/user/longbowzz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use CodeGraph to map code flows to source locations, review changes with diagrams, and create interactive walkthrough pages that explain code to readers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports a potential file-handling concern: files outside the intended repository could be embedded in an output.

Mitigation: Keep source references within the intended repository and inspect generated HTML for embedded source before sharing it.

Risk: The security scan was incomplete, so it could not establish that every artifact file is safe.

Mitigation: Review the skill files and generated outputs before installing or using the release.

Risk: Structural validation cannot establish that diagram labels accurately describe source behavior.

Mitigation: Check each source-linked node, edge, and explanation against the referenced code before relying on the diagram.

## Reference(s):

- [CodeWalkthrough reference](references/walkthrough.md)
- [Mermaid vendored source release](https://registry.npmjs.org/mermaid/-/mermaid-11.12.0.tgz)
- [CodeGraph on ClawHub](https://clawhub.ai/longbowzz/skills/codegraph)

## Skill Output:

**Output Type(s):** [Mermaid diagrams, JSON, HTML, Markdown]

**Output Format:** [Mermaid source with JSON source-location maps, plus interactive single-page HTML visualizations or walkthroughs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are saved as repository files; graph outputs link diagram elements to source locations.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
