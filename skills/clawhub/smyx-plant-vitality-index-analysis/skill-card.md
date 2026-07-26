## Description: <br>
Using plant images, optional environmental data, and growth metrics, this skill calls a plant-analysis service to produce a 0-100 vitality score, vitality grade, trend, change percentage, alert hints, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and plant-monitoring operators use this skill to evaluate plant vitality from plant images or videos and to retrieve cloud-hosted historical vitality reports. It is intended for smart planters, plant factories, home gardening, and plant-monitoring platforms where concise scoring and trend reporting support care decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, videos, URLs, and report history may be processed by lifeemergence.com services. <br>
Mitigation: Use only media and URLs approved to leave the user's environment, and avoid private files or internal URLs unless external processing is permitted. <br>
Risk: The skill may create or reuse a local or remote identity and store session tokens in workspace data. <br>
Mitigation: Review workspace data handling before deployment, limit access to generated tokens, and remove or rotate stored identity data when the skill is no longer needed. <br>
Risk: Single-image vitality scores can be affected by lighting, angle, and image quality. <br>
Mitigation: Prefer consistent daily image sequences and treat scores as care guidance rather than definitive plant-health diagnosis. <br>


## Reference(s): <br>
- [API Documentation](references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown and JSON reports with score, grade, trend, alert hints, report links, and optional history tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud APIs for analysis and historical report retrieval; supports local file paths or public media URLs as inputs.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter lists 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
