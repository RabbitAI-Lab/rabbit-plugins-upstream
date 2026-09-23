## Description:

AI-powered transpiration rate estimation for indoor plants using thermal infrared or RGB leaf media plus environmental context to estimate a relative transpiration index and provide plant water-stress guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, greenhouse operators, and plant-care developers use this skill to analyze indoor plant leaf images or videos and receive a structured transpiration-rate estimate, root water-uptake vitality assessment, stress hints, care suggestions, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-submitted plant images, videos, or URLs are sent to a cloud service.

Mitigation: Use only media suitable for third-party processing and avoid sensitive facility imagery unless the publisher documents retention, deletion, and handling practices.

Risk: The skill creates or reuses a local account identity and stores service tokens and report history locally.

Mitigation: Review local identity and token storage before deployment, restrict filesystem access, and clear stored data where required by policy.

Risk: Security review found leftover pet/video-analysis artifacts that do not fully match the plant-care purpose.

Mitigation: Review generated outputs and configuration before use, and prefer updated releases that remove unrelated artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-transpiration-rate-estimation-analysis)
- [Skill usage demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON structured analysis report with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud-hosted analysis and report-history services; accepts image, video, local file path, or URL inputs.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
