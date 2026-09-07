## Description:

Early monitoring of plant wilting based on hyperspectral imaging and computer vision, captures early wilting signs before visible symptoms, provides early warning for precision irrigation and disease control. | 植物枯萎监测技能，基于高光谱成像与计算机视觉，在肉眼可见症状前捕捉早期枯萎迹象，为精准灌溉和病害防控提供早期预警

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agricultural operators, and plant monitoring teams can use this skill to analyze plant images or videos for early wilting signs, distinguish environmental water stress from pathological wilt, estimate wilting severity, and produce early-warning reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send plant media, identity data, and authentication tokens to remote services, and the security evidence flags insecure HTTP and local token storage.

Mitigation: Review the publisher and configuration before installation, use HTTPS-only production endpoints, remove packaged development HTTP settings, and keep tokens in a secure secret store or short-lived memory.

Risk: The skill can upload files for analysis and retrieve historical reports from cloud services.

Mitigation: Ask clearly before uploading user files or retrieving history, and expose only the analysis results and report links needed by the user.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis)
- [API接口文档](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with findings, risk notes, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can query cloud-hosted historical reports and can write report output to a user-specified file.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
