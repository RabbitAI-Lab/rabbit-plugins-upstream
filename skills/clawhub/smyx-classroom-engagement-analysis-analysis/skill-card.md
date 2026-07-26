## Description: <br>
Analyzes fixed-camera classroom images or video to estimate aggregate student engagement, anonymous low-engagement seat coordinates, heatmaps, alerts, teacher suggestions, and history reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teachers, smart-classroom operators, and education-technology developers use this skill to analyze classroom video or images for group engagement trends, low-engagement seat locations, confusion hotspots, and teaching suggestions. It can also query previously generated classroom engagement reports from the remote service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends classroom video or image inputs to a remote service for analysis, which can involve minors and sensitive classroom context. <br>
Mitigation: Use only with explicit school and parent consent, documented data-retention terms, and verified service-operator controls for storage, access, and deletion. <br>
Risk: Server evidence states that the skill creates and stores a reusable internal user identity and report history despite strong anonymity claims. <br>
Mitigation: Confirm where user identifiers, report history, videos, heatmaps, and tokens are stored, who can access them, and how local and cloud records can be deleted before deployment. <br>
Risk: Engagement and emotion analysis can be inaccurate or misleading if used as an assessment of individual students. <br>
Mitigation: Use outputs only as real-time teaching support, keep reminders anonymous at the seat-coordinate or group level, and prohibit use for student performance evaluation, parent communication, or public ranking. <br>


## Reference(s): <br>
- [API Reference](references/api_doc.md) <br>
- [Additional API Error Reference](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-classroom-engagement-analysis-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include engagement scores, emotion distributions, anonymous seat coordinates, heatmap image URLs, alerts, teacher suggestions, and historical report records.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
