## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Meeting participants and teams use this skill to turn explicitly requested feature or bug discussions into sanitized, confidential GitLab issues in a project they select.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting content may include identifying details or secrets that should not appear in GitLab work items.

Mitigation: Review the complete issue content and attachments, anonymize identifying details, remove secrets, and create the issue as confidential.

Risk: The workflow writes GitLab issue content in English, which may not fit every team's language requirements.

Mitigation: Confirm that English-only issue content suits the project workflow; keep spoken and chat replies in the requester's chosen language.

Risk: The security assessment is incomplete because some path-like references could not be resolved.

Mitigation: Review unresolved references and complete the security assessment before deployment.

## Reference(s):

- [GitLab Meeting Assistant on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Text, API Calls]

**Output Format:** [Sanitized GitLab issue titles and structured descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates confidential feature or bug issues only after an explicit user instruction.]

## Skill Version(s):

1.141.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
