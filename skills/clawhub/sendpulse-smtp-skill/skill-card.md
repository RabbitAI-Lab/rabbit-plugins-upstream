## Description:

Guides agents in sending transactional and bulk email through SendPulse REST API or SMTP relay, including setup, troubleshooting, and deliverability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ymaievska-lang](https://clawhub.ai/user/ymaievska-lang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure SendPulse email access, send transactional email through its REST API or SMTP relay, and troubleshoot delivery and sender setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The guide's address-cleanup instructions may permanently delete email addresses.

Mitigation: Prefer reversible suppression; if deletion is necessary, approve a narrowly scoped deletion and recovery plan.

Risk: Weakening API IP restrictions can expose account access.

Mitigation: Keep the restriction enabled and allow only authorized server addresses.

Risk: Recipient addresses and attachments are sent to SendPulse.

Mitigation: Verify recipients and attachments before sending.

## Reference(s):

- [SendPulse SMTP API documentation](https://sendpulse.com/integrations/api/smtp)
- [SendPulse skills project homepage](https://github.com/sendpulse/sendpulse-skills/tree/main/sendpulse-smtp-skill)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup steps, API and SMTP examples, and troubleshooting guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
