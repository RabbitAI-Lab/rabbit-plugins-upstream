## Description:

Using a fixed home camera to capture frontal facial images or short videos of the elderly, the system uses AI facial-landmark detection to analyze mouth-corner height difference, nasolabial fold symmetry, eyebrow lift asymmetry, and a facial asymmetry index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and health-monitoring platform developers use this skill to analyze frontal elderly face images or short videos for geometric asymmetry indicators, risk-level prompts, and report links. The output is an auxiliary screening signal and is not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles sensitive face and health data and sends it to cloud services.

Mitigation: Use only with informed consent from the monitored person or guardian, confirm endpoint and retention policies, and avoid uploading unnecessary or unrelated media.

Risk: The skill can create or reuse local identities, tokens, and account-linked report history.

Mitigation: Run it only in trusted workspaces, protect local workspace files, and review account linkage before deployment.

Risk: Facial-asymmetry output may be mistaken for a clinical diagnosis.

Mitigation: Present results as auxiliary screening indicators only and direct urgent neurological concerns to qualified medical care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-facial-asymmetry-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with risk prompts, metrics, history tables, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a local output file when requested by the user.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
