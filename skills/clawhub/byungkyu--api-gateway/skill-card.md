## Description:

Guides agents in calling APIs for user-connected apps through the Maton gateway and managing related connections and automations with user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users with Maton-connected apps use this skill to retrieve information or perform explicitly approved actions across third-party services. It also describes separately approved connections, hosted functions, and event automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected apps may expose sensitive data or allow changes beyond the task.

Mitigation: Review connection scopes, prefer read-only access, and confirm the target and effect before any write or deletion.

Risk: Webhooks and triggers can forward event data persistently to external destinations.

Mitigation: Require separate approval for the destination and event scope; remove forwarding when no longer needed.

Risk: Hosted functions and local event handlers can act on connected-account data or untrusted events.

Mitigation: Deploy only reviewed code with explicit approval and least-privilege connections; approve local handlers separately.

## Reference(s):

- [ClawHub API Gateway release](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline commands and examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API results depend on connected services and granted permissions.]

## Skill Version(s):

1.2.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
