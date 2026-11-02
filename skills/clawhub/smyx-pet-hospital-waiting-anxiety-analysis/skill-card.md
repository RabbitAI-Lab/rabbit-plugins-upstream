## Description:

Triggers when a user provides a pet hospital waiting area video URL or file for analysis; supports local video uploads or network URLs to call server-side APIs for anxiety-related behavior recognition, detecting open-mouth panting intensity, limb/torso trembling amplitude, ear-flattening degree and other stress signals, outputting a standardized anxiety level (1-5) to help medical staff identify high-stress pets and prioritize care or comfort (without diagnosing diseases or prescribing treatment).

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Veterinary staff can use the skill to review waiting-area pet videos, identify visible stress behaviors, and prioritize comfort or care. It returns an anxiety level for workflow reference and does not diagnose disease or prescribe treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A setting that promises no analysis may still upload video, and the API-address option may be ignored.

Mitigation: Request fixes and verify the upload destination before use; confirm the provider's retention policy and remove unnecessary bystanders and audio from clinic footage.

Risk: Automatic remote account registration and saved login credentials have unclear user controls.

Mitigation: Request explicit control over remote registration and account selection, plus protected credential storage and removal controls.

## Reference(s):

- [API interface documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-pet-hospital-waiting-anxiety-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured anxiety analysis report with behavior observations, an anxiety level from 1 to 5, and report links when available; report lists can be formatted as Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [For workflow reference; it does not provide a disease diagnosis or treatment plan.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
