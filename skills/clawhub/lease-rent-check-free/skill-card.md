## Description:

租金账单/租赁结算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号，本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and finance or operations employees use this skill to check Chinese-language lease rent and settlement worksheets for arithmetic consistency, rolling arrears, duplicate tenants, blanks, and line-referenced findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes embedded instructions that steer users or agents toward a separate paid install and purchase flow.

Mitigation: Use the local free checker only unless the vendor, package version, merchant, price, and permissions are separately verified; do not let an agent run the SkillPay npx command or initiate purchase steps automatically.

Risk: The checker can return incomplete or misleading conclusions if the rent worksheet lacks required headers or source rows.

Mitigation: Provide the full lease rent or settlement worksheet with headers; treat insufficient-input responses as a request for more source material, not as a clean audit result.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/chenqg618/skills/lease-rent-check-free)
- [Artifact skill definition](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON from a local Node.js checker, typically summarized in Markdown by the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields rather than a positive conclusion.]

## Skill Version(s):

1.0.11 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
