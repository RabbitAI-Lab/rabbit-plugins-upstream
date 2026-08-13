## Description:

Analyzes child or student learning media to identify study behavior patterns, summarize risks, and provide structured family education suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users can provide a child or student's study video, image, local file, or public media URL to receive a structured learning behavior report. The skill is intended for family education reference, study habit review, posture and focus assessment, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends child or student media, or media URLs, to lifeemergence.com cloud APIs for processing.

Mitigation: Install and use only when cloud processing of the child media is acceptable and appropriate consent and data handling review have been completed.

Risk: The skill links analysis results to an internal identity and can retrieve prior cloud reports.

Mitigation: Review identity linkage and historical report access before deployment, and limit use to workflows where this account association is expected.

Risk: The security scan reports silent account creation or reuse and local token persistence in a workspace SQLite database.

Mitigation: Use an isolated workspace, restrict local file access, and clear persisted tokens or workspace state when analysis access should end.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-study-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON analysis reports with report links and optional shell command usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured behavior scores, risk notes, education suggestions, historical report tables, and exported report links.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
