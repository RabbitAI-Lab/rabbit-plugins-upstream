## Description:

Analyzes indoor pet-camera video for sustained contact between a pet’s mouth and hazardous non-food items, then returns a safety alert and structured report without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and smart-home safety operators use the skill to review indoor camera footage for pets contacting hazardous non-food items and receive monitoring alerts and reports. The results support safety monitoring and do not diagnose disease.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos may be uploaded despite an export-only setting.

Mitigation: Use only for explicitly requested pet analysis; avoid private footage until the export-only safeguard is corrected, and clarify upload, retention, and deletion practices first.

Risk: The API secret may be reused as an account identifier.

Mitigation: Wait for secret and identity handling to be corrected, and isolate credentials and report histories in shared installations.

Risk: Remote detection accuracy has not been verified.

Mitigation: Treat alerts as monitoring cues, review the footage, and do not use results as a diagnosis or the sole safety control.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface notes](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured analysis report and safety alert as text or JSON; Markdown tables for history listings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monitoring guidance only; no disease diagnosis.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
