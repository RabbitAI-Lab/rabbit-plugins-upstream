## Description:

Analyzes pet-monitoring video for possible overlap between a pet in a UV disinfection area and an active UV lamp, then returns a structured safety report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and care facilities can submit a local video or video URL for a structured report about potential pet exposure to an active UV disinfection area. The result is an advisory safety assessment, not medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment identifies unclear account and credential handling, external video analysis, privacy and side-effect concerns, and a partial scan.

Mitigation: Review identity and credential handling and the video processing destination before use; avoid submitting sensitive footage until these details are clear.

Risk: The advertised live monitoring and automatic UV shutoff are not clearly reflected in the available submission behavior, which analyzes submitted video and returns a report.

Mitigation: Treat reports as advisory, confirm any monitoring or device-control integration, and keep independent UV safety controls in place.

Risk: Visual UV-lamp status cues can be affected by ambient lighting.

Mitigation: Use a supported smart-home status signal where available and independently verify that the UV lamp is off before allowing pets into the area.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface notes](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Structured safety report with analysis results and a report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory results based on a submitted video or URL; supports basic, standard, and JSON detail levels.]

## Skill Version(s):

1.0.16 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
