## Description: <br>
Automatically identifies wet clothing and abnormal excretion via visual AI. Instantly notifies caregivers to improve care for incontinent elderly, bedridden patients, and infants, reducing skin issues and complications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers and care operations teams use this skill to analyze care images, videos, or media URLs for wet clothing, abnormal excretion, alert level, care suggestions, and report history. It is intended as a caregiver alert and record-review aid, not a substitute for professional medical judgment or manual inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive care images, videos, media URLs, identity metadata, and report history may be sent to the publisher cloud service. <br>
Mitigation: Use only with consent and authorization, restrict access to caregivers who need the data, and confirm privacy and compliance requirements before deployment. <br>
Risk: The skill silently handles account identity and tokens and can retrieve cloud history for the current identity. <br>
Mitigation: Review local token storage and automatic report-history access before installation, and run it only in workspaces where that identity behavior is acceptable. <br>
Risk: Visual analysis can be wrong due to lighting, angle, clothing thickness, image quality, or scene ambiguity. <br>
Mitigation: Require caregiver confirmation before acting on alerts and do not use the output as a replacement for professional medical judgment or manual checks. <br>


## Reference(s): <br>
- [Incontinence Alert Analysis API Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-incontinence-alert-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files, Shell commands] <br>
**Output Format:** [Markdown or JSON text reports with optional saved output files and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can analyze local media files or media URLs, list cloud report history, and save results when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.7 (source: evidence release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
