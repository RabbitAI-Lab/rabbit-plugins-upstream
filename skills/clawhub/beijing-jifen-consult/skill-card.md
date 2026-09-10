## Description:

Helps users check Beijing points-settlement eligibility, simulate scores, interpret results, and discuss planning using a bundled local HTML simulator or constrained text guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vincent51-commits](https://clawhub.ai/user/vincent51-commits)

### License/Terms of Use:

MIT No Attribution License (MIT-0)

## Use Case:

External users use this skill to gather verified personal facts, operate or interpret the local Beijing points-settlement simulator, understand official-rule references, and plan next steps without treating the result as an official decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal settlement facts entered into the bundled simulator may persist in the local browser profile through localStorage.

Mitigation: Use a trusted non-shared browser profile and clear the page records or browser storage after use.

Risk: The simulator and guidance are non-official and may become inaccurate if policy, scoring rules, or official review standards change.

Mitigation: Verify important inputs and outcomes against official Beijing channels or qualified professionals before relying on them.

Risk: Text guidance can be mistaken for a computed result when the HTML page is unavailable.

Mitigation: Use text mode only for field clarification and data checking unless the user supplies page-calculated results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vincent51-commits/skills/beijing-jifen-consult)
- [北京积分落户 · 口径与查询](references/口径与查询.md)
- [北京积分落户 · 填写校验清单](references/填写校验清单.md)
- [Bundled Beijing points-settlement simulator](assets/beijing-jifen-wizard.html)
- [Beijing Human Resources public service](https://fuwu.rsj.beijing.gov.cn/bjdkhy/ggfw/)
- [Beijing planning and natural resources portal](https://ghzrzyw.beijing.gov.cn/)
- [CHSI education verification](https://www.chsi.com.cn/)
- [China individual income tax service](https://etax.chinatax.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style advisory text with score summaries, field checklists, disclaimers, and references to the local HTML simulator.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final scores and projections should come from the HTML page or user-returned page results; text mode provides guidance only.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
