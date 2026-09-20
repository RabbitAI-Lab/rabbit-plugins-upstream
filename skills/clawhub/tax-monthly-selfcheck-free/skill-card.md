## Description:

税务月度自查包（免费版）本地核对分段税务材料，覆盖增值税进销项与税负率、增值税附加税费、预缴企业所得税三类自查，并为每条发现提供可复核依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and operations staff use this skill around monthly close, reconciliation, inventory, or filing preparation to cross-check segmented Chinese tax materials. It performs deterministic arithmetic, totals, duplicate-period, and missing-field checks without treating the result as tax advice or a complete compliance review.

### Deployment Geography for Use:

Global; intended for Chinese-language tax materials.

## Known Risks and Mitigations:

Risk: The skill can report a clean result even when none of the required sections were actually checked.

Mitigation: Before relying on the result, verify that sections_done is greater than zero and each required per_check entry has status ok.

Risk: Users may over-rely on arithmetic cross-check output for tax close or filing decisions.

Mitigation: Treat the output as a local arithmetic and consistency check only, and have a qualified reviewer confirm tax positions and filing decisions.

Risk: Incorrectly segmented or incomplete Chinese tax materials can prevent the intended checks from running.

Mitigation: Provide input sections with the expected === 检查名 === headings and review missing-section or insufficient-input statuses before interpreting findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tax-monthly-selfcheck-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text with optional pretty-printed JSON results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, withheld checks, per-check statuses, findings, severity counts, local execution status, and scope notes.]

## Skill Version(s):

1.0.43 (source: server release metadata; artifact frontmatter lists 1.0.42)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
