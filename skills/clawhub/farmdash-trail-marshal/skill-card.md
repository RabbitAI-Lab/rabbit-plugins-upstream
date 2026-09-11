## Description:

Use when composing multi-step DeFi workflows from FarmDash tools: plan, run, inspect supervised pipelines. Wallet steps stay policy-gated, preview-only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and DeFi workflow operators use this skill to choose named FarmDash recipes, check required sub-skills, separate read-only from state-changing steps, and track supervised workflow sessions. It supports planning and status coordination, while wallet-changing actions remain outside this skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake workflow plans or recipe metadata for financial advice.

Mitigation: Present plans as coordination guidance only and require the user to review financial decisions independently before any separately installed execution skill is used.

Risk: Live workflow features may send session metadata to FarmDash.

Mitigation: Use the public catalog or research-only planning when possible, and send session tokens or agent metadata only when the user chooses live workflow tracking.

Risk: Wallet-changing actions could be performed by companion execution skills after a plan is created.

Mitigation: Keep Trail Marshal out of execution paths and require each execution skill to present fresh quotes and obtain explicit user confirmation.

## Reference(s):

- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash Documentation](https://www.farmdash.one/docs)
- [FarmDash API Schema](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash MCP Server](https://www.farmdash.one/.well-known/mcp.json)
- [Canonical FarmDash Trail Marshal Skill](https://www.farmdash.one/openclaw-skills/farmdash-trail-marshal/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON-shaped tool outputs, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces workflow catalog guidance, quality-gate plans, guarded run records, and run-status summaries; it does not execute wallet transactions.]

## Skill Version(s):

0.1.9 (source: server release metadata; artifact frontmatter reports 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
