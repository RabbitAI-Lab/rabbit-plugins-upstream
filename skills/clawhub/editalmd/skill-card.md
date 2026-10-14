## Description:

Helps agents research Brazilian public procurement through EditalMD, including tender searches, deadlines, prices, document review, alerts, and watches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

Suppliers and procurement researchers use this skill to find Brazilian public tenders, assess deadlines and winning prices, read tender requirements, and monitor purchases.

### Deployment Geography for Use:

Brazil

## Known Risks and Mitigations:

Risk: Document processing and some alerts or watches may use paid access or prepaid credits.

Mitigation: Show the quoted cost and obtain user approval before paid access; let the user make purchases on the site.

Risk: Estimated challenge deadlines and automatically extracted requirements may be incomplete or inaccurate.

Mitigation: Confirm deadlines and requirements against the original tender and check document coverage before relying on a dossier.

Risk: Alert owner tokens, prepaid credit tokens, and document access codes grant access to private or paid features.

Mitigation: Keep tokens and access codes secret and avoid including them in files, logs, or responses.

## Reference(s):

- [EditalMD on ClawHub](https://clawhub.ai/wrpbr/skills/editalmd)
- [EditalMD API reference](https://editalmd.com/llms-full.txt)
- [EditalMD pricing](https://editalmd.com/pricing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text and Markdown summaries of procurement records and tender documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source and page evidence, estimated deadlines, and alert or watch results.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
