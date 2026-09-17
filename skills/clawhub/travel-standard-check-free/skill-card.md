## Description:

差旅费报销与标准表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and expense operations staff use this skill to check travel reimbursement tables against provided standards, including row-level arithmetic, totals, duplicates, blanks, and negative amounts. It reports cited findings from the submitted table and withholds conclusions when required columns or source material are missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a paid-upgrade prompt that asks users to run an external npx installer and install an onboarding skill.

Mitigation: Use only the local free checker unless the user separately trusts SkillPay, the npm package, and the newly installed onboarding skill.

Risk: Default human-readable output can include promotional text for the paid version.

Mitigation: Use the JSON output mode when only checker results are needed.

Risk: The checker reports only the free-tier checks and omits several travel-expense validations listed as withheld.

Mitigation: Treat findings as limited to the executed checks and do not assume unreported categories were evaluated.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON checker results, with shell commands for running the local Node.js script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free-tier checks only; JSON output is available for downstream parsing.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
