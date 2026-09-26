## Description:

Analyzes fixed-camera medication-area videos to detect pick-up, to-mouth, and swallow steps and produce medication-compliance results and caregiver alert text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, elder-care operators, and developers use this skill to analyze medication-area video or image inputs, check whether the pick-up, to-mouth, and swallow steps were observed, and generate structured compliance reports or historical report listings. It supports medication adherence monitoring, not medical diagnosis or dosing advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Medication-area videos may contain sensitive health and household information and are sent to the configured cloud service.

Mitigation: Use the skill only with informed consent from the monitored person or caregiver, avoid unnecessary uploads, and keep video files and report outputs in a protected workspace.

Risk: The skill can create or reuse persistent identities and tokens with limited user-visible control.

Mitigation: Run it in a dedicated workspace or account, review stored workspace data after use, and clear local databases or tokens when report access should not persist.

Risk: Visual medication-step detection can be incomplete or uncertain and should not be treated as medical advice.

Mitigation: Use results as adherence-support signals only; confirm missed or uncertain medication events manually and do not use the output to change medication plans.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-medication-compliance-analysis)
- [Medication compliance API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON containing structured medication-step detections, compliance status, confidence, alert text, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an optional output file when requested by the user.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
