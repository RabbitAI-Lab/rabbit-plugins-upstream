## Description:

Reviews contract clauses from a specified party's perspective and returns a risk-graded checklist with suggested revisions and references to relevant laws or cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, procurement, and business teams use it to review draft contracts from their side's perspective, identify clause and party risks, and prepare suggested edits. A licensed lawyer should review the results before signing; they are not formal legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contract files are sent to an external service, and the skill's privacy and retention claims are unclear.

Mitigation: Before uploading confidential contracts, confirm Cue's storage, sharing-link access, and deletion rules; use redacted material until these are clear.

Risk: Setup automatically downloads and runs an external runner without pinning its version.

Mitigation: Review and pin the runner version and restrict its access to only the files and resources needed.

Risk: The API key is saved for service access, and runs can consume paid credits.

Mitigation: Protect the key and check credit charges and balances before running a review.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-contract-risk-review)
- [CueCue API key setup](https://cuecue.cn/api-key?src=clawhub-contract-risk-review)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with a risk-ranked checklist and suggested contract revisions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cited legal provisions or case identifiers; not a substitute for a lawyer's review.]

## Skill Version(s):

1.1.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
