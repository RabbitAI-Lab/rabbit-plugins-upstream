## Description:

AI-powered non-invasive rooting-stage detection for plant cuttings in transparent containers that analyzes images or videos of the cutting base, detects white root primordia and roots, and reports the rooting stage with transplant-timing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, and plant-propagation operators use this skill to evaluate transparent-container cutting images or videos for root primordia, root distribution, rooting stage, and transplant readiness. It can also retrieve cloud-hosted historical analysis reports associated with the internally resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send user-provided plant media or media URLs to configured cloud analysis services.

Mitigation: Use it only with media that may be processed by the configured service, and review the configured API endpoints before deployment.

Risk: The skill can create or reuse an internal/default identity and associate analysis history with that identity.

Mitigation: Run it in a controlled workspace and verify the intended account identity before using history or report retrieval features.

Risk: The skill may store access tokens and user records in a local SQLite database shared by the skill workspace.

Mitigation: Protect the workspace data directory, avoid sharing it across trust boundaries, and rotate or clear local tokens when decommissioning the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cutting-rooting-status-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text with report links; optional file output when an output path is supplied.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local image or video files and remote media URLs; history queries return structured report records from the configured cloud API.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
