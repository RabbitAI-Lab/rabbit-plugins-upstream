## Description:

Captures forecast errors, supplier risks, logistics delays, inventory mismatches, quality deviations, and demand signal shifts to enable continuous supply chain improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Supply chain, procurement, logistics, inventory, quality, and demand-planning teams use this skill to capture operational disruptions and recurring patterns as structured markdown learning logs. Agents can use it to document stockouts, delivery misses, supplier lead-time changes, forecast variance, quality issues, capacity breaches, and related improvement requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project-local supply-chain learning logs may include sensitive supplier, pricing, contract, or customer-identifiable order information if users enter raw operational data.

Mitigation: Follow the skill guidance to use aggregated metrics and redacted summaries, and avoid proprietary supplier pricing, negotiated contract terms, and customer-identifiable order data.

Risk: Optional hooks run with the same permissions as the agent and may add reminders based on prompts or Bash output.

Mitigation: Keep hooks project-scoped, enable only the needed hooks, prefer the UserPromptSubmit reminder by default, and avoid the optional Bash-output detector unless disruption detection is needed.

Risk: Promoting logged patterns into agent instructions, generated skills, or operational standards can introduce incorrect or misleading guidance.

Mitigation: Review proposed edits and generated skills before applying them, and scan the skill before deployment.

## Reference(s):

- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Entry Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project-local learning logs and reminder text; optional hooks are opt-in and project-scoped.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
