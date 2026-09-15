## Description:

GTS Operator lets an AI agent manage a GTS multi-tenant forms and approval platform through conversation, including tenant setup, organization and user management, form and workflow configuration, approval actions, delegation, timeout handling, queries, exports, and template reuse via the platform's HTTP APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dengkane](https://clawhub.ai/user/dengkane)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, administrators, and business operators use this skill to configure and operate GTS forms, workflows, approvals, delegations, exports, and reusable templates from natural-language requests while relying on the platform's discovery endpoints for current API contracts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate live GTS business data with the authenticated user's permissions and may perform approvals, deletions, public template publishing, delegation changes, or automatic approve/reject behavior.

Mitigation: Install only in a trusted single-user agent environment, restrict the authenticated account to appropriate permissions, and review confirmation prompts carefully before sensitive actions.

Risk: The skill stores a reusable 30-day bearer token in a local plaintext file.

Mitigation: Delete or revoke ~/.gts-operator.json when access is no longer needed, and prefer a hardened credential store or strict 0600 file permissions in production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dengkane/skills/gts-operator)
- [GTS API base](https://www.geeyo.com/s/gts/api.php)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request details and concise operational summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update live GTS platform records when authenticated and authorized by the user.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
