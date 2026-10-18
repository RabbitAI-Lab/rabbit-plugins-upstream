## Description:

Helps deploy an AI agent that manages lead email conversations from a workspace-owned mailbox, responding to replies and checking unanswered threads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales-development teams and developers use this skill to configure and deploy a lead-conversation agent on a workspace-owned email domain and mailbox. The agent can reply in-thread, check for replies or opt-outs, and send at most one unanswered follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated external email could reach leads without appropriate permission or continue after an opt-out.

Mitigation: Confirm a lawful basis and recipient consent, review unsubscribe handling, and test stop conditions before enabling sends.

Risk: Lead correspondence and thread-status data may require privacy and retention controls.

Mitigation: Review access, data retention, and mailbox handling for lead conversations before deployment.

Risk: Provisioning a mailbox incurs recurring charges and deployment can create external resources.

Mitigation: Check the live mailbox price and deployment plan, quote recurring costs, and obtain explicit approval before applying it.

## Reference(s):

- [Conversation loop reference](references/loop.md)
- [Declared skill homepage](https://github.com/getcargohq/gtm-skills/tree/main/agentic-engagement)
- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/agentic-engagement)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown guidance with TypeScript and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires adaptation to a workspace-owned domain, a real mailbox identity, and an authenticated language-model connector before deployment.]

## Skill Version(s):

0.1.2 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
