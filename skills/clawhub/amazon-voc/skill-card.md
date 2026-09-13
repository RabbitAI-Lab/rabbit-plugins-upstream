## Description:

Amazon Review Intelligence helps agents collect and monitor Amazon reviews through ARI, generate VOC and deep insight reports, compare competitors, surface review alerts, and produce listing and product-improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and market analysts use this skill to turn collected Amazon reviews into VOC findings, competitor comparisons, review alerts, and actionable listing or product recommendations. Agents can also guide setup, pricing confirmation, scheduled monitoring, and report or review exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI_BASE_URL can redirect authenticated ARI API requests and expose the ari_live API key if it points to an unintended endpoint.

Mitigation: Before use, ensure ARI_BASE_URL is unset or points only to the intended ARI service, and rotate the ARI API key if it may have been used with an untrusted endpoint.

Risk: The skill can initiate workflows that spend credits or change schedules, watches, competitors, alert state, workbench status, and exports.

Mitigation: Review any proposed action that changes account state or spends credits, and require explicit confirmation before running paid or state-changing commands.

Risk: ARI API keys could be exposed if copied into reports, examples, or shared documents.

Mitigation: Use ARI_API_KEY or the local user config file for credentials, and do not include API keys in generated reports, command examples, or public documentation.

## Reference(s):

- [Server-resolved source repository](https://github.com/funewa/Amazon-VOC)
- [ClawHub skill listing](https://clawhub.ai/funewa/skills/amazon-voc)
- [ARI CLI and API reference](references/reference.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown or text guidance with inline shell commands; CLI workflows may return JSON and export CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid collection, analysis, leaderboard, operations, and advise workflows require explicit user confirmation before execution.]

## Skill Version(s):

1.4.9 (source: server release evidence; artifact _meta.json lists 1.4.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
