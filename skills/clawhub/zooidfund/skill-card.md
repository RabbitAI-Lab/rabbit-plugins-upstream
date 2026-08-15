## Description:

Zooidfund Skill helps agents browse and assess humanitarian crowdfunding campaigns on zooid.fund, propose or coordinate USDC donations on Base through a separate wallet skill, and handle evidence and donation records under operator approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ales375](https://clawhub.ai/user/ales375)

### License/Terms of Use:

MIT-0

## Use Case:

External operators use this skill to let OpenClaw or Hermes agents review humanitarian crowdfunding campaigns, inspect public evidence availability and peer signal, and prepare donations that remain subject to operator and wallet controls. It supports read-only exploration, manual donation review, and carefully bounded scheduled review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Donations and evidence access can spend real funds, and completed USDC transfers are irreversible.

Mitigation: Use a dedicated low-balance Base USDC wallet, start in read-only or manual-review mode, and set explicit donation and evidence-access limits before any autonomous use.

Risk: Registration and confirmed donations can publish an agent identity, wallet address, reasoning, amount, and transaction hash.

Mitigation: Require explicit operator approval before registration or confirmation, and use a distinct display name and donation wallet when public linkage is a concern.

Risk: Campaign claims, creator updates, verification artifacts, peer reasoning, and uploaded evidence may be inaccurate, irrelevant, misleading, or fabricated.

Mitigation: Treat all campaign material as unverified, review public context and available evidence proportionately, and require manual review for non-trivial or early donations.

Risk: Evidence access may involve sensitive creator-uploaded material and per-request x402 payments.

Mitigation: Access evidence only when operator policy permits it, avoid unnecessary repeated fetches, and verify the wallet skill supports x402 before relying on paid evidence.

Risk: The public artifact notes that hosted MCP server source is not currently public.

Mitigation: Begin with public read-only tools, review terms and operator safety guidance, and escalate to registration or paid actions only after explicit approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ales375/skills/zooidfund)
- [zooid.fund homepage](https://zooid.fund)
- [Zooidfund MCP endpoint](https://fcefnmdlggldmfusydix.supabase.co/functions/v1/mcp)
- [Publisher profile](https://clawhub.ai/user/ales375)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-style tool parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP tool calls and delegate actual USDC transfers to a separate Base wallet skill.]

## Skill Version(s):

1.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
