## Description:

Helps agents audit and improve context relevance, redundancy, token budgets, and decay using a four-step workflow and a local budget calculator.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory: All rights reserved

## Use Case:

Developers and agent builders use this skill to diagnose long-context failures and token costs, refine retrieval and memory, and review context blocks with a local budget and redundancy report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation and theory may be reused under the code license by mistake.

Mitigation: Review the scoped licensing terms before redistributing text; the artifact states MIT applies only to Python code.

Risk: Approximate token estimates may understate or overstate actual context costs.

Mitigation: Check important budgets against the target model's token counts and review the audit findings manually.

## Reference(s):

- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/context-engineering)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Markdown guidance and plain-text audit report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local CLI estimates tokens per context block, window usage, and cross-block redundancy.]

## Skill Version(s):

1.0.3 (source: ClawHub release; artifact frontmatter says 1.1.0 and manifest says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
