## Description:

Xodo Sign lets an agent read, create, and update Xodo Sign data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Xodo Sign documents, templates, businesses, audit logs, signer reassignment, and reminders through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected-account access can expose business signing data through read actions.

Mitigation: Run only the requested read actions and avoid disclosing document, template, business, or audit data beyond the user's task.

Risk: Write actions can create documents, reassign signers, or send reminders from the connected Xodo Sign account.

Mitigation: Confirm the exact payload and effect with the user, including document, signer, recipient, and business context, before executing write actions.

## Reference(s):

- [Xodo Sign Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-eversign)
- [Xodo Sign homepage](https://eversign.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses include returned data and an execution identifier when commands are run.]

## Skill Version(s):

1.0.0 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
