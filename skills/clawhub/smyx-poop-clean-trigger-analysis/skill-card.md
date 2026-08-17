## Description:

Analyzes pet toilet or defecation-zone video to detect a pet waste event and produce a cleanup trigger signal for a robot vacuum integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and smart-home integrators can use this skill to analyze pet defecation-area videos, identify the pet-entered, waste-detected, pet-left event sequence, and receive a cleaning trigger signal for downstream robot vacuum automation. The trigger is an event flag; actual robot dispatch requires the user's smart-home gateway or vacuum API integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-area images or videos may be uploaded to the publisher's cloud service.

Mitigation: Use only footage appropriate for the publisher's service and retention practices; avoid sensitive household footage unless the deployment owner has reviewed those practices.

Risk: The skill can create or reuse a local/cloud identity and cache authentication tokens locally.

Mitigation: Run the skill in a controlled workspace, protect the workspace data directory, and review or clear cached identity data when changing users or environments.

Risk: The cleanup trigger is only an event flag and does not itself safely control a robot vacuum.

Mitigation: Route trigger output through a user-managed smart-home gateway or vacuum API with appropriate debounce, area limits, and manual override controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis)
- [Pet poop clean trigger API reference](references/api_doc.md)
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis output with report links and optional history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May output a cleanup trigger event flag; robot vacuum actuation is handled by user-side smart-home integrations.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
