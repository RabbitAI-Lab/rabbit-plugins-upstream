## Description:

A Chinese-language Guangzhou-focused limited liability company registration advisor that supports customer Q&A, internal advisor answers, and draft Word-ready registration plan content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xtoyun](https://clawhub.ai/user/xtoyun)

### License/Terms of Use:

MIT-0

## Use Case:

External customers use the skill to understand whether and how to register a Guangzhou limited liability company, including name, capital, scope, address, fees, timelines, and post-registration obligations. Internal advisors use it to collect client facts and draft structured company-registration plan content for review and Word delivery.

### Deployment Geography for Use:

Guangzhou, Guangdong, China

## Known Risks and Mitigations:

Risk: The skill may collect business, shareholder, legal representative, phone, and address details when drafting formal plans.

Mitigation: Use the skill only in an authorized advisor workflow, collect only needed details, and handle client data under the organization's privacy and retention rules.

Risk: Company registration, tax, fee, timeline, and permit guidance can become outdated or vary by district, agency, bank, or client facts.

Mitigation: Verify official fees, timelines, permit requirements, and legal or tax advice independently before filing, quoting, or delivering a formal plan.

Risk: A drafted plan or quote could contain unconfirmed client facts, licensing assumptions, or pricing that should not be sent directly to customers.

Mitigation: Require advisor review before delivery, use the maintained pricing configuration for formal quote content, and mark unresolved facts as pending confirmation.

Risk: Users may ask for improper conduct such as false invoicing, concealing income, capital withdrawal, forged materials, or unlicensed operations.

Mitigation: Refuse procedural help for unlawful actions, provide only high-level risk warnings, and route complex legal or tax issues to qualified professionals.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xtoyun/skills/gz-reg-company)
- [Artifact README](artifact/README.md)
- [Skill workflow](artifact/SKILL.md)
- [Intake fields](artifact/references/intake-fields.md)
- [Guangzhou parameters](artifact/references/guangzhou-params.md)
- [Naming, capital, scope, and equity guidance](artifact/references/naming-capital-scope.md)
- [Permit map](artifact/references/permit-map.md)
- [Risk and zero-declaration guidance](artifact/references/risk-zero.md)
- [Deliverable specification](artifact/references/deliverable-spec.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Chinese-language conversational answers and structured Markdown content suitable for Word document generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request business, shareholder, legal representative, phone, and address details in advisor workflows; customer-facing answers should use ranges and official-verification caveats.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
