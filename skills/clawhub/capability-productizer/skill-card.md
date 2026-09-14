## Description:

按《AI超级个体》的主业深度、市场需求、独特优势与 AI 提效潜力，批量评估个人能力的产品化可行性，筛选最值得验证的能力并设计首个付费实验。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cglt2026opc](https://clawhub.ai/user/cglt2026opc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and individual creators use this Chinese-language skill to evaluate whether personal capabilities can become paid offers, separate evidence from assumptions, and design a first 7-14 day paid validation experiment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional evaluator runs on local JSON files and may produce incomplete classifications when inputs omit evidence fields.

Mitigation: Run it only on JSON input files intentionally provided by the user, then review classifications against the rubric before acting on them.

Risk: Productization advice can touch regulated services such as medical, legal, or financial work.

Mitigation: Keep recommendations within qualification, compliance, and professional review boundaries for regulated domains.

Risk: The workflow and generated labels are Chinese-language by design.

Mitigation: Use it when Chinese-language guidance is acceptable, or translate and review outputs before sharing with non-Chinese readers.

## Reference(s):

- [产品化判定规则](artifact/references/rubric.md)
- [ClawHub skill page](https://clawhub.ai/cglt2026opc/skills/capability-productizer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance, with optional JSON classifications from the local evaluator script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language outputs; the optional evaluator reads a user-provided JSON list and prints candidate capability statuses.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
