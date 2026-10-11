## Description:

Helps teams deploy a Cargo agent that replies to leads in existing email threads and checks unanswered threads for a single follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales-development teams and GTM engineers adapt and deploy an agent that continues lead conversations from a workspace mailbox, responds to replies, respects opt-outs, and checks quiet threads for at most one follow-up. The example has not yet been verified in a live workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inbound lead emails can influence an agent authorized to send from a real workspace mailbox.

Mitigation: Test with your own mailbox, monitor early sends, and consider human approval or deterministic send guards before contacting external leads.

Risk: Automated outreach could reach contacts the team is not authorized to email or continue after an opt-out.

Mitigation: Use only permitted contacts, verify unsubscribe handling in a test thread, and monitor for unwanted follow-ups.

Risk: Deploying a mailbox incurs recurring charges, while registering a new domain may incur a separate charge.

Mitigation: Review the deployment plan and current prices, and obtain explicit approval before deploying.

## Reference(s):

- [Conversation loop reference](references/loop.md)
- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/agentic-engagement)
- [Project homepage listed in ClawHub metadata](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Email text]

**Output Format:** [TypeScript configuration, Markdown guidance, and threaded email replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One email per wake, with at most one unanswered follow-up; deployment requires operator approval.]

## Skill Version(s):

0.1.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
