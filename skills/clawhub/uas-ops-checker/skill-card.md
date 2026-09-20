## Description:

uas-ops-checker is a zero-dependency decision-support CLI that classifies UAS operations against cited Chinese drone rules and returns JSON IR results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and compliance reviewers can use this skill to run a local UAS classification helper and review obligations, warnings, and rule citations for decision support. Its output must be manually verified and is not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Regulatory classifications may be incorrect or outdated.

Mitigation: Verify results against current official Chinese UAS rules and applicable authority guidance before relying on them.

Risk: Results may be incomplete when only one weight value is available or when controlled airspace, commercial use, or other special operating conditions apply.

Mitigation: Collect complete operation details and escalate special cases for qualified human review.

Risk: The local CLI output could be mistaken for legal proof.

Mitigation: Use the output as a reference aid only and keep a separate record of manual compliance review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/uas-ops-checker)
- [LGD theory ledger](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [JSON IR from the CLI, with markdown and bash usage examples in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes rc status codes and AIGC metadata; classifications are decision support only and require human review.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
