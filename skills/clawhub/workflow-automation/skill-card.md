## Description:

Workflow Automation helps agents validate allowlisted workflows, trigger fixed production webhooks only after explicit approval, and read scoped workflow execution status and history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow operators use this skill to safely validate approved workflow targets, request explicit approval for a concrete trigger action, and inspect execution outcomes without exposing provider credentials or arbitrary webhook endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved workflow triggers may cause real downstream business effects.

Mitigation: Approve only after checking the workflow name, version, content hash, expiration, and exact input.

Risk: Trigger timeouts or reconciliation-required states may still mean a webhook was accepted.

Mitigation: Do not retry automatically; preserve the original request JSON, UUID, task ID, and billing evidence for reconciliation.

Risk: Uncontrolled credentials or endpoints could expose secrets or bypass the fixed workflow target.

Mitigation: Use only preconfigured allowlisted production webhooks and reject caller-supplied URLs, hosts, headers, credentials, tokens, cookies, secrets, or binary data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/workflow-automation)
- [AI Skills Homepage](https://ai-skills.open-idea.net)
- [API Key Configuration](references/API-KEY.md)
- [Operations Contract](references/OPERATIONS.md)
- [HTTP Requests and Task Polling](references/HTTP-REQUESTS.md)
- [Trigger, Reconciliation, and Security Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires WORKFLOW_AUTOMATION_API_KEY and uses scoped workflow automation API operations.]

## Skill Version(s):

1.0.1 (source: server release evidence and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
