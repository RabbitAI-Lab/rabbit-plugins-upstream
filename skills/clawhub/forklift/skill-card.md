## Description:

Forklift expert is a bilingual agent skill for forklift and industrial truck questions covering brands, specifications, selection, troubleshooting, parts, maintenance, used-equipment evaluation, standards, regulations, market data, and sales rankings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangpf6698](https://clawhub.ai/user/yangpf6698)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and operations teams use this skill to answer forklift questions, compare equipment, plan maintenance, troubleshoot faults, check standards and regulations, and format market or sales summaries in Chinese or English.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External searches for current forklift specifications, standards, sales, or market data may disclose confidential procurement plans, internal incidents, customer names, or regulated data.

Mitigation: Avoid sensitive details in search-backed prompts; for confidential work, ask the agent to rely on local reference files or confirm before searching.

Risk: Forklift safety, legal, purchasing, or repair guidance can be time-sensitive or unsuitable for a specific site.

Mitigation: Verify outputs against official sources, manufacturer documentation, or a qualified professional before acting.

Risk: Model specifications, standards status, sales rankings, and market data can change after the local reference files were written.

Mitigation: Use dated web lookup and authoritative sources for current figures, and include the retrieval date in the answer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangpf6698/skills/forklift)
- [ClawHub publisher profile](https://clawhub.ai/user/yangpf6698)
- [README](artifact/README.md)
- [Usage guide](artifact/usage-guide.md)
- [Bilingual glossary](artifact/bilingual-glossary.md)
- [Standards reference](artifact/standards.md)
- [Standard retrieval guide](artifact/standard-retrieval.md)
- [Safety and regulation reference](artifact/safety-regulation.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown prose, tables, checklists, and occasional ASCII charts or shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual output follows the user's language; current specifications, standards, market data, and sales questions may use web lookup.]

## Skill Version(s):

2.0.5 (source: ClawHub release metadata; artifact frontmatter reports 2.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
