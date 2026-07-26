## Description: <br>
Design, scaffold, validate, and review ClinkBill/Clink payment integrations, including clink-integ-cli usage, local clink login Secret Key bootstrap, browserless manual Secret Key setup, webhook endpoint automation, product/price/subscription catalog import, checkout and subscription APIs, webhook signature verification, sandbox validation, new user onboarding, merchant skill integrations, and documentation-backed contracts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clink](https://clawhub.ai/user/clink) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to plan, implement, validate, and review ClinkBill payment integrations. It supports checkout and subscription APIs, bundled CLI workflows, webhook automation, sandbox validation, new-user onboarding, and merchant skill payment handoff designs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill and bundled CLI may access or persist Clink payment credentials and merchant configuration. <br>
Mitigation: Prefer sandbox use, store credentials through env: references or a real secret manager, and avoid literal saved keys. <br>
Risk: Webhook and environment-file automation can write or rotate payment secrets. <br>
Mitigation: Review webhook and env-file writes before running them, and write revealed secrets only to controlled secret destinations. <br>
Risk: Broad local or payment-side actions can affect merchant integration state. <br>
Mitigation: Do not use --restart-command or production skip-validation unless you explicitly approve the exact action. <br>


## Reference(s): <br>
- [Clink Integ Skills on ClawHub](https://clawhub.ai/clink/skills/clink-integ-skills) <br>
- [README](README.md) <br>
- [Clink Integ CLI Integration](references/clink-integ-cli-integration.md) <br>
- [Standard Integration](references/standard-integration.md) <br>
- [Elements Integration](references/elements-integration.md) <br>
- [New User Onboarding](references/new-user-onboarding.md) <br>
- [Merchant Skill for Generic Agent Integration](references/generic-agent-integration.md) <br>
- [Merchant Skill for OpenClaw Integration](references/agent-integration.md) <br>
- [Validation Workflow](references/validation-workflow.md) <br>
- [Output Artifacts](references/output-artifacts.md) <br>
- [Official Clink Docs Export](https://docs.clinkbill.com/llms-full.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code, shell commands, JSON snippets, checklists, and validation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce developer-facing implementation plans, contracts, checklist artifacts, and validation reports.] <br>

## Skill Version(s): <br>
2.0.0 (source: ClawHub release evidence, released 2026-07-02) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
