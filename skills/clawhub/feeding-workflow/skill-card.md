## Description:

This document-only skill guides AI teams, RAG maintainers, and knowledge-base operators through a five-step workflow for registering, verifying, rewriting, partitioning, and acknowledging knowledge inputs so factual claims carry source, applicability, and governing-standard context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and knowledge operations teams use this skill to turn loose files, URLs, notes, screenshots, or meeting records into verified feed packages for knowledge bases, RAG systems, and multi-agent teams. It emphasizes official-source checking, sensitive-data screening, public/private partitioning, and clear receipts for each ingestion pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags provenance and compliance risk because the artifact instructs agents to rewrite third-party content without retaining third-party attribution.

Mitigation: Require source URLs, authors or publishers, dates, and licensing notes for third-party material before adding it to any knowledge base or RAG corpus.

Risk: The security evidence recommends review before installation despite finding no executable code or credential access.

Mitigation: Review the package text and keep execution disabled unless future versions add scripts, commands, network actions, or dependency installation steps.

## Reference(s):

- [喂料包模板.md](references/喂料包模板.md)
- [喂料纪律.md](references/喂料纪律.md)
- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/feeding-workflow)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown with structured tables, checklists, and concise receipt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Document-only workflow; factual claims should retain source, applicability, and governing-standard fields.]

## Skill Version(s):

1.0.0 (source: frontmatter, manifest, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
