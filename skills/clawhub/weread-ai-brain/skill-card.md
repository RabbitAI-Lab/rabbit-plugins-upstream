## Description:

WeRead AI Brain analyzes a user's WeRead shelf, reading statistics, highlights, and personal thoughts to produce reading dashboards, book analyses, cross-book connections, and optional Markdown or HTML exports after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yamyeed](https://clawhub.ai/user/yamyeed)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to turn WeRead activity, highlights, and personal notes into readable dashboards, focused book analysis, cross-book synthesis, and portable note exports. The skill is intended for user-approved WeRead workflows that may require a WeRead API key and access to private reading data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private WeRead shelf data, reading statistics, highlights, personal thoughts, and a WeRead API key.

Mitigation: Use the skill only after the user confirms the data scope; keep the API key in WEREAD_API_KEY and send it only to the WeRead official HTTPS gateway.

Risk: Markdown or HTML exports may contain private reading notes, highlights, or analysis derived from those notes.

Mitigation: Confirm the export content and path before writing files, and avoid exporting unless the user explicitly requests it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yamyeed/skills/weread-ai-brain)
- [Project homepage](https://github.com/yamyeed/weread-ai-brain)
- [WeRead API gateway](https://i.weread.qq.com/api/agent/gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses, optional Markdown files, optional single-file HTML dashboards, and JSON API data used for analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require WEREAD_API_KEY and explicit confirmation before fetching private WeRead data or writing exports.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
