## Description:

Use a repository’s indexed code graph to answer questions about symbol relationships, such as callers, callees, routes, dependency wiring, reachability, and change impact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nithin554](https://clawhub.ai/user/nithin554)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to answer questions about how symbols connect across an indexed repository, including call paths, routes, dependency injection, and change impact. It helps choose graph analysis for relationship questions and plain search or file reading for questions about text or one file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions use unpinned package versions, so later installs may resolve to different releases.

Mitigation: Review the setup commands and pin package versions before installing.

Risk: A scanner reports a possible mismatch between the skill’s purpose and a Cursor configuration action.

Mitigation: Inspect the Cursor configuration step and apply it only if it matches your intended setup.

Risk: The security analysis is incomplete, with medium confidence and unresolved references.

Mitigation: Review the skill and its references before installing, and treat the scan result as incomplete.

## Reference(s):

- [Code Crawler project site](https://nithin554.github.io/code-crawler/)
- [ClawHub release page](https://clawhub.ai/nithin554/skills/code-crawler)
- [Tool reference](artifact/reference/tools.md)
- [Edge semantics reference](artifact/reference/edge-semantics.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Concise Markdown analysis with code symbol references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Repository-specific; results depend on the indexed code and its freshness.]

## Skill Version(s):

0.1.82 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
