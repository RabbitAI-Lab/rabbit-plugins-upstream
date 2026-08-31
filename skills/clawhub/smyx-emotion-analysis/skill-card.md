## Description:

Analyzes face images or videos for micro-expressions and emotional states, returning structured reports with findings, suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to submit face media or media URLs for micro-expression and emotion analysis, then retrieve structured results or historical report lists. Results should support review and communication workflows, not serve as proof of a person's true feelings or as a substitute for professional psychological judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive face media or media URLs to a vendor cloud service for analysis.

Mitigation: Use only with appropriate consent and data handling review, and avoid submitting media where cloud processing is not acceptable.

Risk: Reports are tied to automatically managed local or remote identity records.

Mitigation: Do not expose internal identity values to users, and review account, token, retention, and access behavior before deployment.

Risk: Emotion-analysis outputs can be mistaken for objective proof of a person's true feelings.

Mitigation: Present outputs as informational signals only and avoid employment, legal, medical, school discipline, surveillance, or other high-stakes decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-emotion-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON text containing emotion analysis results, history report tables, report links, and script invocation guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include vendor-hosted report export links and historical report records associated with an automatically managed identity.]

## Skill Version(s):

1.0.14 (source: server release evidence; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
