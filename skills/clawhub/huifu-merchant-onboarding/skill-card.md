## Description: <br>
Guides developers integrating Huifu merchant onboarding for enterprise and individual merchant KYC, image upload, business activation or modification, merchant data changes, rate queries, status changes, SMS verification, detail queries, application status, and onboarding notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huifu](https://clawhub.ai/user/huifu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integration engineers use this skill to identify the correct Huifu onboarding interface, load the right reference files, and produce field-checked guidance, DTOs, configuration notes, or guarded implementation snippets for merchant onboarding workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated guidance can touch sensitive merchant onboarding, identity, bank-account, credential, and account-management workflows. <br>
Mitigation: Use the skill only for intended Huifu onboarding work, keep credentials and merchant materials in server-side secure storage, avoid logging or front-end exposure, and review generated runnable code before use. <br>
Risk: The artifact identifies unsafe SDK paths for Java and PHP transport security, debug logging, and local file upload behavior. <br>
Mitigation: Keep those paths blocked for integration or production code until fixed or verified safe, and require explicit confirmation before producing runnable implementations. <br>
Risk: Payment transaction, refund, reconciliation, checkout, or payment-final-state tasks may be confused with merchant onboarding. <br>
Mitigation: Route payment workflows to the payment integration skill and keep this skill limited to onboarding, merchant-management, and related status workflows. <br>
Risk: Notification envelopes, ACK behavior, retry semantics, and some local image-upload protocol details are not fully confirmed. <br>
Mitigation: Mark those areas as needing official confirmation and avoid generating callback or upload implementations when the required protocol evidence is missing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huifu/skills/huifu-merchant-onboarding) <br>
- [Official service source index](references/official-service-source-index.md) <br>
- [Merchant onboarding overview](references/shared-overview.md) <br>
- [Merchant onboarding field contracts](references/merchant-onboarding-field-contracts.md) <br>
- [Complete merchant onboarding field catalog](references/merchant-onboarding-complete-field-catalog.md) <br>
- [Credential and sensitive-material boundary](references/shared-credential-boundary.md) <br>
- [Server SDK capability matrix](references/shared-server-sdk-matrix.md) <br>
- [Skill version policy](references/skill-version-policy.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with field tables, checklists, code blocks, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hard-stop questions and [需要官方确认] markers when required protocol evidence is missing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact version policy) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
