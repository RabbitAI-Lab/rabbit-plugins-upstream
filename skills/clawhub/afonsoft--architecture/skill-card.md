## Description:

Routes repository architecture documentation, decisions, and diagrams to the appropriate authoring tools and coordinates a final gap audit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create and maintain architecture decision records, design documents, and diagrams for a repository, then hand off an evidence-backed gap audit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An optional diagram skill discovered inside the repository could be untrusted and run code when used.

Mitigation: Review before installation; use a runtime that does not trust repository-local skills, or manually approve the resolved archify path before running Node commands.

## Reference(s):

- [ClawHub architecture release](https://clawhub.ai/afonsoft/skills/architecture)
- [Author-provided project link](https://github.com/afonsoft/skills)
- [Architecture inventory contract](references/architecture-inventory.md)
- [Gap-analysis handoff](references/gap-audit-handoff.md)
- [Optional archify diagram engine](https://github.com/tt-a1i/archify)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Code, Guidance]

**Output Format:** [Architecture documents, ADRs, diagram sources and exports, and audit guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Artifacts are organized under docs/architecture/; interactive HTML diagrams require an already installed optional engine.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
