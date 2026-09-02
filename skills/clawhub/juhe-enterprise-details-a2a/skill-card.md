## Description:

Looks up detailed Chinese enterprise registration information from Juhe Data by company name, registration number, or unified social credit code through an Alipay-mediated paid flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve a structured enterprise profile for a specified Chinese company, including registration details, officers, shareholders, branches, change records, and abnormal-operation records. It is suited for business verification, counterparty checks, and lightweight due diligence where the user has confirmed the paid query.

### Deployment Geography for Use:

Global, subject to availability of Alipay payment and Juhe Data service access.

## Known Risks and Mitigations:

Risk: The lookup is paid and uses an Alipay-mediated payment flow.

Mitigation: Before payment, verify the company keyword, price, order details, and user order number.

Risk: Enterprise reports can include public sensitive identifiers such as officer names, shareholder names, addresses, registration numbers, and unified social credit codes.

Mitigation: Display and retain only the fields needed for the user's request, and avoid logging complete query text or full reports.

Risk: Third-party enterprise data may be delayed, incomplete, or unsuitable as the sole basis for a business or legal decision.

Mitigation: Present the report as reference information and advise verification against official registry sources for consequential decisions.

Risk: The user-provided enterprise identifier is sent to Juhe Data's API.

Mitigation: Send only the requested enterprise keyword to the fixed provider endpoint and do not attach personal, session, device, or marketing data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-details-a2a)
- [Juhe enterprise query endpoint](https://apis.juhe.cn/a2a/query)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown report with tables and concise payment or service-status guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes only provider-returned enterprise fields and omits raw signatures, raw JSON, and unsupported categories.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
