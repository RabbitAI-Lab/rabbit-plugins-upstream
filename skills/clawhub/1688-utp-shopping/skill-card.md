## Description:

1688 UTP Shopping helps agents handle natural-language 1688 purchasing requests across product search, cart management, checkout, payment handoff, and order status flows through UTP MCP or CLI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1688aiinfra](https://clawhub.ai/user/1688aiinfra)

### License/Terms of Use:

Apache License 2.0

## Use Case:

External users and procurement-focused agents use this skill to search 1688 suppliers, compare products, manage carts, create checkout flows, and guide login or payment handoff for personal buying or bulk procurement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change agent host configuration, install or update a global UTP CLI, and enable an MCP connector.

Mitigation: Review installation prompts and host targets before running setup, and install only when those configuration changes are acceptable.

Risk: Reset options and update flows can affect local UTP state, including stored shopping preferences or pending binaries.

Mitigation: Treat reset and update prompts as sensitive actions, confirm user intent, and avoid reset paths unless the user explicitly asks for a fresh local setup.

Risk: Shopping, login, checkout, and payment handoff involve sensitive user decisions.

Mitigation: Require explicit user review for purchase, login, checkout, update, and reset steps, and rely on card-based confirmation where available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/1688aiinfra/skills/1688-utp-shopping)
- [UTP Official Site](https://ut-protocol.com)
- [Default UTP B2B Host](https://ucp-b2b.com)
- [Checkout and Ordering Guide](references/checkout-guide.md)
- [CLI Execution Guide](references/cli-guide.md)
- [Error Handling Guide](references/error-guide.md)
- [Feedback Guide](references/feedback-guide.md)
- [Installation Guide](references/install-guide.md)
- [Preferences Guide](references/preferences-guide.md)
- [Commercial Entity Registry](references/registry.md)
- [Update Guide](references/update-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with shell command blocks, JSON-style tool arguments, and concise user-facing text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May hand off purchase, login, checkout, and payment steps to UTP UI cards where the host supports MCP apps.]

## Skill Version(s):

2.0.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
