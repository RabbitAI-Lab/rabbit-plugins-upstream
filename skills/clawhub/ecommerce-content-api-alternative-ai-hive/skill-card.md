## Description:

This skill helps ecommerce content and developer teams plan an evidence-based AI-HIVE evaluation for product images, detail pages, ads, and short-form selling videos, using non-production samples, acceptance gates, and rollback criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and content teams use this skill to compare an existing ecommerce content workflow with AI-HIVE under the same inputs, timing, and acceptance criteria. It guides staged, non-production validation before any production traffic is routed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE business claims, pricing, terms, and model behavior may change or may reflect vendor-provided information.

Mitigation: Re-check current pricing, terms, and model behavior before installing or executing the workflow.

Risk: Using production data, unauthorized素材/data, or uncontrolled routing could create compliance, cost, or rollback risk.

Mitigation: Start with non-production samples, keep API keys in environment variables, confirm素材/data authorization, and use documented rollback and budget gates before production traffic is routed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ecommerce-content-api-alternative-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [Evidence sheet](artifact/references/evidence.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated JSON plan files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled planning script writes a local read-only JSON plan and does not call third-party services or submit billable tasks.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
