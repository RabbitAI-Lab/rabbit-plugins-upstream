## Description:

GTS Operator lets an AI agent manage a GTS multi-tenant form and workflow platform through conversation, including tenant setup, organization and user maintenance, form and workflow configuration, business document submission, approvals, queries, and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dengkane](https://clawhub.ai/user/dengkane)

### License/Terms of Use:

MIT-0

## Use Case:

External users and platform administrators use this skill to manage GTS tenant administration and OA workflow tasks through conversation while the agent performs the corresponding REST API actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist a powerful GTS OAuth token in a local token file.

Mitigation: Prefer OAuth device authorization, protect or delete the local token file when finished, and revoke platform access if the workstation or token file may be exposed.

Risk: An overridden API base could route credentials or tokens to an untrusted origin.

Mitigation: Do not override the API base except for a trusted environment with separate credentials.

Risk: The security verdict is suspicious because production-tenant use can affect administrative data and workflow approvals.

Mitigation: Review before installing in a production tenant and confirm sensitive or destructive operations before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dengkane/skills/gts-operator)
- [GTS API endpoint](https://www.geeyo.com/s/gts/api.php)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Configuration, Markdown]

**Output Format:** [Markdown instructions with JSON examples and REST API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OAuth device authorization when available and relies on live discovery endpoints before performing operations.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
