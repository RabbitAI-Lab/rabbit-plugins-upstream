## Description:

AI-powered wealth advisor for bank mobile apps offering personalized product matching, investment consultation, and compliance-compliant customer interaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Digital banking teams and wealth management advisors use this skill to draft bank mobile app product-matching logic, customer-facing wealth advisory text, and compliance checks. It is oriented toward China commercial banking contexts and outputs should be reviewed by qualified advisory and compliance staff before use.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Customer profiles can contain sensitive financial personal information such as risk preference, asset size, holdings, and transaction intent.

Mitigation: Use anonymized or synthetic profiles for design and testing, and do not paste real customer names, account numbers, IDs, full holdings, or live transaction data into general chat.

Risk: Draft advisory language or product-matching output could be mistaken for personalized financial, legal, or insurance advice.

Mitigation: Treat outputs as drafts only and require review by qualified advisory and compliance staff before customer-facing or real-world use.

Risk: Regulatory summaries and compliance wording may become outdated or may not match an institution's current policy.

Mitigation: Verify recommendations, disclosures, and workflow requirements against official current regulators' guidance and the deploying institution's compliance rules.

Risk: Illustrative Python snippets describe matching logic but are not a production implementation.

Mitigation: Adapt, test, and harden any implementation separately, including suitability validity checks, over-risk blocking or special confirmation, concentration controls, logging, and traceability.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code]

**Output Format:** [Markdown and text with illustrative Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory drafts and reference material requiring qualified human review before customer-facing or real-world use.]

## Skill Version(s):

3.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
