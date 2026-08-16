## Description:

Analyzes household public-area audio and video for conflict signals, waits for a calm window, and returns neutral aftercare suggestions or safety-resource escalation when red-line signals appear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and smart-home integrators use this skill to process household public-area camera and microphone inputs, produce structured conflict-monitoring reports, and suggest neutral post-conflict aftercare actions after a calm window. It is intended for event detection and aftercare prompts, not psychological counseling or domestic-violence intervention.

### Deployment Geography for Use:

Global, with jurisdiction-specific emergency resources configured before use.

## Known Risks and Mitigations:

Risk: Sensitive household audio/video may be uploaded to cloud APIs and retained in reports.

Mitigation: Use only with informed consent from affected household members, limit deployment to approved public household areas, and confirm deletion paths for uploaded media and cloud reports.

Risk: The skill can silently create or reuse local identities and store tokens in a workspace database.

Mitigation: Review the workspace data directory before and after use, rotate or remove stored tokens when access is no longer needed, and document how local records are deleted.

Risk: Safety-resource guidance can be wrong outside the configured jurisdiction.

Mitigation: Configure jurisdiction-appropriate emergency and domestic-violence resources before deployment and verify escalation behavior for red-line events.

Risk: False positives or poorly timed prompts could escalate a household conflict.

Mitigation: Require the documented calm-window checks, provide an opt-out or disable control, cap repeated prompts, and keep aftercare messages neutral.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-family-conflict-aftercare-suggest-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown-oriented text with JSON structured report content and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the returned report text to a user-specified output file and can query cloud-stored historical reports.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
