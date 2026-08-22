## Description:

Generates condensed album highlights based on specified keywords or targets, extracting specific target segments from long videos and compiling them into a summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit local videos or public video URLs with target keywords, then receive condensed time-lapse album highlights and structured analysis results. It can also query cloud-hosted historical report lists for the same analysis workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends supplied videos or URLs to an external backend for analysis.

Mitigation: Use only videos and URLs approved for external processing, and avoid private, internal, or regulated personal data unless the publisher documents retention and deletion controls.

Risk: The skill silently creates or reuses an internal account identity and stores authentication tokens in a local workspace SQLite database.

Mitigation: Review account handling and local token storage before deployment, and restrict workspace access to trusted users.

Risk: History-query trigger phrases can automatically query cloud report history.

Mitigation: Tell users when a cloud history query is being performed and confirm the workspace is authorized to access those reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-custom-timelapse-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write analysis output to a user-specified file path.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
