## Description: <br>
Draft-first e-commerce Gmail support: triage customer threads, verify order and policy context, and create auditable drafts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ecom-agent-tools](https://clawhub.ai/user/ecom-agent-tools) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
E-commerce merchants and support operators use this skill to triage Gmail customer-service threads, retrieve relevant order and policy context, and prepare auditable reply drafts. It is intended for owner-controlled support workflows with explicit setup, Gmail authorization, and human review before broader automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-access Gmail automation can affect customer communications and support records. <br>
Mitigation: Use a dedicated support mailbox or tightly scoped Gmail query, review draft-only results first, test manual-escalation cases, and enable automatic sending only for exact owner-approved categories. <br>
Risk: OAuth files, tokens, local memory, and category permissions may expose sensitive customer or merchant data if mishandled. <br>
Mitigation: Keep OAuth files and tokens out of the workspace, and periodically review or clear local memory and category-permission state. <br>
Risk: Public storefront discovery may collect candidate policy or product evidence that is stale or not applicable to a specific order. <br>
Mitigation: Use public storefront data only as candidate evidence, verify applicability against current authorized order and policy sources, and escalate uncertain cases for manual handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ecom-agent-tools/skills/ecommerce-gmail-customer-service) <br>
- [Server-resolved GitHub source](https://github.com/Ecom-Agent-Tools/Ecom-Agent-Tools/tree/main/awesome-skills-for-ecommerce/ecommerce-gmail-customer-service) <br>
- [Publisher profile](https://clawhub.ai/user/ecom-agent-tools) <br>
- [Project homepage](https://ecomagenttools.com) <br>
- [Onboarding guide](references/onboarding.md) <br>
- [Gmail operations](references/gmail-operations.md) <br>
- [Merchant data contract](references/merchant-data-contract.md) <br>
- [Storefront discovery](references/storefront-discovery.md) <br>
- [Reply playbooks](references/reply-playbooks.md) <br>
- [Learning workflow](references/learning-workflow.md) <br>
- [Research sources](references/research-sources.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Gmail drafts, masked JSON reports, Markdown guidance, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default draft-only Gmail workflow with owner-gated learning, memory use, scheduling, storefront discovery, and category-based sending controls.] <br>

## Skill Version(s): <br>
1.2.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
