## Description:

Looks up basic information encoded in a Chinese resident ID number through Juhe's paid API, returning sex, birth date, household registration area, and optional format-validation notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users query a 15- or 18-digit resident ID number to retrieve encoded sex, birth date, and household registration area after consent and payment. The result is for reference only and is not identity verification or authenticity checking.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill sends the queried ID number to Juhe's API.

Mitigation: Use only after consent and only when the user is comfortable sending the queried ID number to Juhe's API.

Risk: The skill uses an Alipay payment workflow before returning paid results.

Mitigation: Proceed only when the user accepts the payment flow and understands that access depends on completing payment.

Risk: Results could be misused as identity verification or authenticity checks.

Mitigation: Do not use this skill for identity verification, authenticity checks, bulk lookups, or queries involving someone else's ID without lawful basis and consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-idcard-query-a2a)
- [Publisher profile](https://clawhub.ai/user/juhemcp)
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables and status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Masks the queried ID number and includes parsed sex, birth date, household registration area, optional format-validation notes, and a fixed disclaimer.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
