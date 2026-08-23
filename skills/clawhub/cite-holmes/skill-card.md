## Description:

Cite Holmes guides an agent through scoped deep research, iterative source discovery, citation verification, and confidence-graded reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT

## Use Case:

Researchers, analysts, developers, and other external users can use this skill when they need a sourced research report, fact check, citation audit, or comparison that separates verified, partial, unreachable, invalid, and unverified references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online verification contacts reference URLs and may create web activity while checking sources.

Mitigation: Use QUICK mode, offline verification, or explicit task scoping when lower web activity is required.

Risk: Broad prompts may trigger open-ended research and multiple searches.

Mitigation: Ask the agent to use a constrained mode, scope, timeframe, and search budget before research begins.

Risk: Mechanical checks can confirm reachability and metadata but cannot guarantee that a source semantically supports a claim.

Mitigation: Keep semantic support review in the workflow and route unreachable, invalid, or unverified references to human review rather than treating them as supported evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Publisher profile](https://clawhub.ai/user/docsor1212)
- [Report template and reference schema](artifact/references/report-template.md)
- [Search strategies](artifact/references/search-strategies.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with citation tables, confidence grades, reference-verification summaries, and optional shell commands for mechanical reference checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports QUICK and FULL research modes; verifier output can include verified, partial, unreachable, invalid, and unverified reference states.]

## Skill Version(s):

1.1.1 (source: artifact/SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
