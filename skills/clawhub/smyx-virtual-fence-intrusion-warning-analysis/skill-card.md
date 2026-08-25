## Description:

Customizes safety zones for infant home monitoring, analyzes submitted video or image inputs for boundary crossings near bedsides or windowsills, and returns alerts, reports, or historical report listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and developers use this skill to submit infant home monitoring videos or URLs for virtual fence crossing analysis and to retrieve cloud-hosted historical alert reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private infant or home monitoring video may be sent to remote services for processing.

Mitigation: Use only with trusted service endpoints and submit footage only when cloud processing of that data is acceptable.

Risk: The skill can silently create or reuse an identity and stores account tokens locally.

Mitigation: Run it in an isolated environment, review token storage before deployment, and clear local tokens when access should end.

Risk: Historical report queries can expose cloud-hosted monitoring reports tied to the resolved account.

Mitigation: Restrict who can run history queries and confirm the account linkage before using the report-listing workflow.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-virtual-fence-intrusion-warning-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown report or JSON response, optionally saved as a file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or public video URLs; documented formats are mp4, avi, and mov with a 10 MB maximum file size.]

## Skill Version(s):

1.0.11 (source: server release metadata; SKILL.md frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
