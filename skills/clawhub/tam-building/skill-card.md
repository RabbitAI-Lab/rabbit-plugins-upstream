## Description:

Sources a Cargo account universe from AI Ark using an ICP-shaped filter, then tiers each company against a workspace rubric with rationale and evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

GTM operators, revenue teams, and developers use this skill to build and maintain a targeted account universe, size it before paid sourcing, and route companies into A, B, C, or disqualified tiers. It is intended for teams adapting Cargo CDK resources into their own workspace and reviewing cost gates before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changing Cargo CLI or cargo-cdk dependencies could alter behavior between review and installation.

Mitigation: Review and preferably pin the Cargo CLI and cargo-cdk dependency before installing or deploying the skill.

Risk: Placeholder ICP and rubric content could source or tier the wrong market.

Mitigation: Replace the placeholders with reviewed workspace context before deployment, and keep secrets out of those context markdown files.

Risk: Paid sourcing could exceed expectations if the plan, filter, limit, or cost estimate is not reviewed.

Mitigation: Use the count-first workflow, verify the deployment plan and cost estimates, and require explicit approval before approving any sourcing run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/tam-building)
- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Skill source homepage](https://github.com/getcargohq/gtm-skills/tree/main/tam-building)
- [Configure](references/configure.md)
- [Run](references/run.md)
- [Acceptance](evals/acceptance.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, TypeScript CDK resource changes, and JSON agent judgments.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent judgments return tier, rationale, and evidence_url; the play writes tier, tier_rationale, tier_evidence_url, and tiered_at to the sourced company row.]

## Skill Version(s):

0.3.0 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
