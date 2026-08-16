## Description:

Helps an agent request Cue-based cross-border legal and regulatory research, returning source-linked reports on statutes, regulatory requirements, legislative background, applicability boundaries, and compliance considerations across supported jurisdictions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, compliance, product, and business users can use this skill through an agent to research cross-border regulatory requirements in areas such as product market entry, privacy, export control, foreign investment review, tax, and employment compliance. The skill is intended for research support with source links, not privileged legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may be sent to Cue as an external research provider.

Mitigation: Do not include personal data, trade secrets, confidential business plans, or privileged legal advice requests unless the organization permits sending that information to Cue.

Risk: Regulatory research output may be incomplete, outdated, or unsuitable as legal advice.

Mitigation: Use source links for review and have qualified counsel validate conclusions before relying on them for legal or compliance decisions.

Risk: The workflow depends on Cue service availability, valid credentials, credits, and public data source access.

Mitigation: Run the documented health checks before use and fall back to official public legal sources when the external service is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-cross-border-regulation)
- [Cue skills runner](https://github.com/sensedeal/cue-skills)
- [Cue skills runner mirror](https://gitee.com/sensedeal/cue-skills)
- [EUR-Lex](https://eur-lex.europa.eu)
- [U.S. Code](https://uscode.house.gov)
- [eCFR](https://www.ecfr.gov)
- [Singapore Statutes Online](https://sso.agc.gov.sg)
- [Congress.gov](https://www.congress.gov)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research report with source links, plus setup and diagnostic shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language reports preserve key statute names and section numbers in the original language; Markdown reports may be saved locally and optionally converted to DOCX or PDF.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
