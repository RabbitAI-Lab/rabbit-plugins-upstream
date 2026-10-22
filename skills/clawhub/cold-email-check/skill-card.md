## Description:

Checks if a cold email to a specific address is legal before you send it (UK, US, Canada, Germany, France, Australia, Ireland, Netherlands), with a receipt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gabrielaoimevbore-beep](https://clawhub.ai/user/gabrielaoimevbore-beep)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and outreach teams use this skill to check whether a proposed cold email to a specific address is permitted under the supported rules before deciding whether to send it. It returns a verdict and receipt; it does not write or send the email.

### Deployment Geography for Use:

Senders based in the United Kingdom or United States; recipient rules cover the UK, US, Canada, Germany, France, Australia, Ireland, and the Netherlands.

## Known Risks and Mitigations:

Risk: A check sends the recipient address or domain and supplied outreach facts to Precleared; receipt IDs can expose check details.

Mitigation: Review Precleared's privacy and retention terms, use --dry-run to preview submissions, and keep receipt IDs private.

Risk: Eligibility results may be incomplete or mistaken and are not a legal guarantee.

Mitigation: Supply accurate, non-guessed facts and treat blocked, unknown, or failed checks as a reason not to send until resolved.

## Reference(s):

- [Precleared Cold Email Check on ClawHub](https://clawhub.ai/gabrielaoimevbore-beep/skills/cold-email-check)
- [Precleared](https://precleared.dev)
- [Precleared API documentation](https://precleared.dev/docs)
- [Precleared rules and sources](https://precleared.dev/rules)

## Skill Output:

**Output Type(s):** [JSON, CSV, JSONL, Guidance]

**Output Format:** [JSON verdicts and receipts for a single check; annotated CSV or JSONL results for batch checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes verdict, send eligibility, next steps, and receipt details; batch results retain the input rows.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
