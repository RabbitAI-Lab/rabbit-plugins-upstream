## Description:

Rent a sandboxed Python runner, browser-based page fetcher, or small Linux home, paid by the hour in USDC on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drew-dot-com](https://clawhub.ai/user/drew-dot-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use it to run small Python jobs remotely, fetch JavaScript-rendered or access-restricted pages, and rent a Linux environment with persistent disk and SSH. Paid operations cost 0.007 USDC per hour and use funds supplied by the operator.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags the unpinned `npx -y charter-mcp` command because a future package release could differ from the reviewed version; the review was partial.

Mitigation: Use an exact reviewed version or an integrity-verified dependency, and restrict the client’s access.

Risk: The skill keeps its wallet key in a local file, and the rented home’s operator can read its disk.

Mitigation: Keep only what the rental needs in the wallet and transfer secrets directly with the documented `scp` method rather than through Charter.

Risk: Paid commands charge by the hour, provide no refund for unused time, and some refused busy calls may count toward the daily cap.

Mitigation: Check offers and wallet balance, confirm the cost before renting, and do not retry paid commands in a loop.

## Reference(s):

- [Charter service documentation and pricing](https://charter.mainnet.toonprotocol.dev/agents)
- [Charter machine-readable service guide](https://charter.mainnet.toonprotocol.dev/llms.txt)
- [ClawHub skill release](https://clawhub.ai/drew-dot-com/skills/charter-compute)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Text, Guidance]

**Output Format:** [Markdown instructions with shell commands; service responses are JSON containing execution output, fetched page text, or lease details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid remote operations are billed hourly; Python scripts are limited to 8 KiB and the documented environment includes NumPy.]

## Skill Version(s):

0.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
