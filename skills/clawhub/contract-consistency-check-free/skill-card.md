## Description:

合同一致性AI核对（免费版）在本机对合同文本执行机械一致性核对，输出带原文、数字或行号证据的日期、金额、当事方、占位符、条款引用和定义词问题清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users, legal operations teams, and contract reviewers can use this skill to scan contract text before final review for mechanically checkable inconsistencies. It helps surface evidence-backed issues, but it does not provide legal advice or evaluate whether contract terms are fair or enforceable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional full-version upgrade path asks users to run unpinned external installer code and then follow newly installed skill instructions.

Mitigation: Treat the upgrade path as a separate high-trust action: verify the package, source, version, merchant, and payment flow before running installers or authorizing purchases.

Risk: Contract text may contain confidential business, legal, or personal information.

Mitigation: Use the free local checker only on the intended local Node.js path and keep contract files and credentials out of any optional purchase or installer process.

Risk: A clean result can be mistaken for legal clearance.

Mitigation: Use the result as an evidence-backed consistency screen only; have a qualified reviewer assess legal sufficiency, fairness, enforceability, and checks outside the free version scope.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chenqg618/skills/contract-consistency-check-free)
- [Publisher Profile](https://clawhub.ai/user/chenqg618)
- [Optional Full-Version Shelf](https://skillpay.alipay.com/public/tokendidi)
- [Optional SkillPay Build Guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance and local Node.js command output; optional JSON result with findings, summary, checks_given, and checks_withheld.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, line, message, advice, and evidence when sufficient contract text is provided.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
