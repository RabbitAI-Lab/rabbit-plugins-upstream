## Description:

Analyzes agent transcripts or context inventories, estimates token use across seven categories, identifies context pollution and compaction risks, and recommends layered ways to retain, structure, reference, or discard information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use the skill to understand how a provided agent conversation spends its context budget, locate potential context pollution, and plan what to preserve when context is compacted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provided transcripts may contain secrets or sensitive content.

Mitigation: Share only material intended for analysis and remove secrets beforehand.

Risk: Token totals and content classifications are estimates.

Mitigation: Treat findings as approximate and verify important classifications against the provided source.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/z-zihan/skills/context-budget-analyzer)
- [Project homepage](https://github.com/z-Zihan/awesome-skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with estimated token-budget tables, evidence-based findings, a compaction preview, and recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only analysis; token totals and classifications are estimates.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
