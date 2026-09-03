## Description:

A background accountability loop that surfaces fresh, high-scoring RedReplier lead opportunities and relays server-generated marketing nudges until the user acts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to receive scheduled RedReplier lead notifications and act on fresh marketing opportunities. Host agents can also help configure the RedReplier criteria and relay approve or reject triage back to the service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and reuses a RedReplier API token for background polling.

Mitigation: Use a dedicated, revocable token, keep the config file private, and rotate or revoke the token if exposure is suspected.

Risk: Each poll changes RedReplier server state and can consume a lead if output is discarded.

Mitigation: Only run scheduled polling when its non-empty output is delivered to the user.

Risk: Approve and reject triage calls update a RedReplier mention-status endpoint that is not included in the declared network permission path.

Mitigation: Review the undeclared status-changing endpoint before enabling triage behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tarasshyn/skills/redreplier-mean-marketer)
- [RedReplier](https://redreplier.com)
- [RedReplier API Host](https://ai.redreplier.com)
- [Publisher Profile](https://clawhub.ai/user/tarasshyn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text and Markdown with inline shell commands; poll commands can return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Notify output is empty when there is nothing to send; non-empty output should be delivered to the user as-is.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
