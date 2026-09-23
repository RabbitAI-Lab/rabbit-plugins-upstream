## Description:

AI KEY·口播稿写作 helps agents co-write Chinese talking-head scripts for knowledge creators through script-type selection, content-unit assembly, and section-by-section collaboration rather than one-shot drafting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and operators use this skill to develop Chinese knowledge-commerce talking-head scripts, hooks, title inputs, evidence-shot notes, and material collection checklists from local content sources. It supports collaborative drafting where the agent asks for real materials and confirms each section before final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read and update local content, feedback, and memory stores during drafting.

Mitigation: Review or disable automatic feedback, content-library, and memory writeback behavior before installation when retained corrections, preferences, or draft-derived material are not desired.

Risk: Drafting quality depends on configured local vault files and recent feedback artifacts that may be absent or stale.

Mitigation: Confirm required local paths are present before use, and require the agent to report missing inputs instead of substituting memory or assumptions.

Risk: The workflow is designed around real creator materials, so fabricated examples or numbers could mislead the user or audience.

Mitigation: Require user-provided source material for personal stories, cases, and metrics, and stop to ask for details when the supporting material is missing.

## Reference(s):

- [规则卡](artifact/references/规则卡.md)
- [概念型口播](artifact/references/概念型口播.md)
- [ClawHub skill listing](https://clawhub.ai/iamzifei/skills/aikey-script)
- [AI KEY README upgrade note](https://github.com/iamzifei/aikey#老用户升级zmm-已改名为-ai-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Configuration]

**Output Format:** [Markdown prose, structured script drafts, inline checklists, and occasional shell command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write draft files and update local content or memory stores when the host workspace provides the configured vault paths.]

## Skill Version(s):

0.4.4 (source: server release metadata; artifact frontmatter says 0.4.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
