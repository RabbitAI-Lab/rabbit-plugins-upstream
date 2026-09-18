## Description:

运单回单与代收货款核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, logistics, and settlement teams use this skill during monthly close, reconciliation, and inventory checks to review waybill POD and COD reconciliation tables. It checks row-level arithmetic, total-row consistency, duplicate waybill rows within the same period, blanks, placeholders, and negative values, with source-line evidence for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a paid-upgrade path that asks an agent to run external install and payment onboarding commands.

Mitigation: Keep use of the free checker local, and require manual review plus explicit user approval before any npx install, dependency installation, wallet authorization, or payment action.

Risk: The free checker intentionally omits several higher-tier checks, so users may over-read a clean result.

Mitigation: Present executed and withheld checks together, and do not treat a free-tier clean result as coverage for checks listed as not run.

Risk: The checker does not decide contractual, legal, tax, accounting, or signature-validity questions.

Mitigation: Use findings only for table arithmetic and consistency review, and route contract, legal, tax, accounting, and POD-signature questions to the appropriate human reviewer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/waybill-pod-cod-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with local shell commands and optional JSON checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; the free checker reports executed and withheld checks and refuses to conclude when required input is missing.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
