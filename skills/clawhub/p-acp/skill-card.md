## Description:

Build and review private A2A commerce workflows with P-ACP packages, privacy boundaries, Solana settlement plans, and receipt proofs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kairomarkets](https://clawhub.ai/user/kairomarkets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold or review private agent-to-agent commerce integrations, select the appropriate P-ACP packages, model lifecycle and privacy boundaries, and plan Solana settlement through an external wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated commerce integrations could mishandle wallet authority or sensitive signing material.

Mitigation: Keep seed phrases, private keys, transaction signing, and broadcast outside the agent; prepare unsigned settlement plans for review by the consuming application's selected wallet.

Risk: Private negotiation content, deliverables, keys, or disclosure grants could leak through journals, receipts, logs, exceptions, or public output.

Mitigation: Bind encrypted payloads and disclosures to explicit sessions, recipients, grants, and expiry; publish only commitments, references, and approved disclosure fields.

Risk: A settlement plan could be mistaken for completed payment.

Mitigation: Report plan creation separately from funds movement and require verified chain evidence through the application's RPC path before claiming payment confirmation.

## Reference(s):

- [Package selection](references/package-selection.md)
- [Safety boundaries](references/safety-boundaries.md)
- [Workflow recipes](references/workflow-recipes.md)
- [Server-resolved GitHub source](https://github.com/KairoMarkets/p-acp/tree/main/skills/p-acp-agent-commerce)
- [ClawHub skill page](https://clawhub.ai/kairomarkets/skills/p-acp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with implementation notes and inline code or shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected packages, lifecycle and participant maps, privacy boundaries, settlement boundaries, tests, validation results, and remaining dependencies.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
