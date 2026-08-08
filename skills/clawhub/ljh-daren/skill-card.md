## Description:

Influencer account diagnosis tool that screens creator accounts with a six-dimension scorecard, runs a three-part anti-fraud check, and returns a partner, negotiate, request-more-data, or pass recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomeng](https://clawhub.ai/user/handsomeng)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and ecommerce operators use this skill to decide whether an influencer account is worth entering quotation and collaboration discussions. It asks for account, traffic, engagement, audience, commerce, and price data, then produces a structured screening report and cooperation recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read and update local business archive files and create an onboarding marker in the user's home directory.

Mitigation: Review archive behavior before installation, run in a workspace where local file writes are acceptable, and decline archive creation when records should not be persisted.

Risk: The generated diagnosis can affect influencer spending decisions and may be wrong if required traffic, audience, commerce, or anti-fraud data is missing or inaccurate.

Mitigation: Require the report to mark missing dimensions as pending verification and have a human review source data before committing budget.

Risk: The artifact includes off-platform promotional contact handles in onboarding text.

Mitigation: Review onboarding text against marketplace and organizational policies before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomeng/skills/ljh-daren)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Guidance]

**Output Format:** [Markdown screening report with tables and recommendation labels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local ljh archive files when the user accepts archive behavior.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter lists 0.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
