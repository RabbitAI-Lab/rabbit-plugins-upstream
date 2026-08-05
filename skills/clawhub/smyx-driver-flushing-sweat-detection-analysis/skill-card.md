## Description:

Using an in-cabin DMS camera, the skill analyzes driver face video for visual facial flushing and sweat or reflective-area signals, then returns a health-risk reminder without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, vehicle safety teams, and fleet operators use this skill to route in-cabin DMS images or video to a cloud analysis service and receive structured visual reminders about facial flushing or sweating abnormalities. It is intended as an assistive driver-health alerting workflow, not as a medical diagnostic device.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive driver face video and health-adjacent visual inferences through a configured cloud service.

Mitigation: Use only with clear driver or employee consent, documented tenant scoping, retention and deletion rules, and controls for exported report links.

Risk: The skill silently creates or reuses a local identity and persists tokens while retrieving historical report links.

Mitigation: Review local identity and token storage before deployment, restrict access to report history, and verify that production environments isolate users and tenants correctly.

Risk: Facial flushing and sweat signals can be affected by lighting, camera channel, tinting, occlusion, and individual skin-tone variation.

Mitigation: Treat outputs as assistive visual alerts only, require RGB camera input and stable lighting, and route medical concerns to appropriate professional evaluation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-flushing-sweat-detection-analysis)
- [Driver flushing and sweat detection API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured analysis text, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include visual metrics, warning type, recommended action, analysis status, and historical report links returned by the configured cloud service.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
