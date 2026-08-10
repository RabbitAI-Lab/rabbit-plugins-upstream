## Description:

Deep Research Forge helps agents plan and produce evidence-led deep research, competitive analysis, concept lineage, decision briefs, reusable research assets, and retrospectives, with optional parallel research lanes for complex topics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fxbin](https://clawhub.ai/user/fxbin)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, developers, and other agent users use this skill to turn broad or messy questions about products, companies, people, technologies, markets, policies, or cultural phenomena into traceable research outputs and action-oriented briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security verdict is suspicious because the skill may coordinate multiple agents, persist research or iteration state, and expose local maintainer scripts.

Mitigation: Review the skill and its scripts before deployment, require explicit confirmation for parallel research, and monitor any file-changing improvement loop.

Risk: The retrospective iteration workflow can run a user-provided behavior command.

Mitigation: Do not run the iteration workflow or --behavior-command with untrusted commands; inspect command arguments and expected output paths first.

Risk: Research outputs can contain incorrect or misleading guidance when source quality, recency, or conflicts are weak.

Mitigation: Use the skill's evidence ledger, claim-level citation protocol, conflict resolution, and quality gates before relying on conclusions.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/fxbin/skills/tree/main/deep-research-forge)
- [ClawHub skill page](https://clawhub.ai/fxbin/skills/deep-research-forge)
- [Research protocol](references/research-protocol.md)
- [Methodology routing index](references/methodology-routing-index.md)
- [Multi-agent protocol](references/multi-agent-protocol.md)
- [Source strategy](references/source-strategy.md)
- [Quality gates](references/quality-gates.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance, configuration, shell commands]

**Output Format:** [Markdown reports and briefs, JSON evidence ledgers, structured plans, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include evidence IDs, citation maps, confidence labels, conflict notes, quality scorecards, and route-specific research templates.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
