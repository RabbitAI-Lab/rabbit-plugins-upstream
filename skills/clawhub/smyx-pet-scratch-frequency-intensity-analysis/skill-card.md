## Description:

Analyzes cat scratch post videos or URLs to report scratching frequency, session duration, intensity estimated from vibration, and observational stress or claw-health signals without diagnosing disease or prescribing behavior changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze cat scratch post footage for structured behavior observations, including frequency, duration, relative intensity, stress indicators, claw-health observations, and cloud report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded pet videos or supplied URLs are sent to the publisher's cloud service for analysis.

Mitigation: Use an isolated workspace or account and avoid sensitive home footage unless the publisher provides clear retention, authorization, and deletion guarantees.

Risk: The skill can silently create or reuse an internal account and store local identity or token data.

Mitigation: Review the publisher's account behavior before installation and avoid sharing workspaces across unrelated users.

Risk: Historical report queries can retrieve cloud-stored analysis reports.

Mitigation: Confirm that report history access matches the intended user and workspace before relying on returned records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-scratch-frequency-intensity-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis text with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a file when an output path is provided.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
