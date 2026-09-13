## Description:

詹明明·口播稿写作 helps an agent collaborate on Chinese talking-head scripts by selecting script type, assembling real content units, and drafting section by section rather than producing a one-shot script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and writing assistants use this skill to co-create knowledge-payment talking-head scripts from configured style rules, content units, feedback, and prior drafts. It supports script-form selection, outline assembly, hook and body drafting, evidence-visual planning, and material collection lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured vault files and automatic memory writebacks can have durable influence over future drafts.

Mitigation: Keep the vault private and trusted, review or disable automatic writeback, and require explicit confirmation before storing feedback or promoting derived cases.

Risk: The skill may read configured vault materials and write drafts, rules, memories, and content units.

Mitigation: Install only for the intended private Chinese writing workflow and review generated drafts and stored changes before reuse or publication.

## Reference(s):

- [概念型口播.md](references/概念型口播.md)
- [规则卡.md](references/规则卡.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-script)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Chinese Markdown script drafts with hooks, evidence visuals, material collection checklists, and concise collaboration prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read configured vault materials and write drafts, feedback-derived rules, memories, and content units when enabled.]

## Skill Version(s):

0.2.10 (source: server release metadata; artifact frontmatter reports 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
