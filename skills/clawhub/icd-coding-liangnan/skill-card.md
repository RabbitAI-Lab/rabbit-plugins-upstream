## Description:

ICD-Coding helps agents answer Chinese ICD-10, ICD-9-CM-3, ICD-O, clinical terminology, and CHS-DRG/DIP coding questions, including CHS-DRG 3.0 lookup and comparison workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liangnan](https://clawhub.ai/user/liangnan)

### License/Terms of Use:

MIT-0

## Use Case:

Healthcare coding, medical records, and reimbursement workflow users can use this skill to look up ICD and CHS-DRG codes, compare DRG 2.0 and 3.0 groupings, and draft coding guidance. Outputs should be checked against official coding and payer policy sources before operational use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Included ICD and DRG reference data may be incomplete, stale, or inconsistent with official policy sources for a specific payer or implementation date.

Mitigation: Confirm coding and reimbursement decisions against authoritative NHSA, WHO, and local payer policy sources before operational use.

Risk: Medical coding prompts or logs may contain unnecessary patient identifiers.

Mitigation: Use de-identified case details where possible and avoid including patient identifiers that are not needed for the coding task.

## Reference(s):

- [ICD-Coding ClawHub Skill Page](https://clawhub.ai/liangnan/skills/icd-coding-liangnan)
- [National Healthcare Security Administration ICD-10 Lookup](https://code.nhsa.gov.cn/jbzd/public/dataWesterSearch.html)
- [WHO ICD-10 Browser](https://icd.who.int/browse10/2022/en)
- [WHO ICD-11 Browser](https://icd.who.int/browse/11)
- [National Healthcare Security Administration DRG/DIP 3.0 Notice](https://www.nhsa.gov.cn/art/2026/9/2/art_104_21975.html)
- [CHS-DRG 3.0 Knowledge Manual](docs/DRG3.0_Knowledge.md)
- [CHS-DRG 2.0 to 3.0 Changes](docs/DRG3.0_Changes.md)
- [DRG 3.0 Lookup Tool](docs/drg3.0_lookup_tool.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown and plain text with optional Python or shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite local JSON lookup data and official policy references; no hidden network, credential, persistence, or destructive behavior was found in the security evidence.]

## Skill Version(s):

2.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
