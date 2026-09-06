## Description:

Amazon ASIN 运营体检 helps Amazon sellers audit one ASIN with product-detail and review evidence, producing issues, supporting evidence, and prioritized operations actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to run a single-ASIN listing and operations audit from product details and Amazon review evidence. It is scoped to diagnosis and prioritized operating actions, not advertising execution, inventory, profit, or order accounting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an ARI account and API key.

Mitigation: Install only if the agent should access ARI account workflows, keep the key out of reports and prompts, and revoke or recreate the key from the ARI account page if access is no longer needed.

Risk: Paid ARI operations can spend credits, including analysis, collection, leaderboard, and advice workflows.

Mitigation: Review quotes before confirmed paid actions and turn autoconfirm off when every paid action should require explicit approval.

Risk: The skill can change ongoing account behavior through schedules, watches, competitors, and autoconfirm rules.

Mitigation: Confirm persistent changes with the account owner and periodically review active schedules, watches, competitors, and autoconfirm settings.

Risk: The skill can export reports or reviews to local files.

Mitigation: Choose export paths deliberately and review exported CSV, Markdown, or HTML files before sharing them outside the intended audience.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/asin-audit)
- [Operation Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown reports and concise guidance, with JSON CLI responses and optional CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid operations can spend ARI credits and should be quoted and confirmed according to the skill workflow.]

## Skill Version(s):

1.4.5 (source: evidence.release.version, artifact/SKILL.md frontmatter, artifact/_meta.json, and artifact/scripts/ari.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
