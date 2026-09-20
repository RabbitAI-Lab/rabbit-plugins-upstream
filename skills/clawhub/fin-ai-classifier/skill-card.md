## Description:

fin-ai-classifier is a zero-dependency decision-support CLI that classifies financial AI application risk under TH-FIN-002-oriented rules and emits JSON IR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, compliance reviewers, and financial AI teams use this local CLI to make preliminary risk-level and obligation classifications for financial AI applications. Outputs are decision-support material and should be manually checked against current official regulatory text or qualified counsel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool's financial AI classification output may be mistaken for legal or compliance proof.

Mitigation: Treat results as preliminary decision support and require human review against current official regulatory text or qualified counsel.

Risk: Some usage examples reference a stale option name that is not accepted by the CLI.

Mitigation: Use the implemented arguments --autonomy, --impact, and --target, or run --demo before integrating the tool into a workflow.

Risk: Non-Chinese users may miss context because key documentation and domain terminology are primarily Chinese.

Mitigation: Review the Chinese source documentation or obtain domain-language support before relying on classifications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/fin-ai-classifier)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [LGD theory ledger](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [JSON IR with text guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Python CLI output includes rc status codes, classification results, obligations, warnings, and aigc_mark metadata.]

## Skill Version(s):

1.0.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
