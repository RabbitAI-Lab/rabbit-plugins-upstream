## Description:

Analyzes images or videos of plant cuttings in transparent containers to assess visible root primordia, root distribution, rooting stage, and transplant timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to monitor cutting propagation from uploaded or URL-based plant media and receive structured rooting-stage analysis, root-point observations, transplant timing guidance, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media or media URLs are sent to the Life Emergence backend for analysis.

Mitigation: Use only media that is acceptable to send to that backend, and avoid sensitive or private imagery unless organizational review approves the data flow.

Risk: The skill silently creates or reuses cloud identities and can access cloud report history.

Mitigation: Review identity linkage and report-history behavior before installation, and run the skill in an account or workspace appropriate for the reports it may retrieve.

Risk: Reusable tokens may be stored locally in plaintext.

Mitigation: Restrict filesystem access to the workspace, rotate tokens if exposed, and remove local token files when the skill is no longer needed.

Risk: A shipped development HTTP configuration can expose data and credentials if used for normal operation.

Mitigation: Replace development HTTP endpoints with approved production HTTPS configuration before normal use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cutting-rooting-status-detection-analysis)
- [Life Emergence demo page](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report history entries and exported report URLs when history lookup is requested.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
