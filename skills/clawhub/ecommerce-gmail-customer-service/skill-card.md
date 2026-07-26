## Description: <br>
Safely triage e-commerce customer-service Gmail threads: classify requests, match products and orders, check campaigns and policies, and create auditable reply drafts with escalation safeguards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ecom-agent-tools](https://clawhub.ai/user/ecom-agent-tools) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Merchant support teams use this skill to process Gmail customer-service threads for e-commerce stores. It prepares auditable draft replies by classifying requests, matching product and order evidence, checking merchant policies and campaigns, and escalating cases that require human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires sensitive Gmail and merchant-service access. <br>
Mitigation: Install it only for a dedicated support mailbox, keep credentials out of the repository, and use authorized merchant connectors with the minimum required permissions. <br>
Risk: Full Gmail authorization can read, label, draft, and potentially send mail if later enabled. <br>
Mitigation: Keep draft-only mode until testing is complete; enable sending only after explicit authorization and successful automatic sending gates. <br>
Risk: Historical customer-service email learning may expose private customer data if mishandled. <br>
Mitigation: Run learning only after explicit user consent and store only redacted summaries in user_memory.md, not original emails, attachments, identifiers, payment data, or mailbox exports. <br>
Risk: Public storefront data can be stale or insufficient for customer-specific decisions. <br>
Mitigation: Treat public pages as candidate evidence and verify region, channel, product, effective date, order-time applicability, and authenticated order or policy sources before using them in replies. <br>
Risk: The default persona may not be appropriate for every business. <br>
Mitigation: Review and replace the editable runtime persona with business-appropriate traits during setup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ecom-agent-tools/skills/ecommerce-gmail-customer-service) <br>
- [Project homepage](https://ecomagenttools.com) <br>
- [Guided setup](references/onboarding.md) <br>
- [Gmail operating instructions](references/gmail-operations.md) <br>
- [Merchant data connection contract](references/merchant-data-contract.md) <br>
- [Public storefront discovery](references/storefront-discovery.md) <br>
- [Reply playbooks](references/reply-playbooks.md) <br>
- [Intent taxonomy](references/intent-taxonomy.csv) <br>
- [User email learning workflow](references/learning-workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates Gmail drafts by default, applies status labels, and produces masked processing reports when batch processing is used.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
