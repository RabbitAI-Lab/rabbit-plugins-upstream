## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Planning meeting participants use this assistant to turn explicitly requested feature and bugfix discussions into sanitized, confidential GitLab issues. It keeps implementation work out of scope unless separately requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting material may include identifying details or secrets that should not be copied into GitLab issues.

Mitigation: Sanitize every outgoing field and attachment, replace identifying details with stable placeholders, and remove secrets completely before writing.

Risk: The security scan has partial coverage because some local references were unresolved.

Mitigation: Review the skill and relevant referenced material before deployment; do not treat the scan as covering unresolved references.

Risk: Requiring English for GitLab content may introduce wording errors when meeting discussion is in another language.

Mitigation: Check that English issue content is acceptable and leave unclear or missing details open rather than inventing them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Sanitized GitLab issue titles and descriptions with acceptance criteria, plus brief natural-language replies.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issue content is written in English and created as confidential only on explicit request.]

## Skill Version(s):

1.147.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
