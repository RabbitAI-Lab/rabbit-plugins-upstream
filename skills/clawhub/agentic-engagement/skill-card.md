## Description:

Deploys a Cargo CDK example for an agent that holds email conversations with leads from a workspace-owned mailbox, waking on replies, unsubscribes, and heartbeat status checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and go-to-market engineers use this skill to add a bounded email conversation agent to a Cargo workspace. It provides the domain, mailbox, send-email tool, native email reply/unsubscribe trigger, heartbeat, prompts, and checks needed to adapt and review the deployment before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outbound lead outreach can create compliance or consent issues if used without a lawful basis or without honoring opt-outs.

Mitigation: Confirm outreach basis and applicable email/privacy rules before deployment, and preserve the unsubscribe and stop conditions described by the skill.

Risk: Domain registration and mailbox creation can incur non-refundable or recurring workspace credit charges.

Mitigation: Review `cargo-ai cdk plan`, quote live pricing from `cargo-ai mailboxManagement pricing get`, and get explicit approval before deploying chargeable resources.

Risk: Using the wrong mailbox or exposing `mailboxUuid` as an agent input can split the send path from the trigger path.

Mitigation: Keep the send-email tool pinned to the declared mailbox and run the contract check before deployment.

Risk: Missing `inReplyTo` or an incomplete `references` chain can break email threading.

Mitigation: Require threaded replies to include `inReplyTo` and the full references chain, then verify with a test thread sent to the operator's own address.

## Reference(s):

- [Conversation Loop Reference](references/loop.md)
- [Agentic Engagement Homepage](https://github.com/getcargohq/gtm-skills/tree/main/agentic-engagement)
- [Cargo GTM Skills](https://github.com/getcargohq/gtm-skills)
- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/agentic-engagement)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with TypeScript Cargo CDK files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes acceptance checks and deployment review steps; generated resources must be adapted to the user's Cargo workspace before deployment.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
