## Description:

Read SimplePractice Client Portal data from a shell with curl, including appointments, billing documents, documents to sign, announcements, practice details, and clinician details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable portal users use this skill to retrieve their own SimplePractice Client Portal information with curl when they want scriptable access without running the simplepractice-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The cookie jar and copied magic-link token can grant access to medical portal data.

Mitigation: Keep them out of logs and shared machines, store the cookie jar with restrictive permissions, and remove it when access is no longer needed.

Risk: Extending the examples beyond read-only access could affect payments, document signing, cancellations, or messaging.

Mitigation: Use the skill's read-only examples for inspection and perform state-changing actions in the SimplePractice portal where the user can review the action.

## Reference(s):

- [SimplePractice Client Portal request reference](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, curl, and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal examples; users provide their own practice host and authenticated session.]

## Skill Version(s):

1.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
