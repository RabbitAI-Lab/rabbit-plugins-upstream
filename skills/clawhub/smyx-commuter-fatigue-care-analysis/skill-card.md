## Description:

Analyzes smart-home living-room video or URL inputs from the first 30 minutes after a commuter arrives home to estimate fatigue signals and return care suggestions, history results, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External smart-home users and developers use this skill to analyze living-room camera video or URLs for after-work fatigue cues, receive a structured fatigue report, and retrieve previous reports from the configured cloud service. It is not a medical diagnosis tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home video or audio-derived fatigue data may be sent to the configured cloud or private service.

Mitigation: Require explicit user opt-in, use production HTTPS endpoints, and confirm retention and deletion controls for raw media and reports before use.

Risk: The skill silently creates or reuses an account identifier and stores tokens in the workspace.

Mitigation: Restrict workspace access, review account-linkage behavior before deployment, and remove or rotate local tokens when they are no longer needed.

Risk: Fatigue scoring could be mistaken for a medical or employment decision signal.

Mitigation: Keep outputs limited to care suggestions, avoid medical diagnosis, and do not share fatigue data with employers, insurers, or unrelated third parties.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown/text containing structured JSON-style analysis results, history tables, progress messages, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save output to a file when an output path is provided.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
