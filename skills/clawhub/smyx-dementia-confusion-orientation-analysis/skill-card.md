## Description:

Analyzes fixed-camera and optional microphone footage in dementia care or home settings to identify confusion or disorientation behaviors and produce structured orientation-soothing reports and actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, care facilities, and home-care operators use this skill to analyze submitted video or video URLs for confusion or disorientation signals in people with dementia and receive structured reports, history listings, and orientation-soothing recommendations. It is not a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive video, optional audio, and history queries for people with dementia through cloud services.

Mitigation: Use only in controlled care settings with documented consent, visible notice, retention rules, and strict limits on who may submit media URLs or request history.

Risk: Silent account setup and local token storage can weaken identity scoping and access control.

Mitigation: Review the account and token storage behavior before deployment, isolate the workspace, restrict filesystem access, and rotate or remove locally stored credentials when access changes.

Risk: Behavior recognition and soothing recommendations could be mistaken for medical diagnosis or relied on without caregiver review.

Mitigation: Present outputs as observational support only, require caregiver review before operational use, and escalate recurring or severe confusion events to appropriate local clinical resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-dementia-confusion-orientation-analysis)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [Markdown and JSON text, with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links and cloud history listings when the skill is used with analysis or list commands.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
