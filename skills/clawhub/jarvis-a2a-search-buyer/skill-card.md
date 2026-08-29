## Description:

No-key web search for autonomous agents. One Jarvis call, paid per use with Base USDC x402; You.com routes first with automatic Exa fallback. Fixed maximum buyer price $0.012. No search-provider account or API key required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yl124915300-dot](https://clawhub.ai/user/yl124915300-dot)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and autonomous-agent operators use this skill to perform current public-web searches without provisioning You.com or Exa credentials, while capping each x402 Base USDC payment at $0.012.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize paid public-web search calls through the listed Jarvis router up to $0.012 USDC per search.

Mitigation: Install only when paid search is acceptable, and configure the buyer wallet or x402 client to enforce the stated maximum before funding.

Risk: Using the skill for free-search tasks, automated probing, or synthetic traffic can create avoidable cost and misuse risk.

Mitigation: Use it only for genuine current-web search needs, prefer free search tools when they meet the task, and avoid endpoint probing or promotional traffic.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yl124915300-dot/skills/jarvis-a2a-search-buyer)
- [Router manifest](https://jarvis-orderflow-router.yl124915300.workers.dev/.well-known/jarvis-a2a-router.json)
- [x402 buyer examples](https://jarvis-orderflow-router.yl124915300.workers.dev/integrations/x402-buyers.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline commands and machine-readable terminal status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Terminal outcome is SUCCESS or FAILED; the skill documents a hard maximum of 12000 atomic USDC ($0.012) per search.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
