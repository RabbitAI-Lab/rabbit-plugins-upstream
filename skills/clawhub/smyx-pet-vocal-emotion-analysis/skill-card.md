## Description:

Recognizes cat and dog barks through pet voiceprint AI, translates and outputs emotions and behavioral intentions such as happiness, excitement, anger, anxiety, pain, vigilance, and attention-seeking, enabling human-pet smart interaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze cat or dog vocalizations from local media files or URLs, returning structured emotion and behavioral-intent results for pet interaction scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded pet media or supplied URLs are sent to lifeemergence.com cloud services for analysis.

Mitigation: Use only media and URLs approved for cloud processing, and avoid submitting sensitive or private content unless the user accepts that transfer.

Risk: The skill creates or reuses a local user/session identity record in the workspace data directory.

Mitigation: Run the skill in a dedicated workspace for sensitive use, and review or clear workspace data before sharing the environment.

Risk: Report-history wording can trigger automatic retrieval of prior cloud reports.

Mitigation: Confirm the user intends to query cloud history before using report-list or history phrasing.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-vocal-emotion-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown or JSON analysis report with optional report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the report to a local file when an output path is provided.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
