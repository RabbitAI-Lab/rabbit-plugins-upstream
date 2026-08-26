## Description:

Analyzes pet defecation-zone video or image input to detect a pet defecation event and return a cleaning trigger signal and report for downstream robot vacuum integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze fixed pet toilet or defecation-area media, identify the enter-defecate-leave event sequence, and generate a cleanup trigger that can be connected to a user-managed robot vacuum or smart-home gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-area media or media URLs are sent to the publisher's backend for analysis.

Mitigation: Use only media approved for third-party processing and avoid clips that expose people, private rooms, credentials, or unrelated sensitive content.

Risk: The skill queries cloud history and stores identity tokens in the local workspace database.

Mitigation: Review the identity and token storage behavior before installation, restrict workspace access, and clear stored credentials when the skill is no longer needed.

Risk: Packaged configuration includes dev HTTP endpoints as well as public production URLs.

Mitigation: Inspect the active configuration and use only the intended trusted backend endpoints before operational deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis)
- [API interface document](artifact/references/api_doc.md)
- [Shared analysis API document](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or text report with JSON analysis content, history tables, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs a vision-based event result and cleanup trigger flag; actual robot vacuum control requires a separate user-side smart-home or vendor API integration.]

## Skill Version(s):

1.0.8 (source: server release metadata; SKILL.md frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
