## Description: <br>
Draft-first e-commerce Gmail support: triage customer threads, verify order and policy context, and create auditable drafts. Owners independently control ongoing draft-edit learning, existing long-term memory use, and category-based automatic sending. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ecomagenttools](https://clawhub.ai/user/ecomagenttools) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
E-commerce merchants and support operators use this skill to process a dedicated Gmail support inbox, classify customer requests, verify order and policy evidence, draft auditable replies, and optionally manage tightly gated automatic sending. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has high authority over a Gmail support workflow and can handle sensitive customer-service context. <br>
Mitigation: Run it only on a dedicated support mailbox or clearly scoped Gmail label/query, keep draft-only mode during testing, and review generated drafts before enabling sending. <br>
Risk: Automatic sending could send an incorrect or insufficiently reviewed response if enabled too broadly. <br>
Mitigation: Enable automatic sending only after validating the global switch and each independent category permission; keep unmatched, disabled, high-risk, or mixed-category cases as drafts. <br>
Risk: Local runtime state can contain redacted business memory and support workflow state. <br>
Mitigation: Treat the runtime directory as sensitive, keep OAuth credentials and tokens out of the repository and email content, and clear long-term memory only through explicit owner-confirmed commands. <br>
Risk: Public storefront discovery may provide incomplete or stale candidate evidence. <br>
Mitigation: Use storefront discovery as supplemental public evidence only; verify region, channel, effective date, order-time applicability, and authenticated order data before relying on it in replies. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ecomagenttools/skills/ecommerce-gmail-customer-service) <br>
- [EcomAgentTools Homepage](https://ecomagenttools.com) <br>
- [Onboarding Guide](references/onboarding.md) <br>
- [Gmail Operations](references/gmail-operations.md) <br>
- [Merchant Data Connection Contract](references/merchant-data-contract.md) <br>
- [Public Storefront Discovery](references/storefront-discovery.md) <br>
- [Learning Workflow](references/learning-workflow.md) <br>
- [Reply Playbooks](references/reply-playbooks.md) <br>
- [Research Sources and Applicable Boundaries](references/research-sources.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Shell commands, Configuration, Gmail drafts, Reports, Guidance] <br>
**Output Format:** [Markdown and text guidance with shell command blocks, Gmail draft content, labels, and masked JSON-style processing reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default operation creates drafts for review; sending requires owner-enabled global automatic-send plus matching per-category permissions.] <br>

## Skill Version(s): <br>
1.2.6 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
