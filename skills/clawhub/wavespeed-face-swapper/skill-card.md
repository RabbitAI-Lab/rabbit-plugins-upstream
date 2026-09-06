## Description:

Swap faces in images and videos using WaveSpeed AI, with multi-face targeting and automatic lighting and skin tone adaptation for consented, lawful, non-deceptive edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide consented face swaps in images or videos through WaveSpeed's CLI or MCP tools, including setup, parameter selection, price checks, and result retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads image or video media to WaveSpeed's cloud service, which can include identifiable likenesses.

Mitigation: Use it only for media the user has permission to edit and only when all identifiable people have consented to the face swap.

Risk: Face swapping can be misused for impersonation, deception, harassment, sexual content, or edits involving minors.

Mitigation: Refuse unclear or prohibited requests, including non-consensual likeness use, deceptive presentation, sexual or intimate material, and media involving children.

Risk: Setup installs third-party npm tooling that can store authentication locally and API usage can incur charges.

Mitigation: Use WaveSpeed login or environment-based authentication without asking for secrets in chat, verify sign-in status, and quote pricing before running paid jobs.

## Reference(s):

- [WaveSpeedAI Face Swapper on ClawHub](https://clawhub.ai/wavespeed/skills/wavespeed-face-swapper)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and WaveSpeed model parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce WaveSpeed output URLs when commands or MCP tools are run.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
