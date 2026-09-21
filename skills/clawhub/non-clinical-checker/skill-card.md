## Description:

A zero-dependency medical-device decision-support CLI that maps device inputs to non-clinical study checklist recommendations and JSON IR output based on cited GB/T, YY, and GB standards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, medical-device compliance teams, and reviewers can use this skill to run a local CLI that produces a JSON checklist of likely non-clinical study requirements for device self-assessment. The output is decision support and should be manually verified against current official NMPA, GB, and YY texts before registration, recall, clinical, or business decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat decision-support output as a regulatory or legal conclusion.

Mitigation: Use the output only as a checklist aid and require manual review before registration, recall, clinical, or business decisions.

Risk: Regulatory recommendations may be outdated or incomplete for a specific device or jurisdiction.

Mitigation: Verify recommendations against current official NMPA, GB, and YY texts and any written authority decisions.

Risk: The tool is designed for Chinese-language medical-device regulatory decision support.

Mitigation: Install and use it only when that domain and language fit the workflow, and involve qualified reviewers for final interpretation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/non-clinical-checker)
- [LGD Theory Ledger](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and deterministic JSON IR from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local zero-dependency Python CLI; return codes 0, 1, and 2 indicate completed, completed with warnings, or insufficient input.]

## Skill Version(s):

1.0.0 (source: server release metadata, SKILL.md frontmatter, non-clinical-checker.py META)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
