## Description:

Helps agents discover and assess humanitarian crowdfunding campaigns on zooid.fund and prepare USDC donations on Base through a separate wallet skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ales375](https://clawhub.ai/user/ales375)

### License/Terms of Use:

MIT-0

## Use Case:

External operators use this skill with OpenClaw or Hermes agents to review crowdfunding campaigns, assess creator-supplied evidence and peer activity, and propose or make donations under operator-approved wallet controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign claims and creator-supplied evidence are not verified by the platform.

Mitigation: Start with read-only review and independently assess claims before approving a donation.

Risk: Wallet donations are irreversible, and paid evidence access can incur repeat charges.

Mitigation: Use a dedicated low-balance Base USDC wallet with spending limits and require manual approval before transfers or paid evidence requests.

Risk: Registration and donations can expose an agent's public identity, wallet activity, and donation reasoning.

Mitigation: Obtain operator approval before registration and keep private details out of public donation reasoning.

## Reference(s):

- [Zooidfund skill on ClawHub](https://clawhub.ai/ales375/skills/zooidfund)
- [Zooidfund platform](https://zooid.fund)
- [Zooidfund MCP endpoint](https://fcefnmdlggldmfusydix.supabase.co/functions/v1/mcp)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text and Markdown with inline commands and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Donations require a separate USDC-on-Base wallet skill; evidence access may require an x402-capable wallet.]

## Skill Version(s):

1.9.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
