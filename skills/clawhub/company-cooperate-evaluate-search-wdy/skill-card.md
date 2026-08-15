## Description:

Evaluates whether a company is suitable as a customer, supplier, partner, or investment target using WenDaoYun company data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rose-develop](https://clawhub.ai/user/rose-develop)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and agents use this skill to search for a company, confirm the target entity, and produce a cooperation-risk assessment for customer, supplier, partnership, or investment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The WenDaoYun API key is sensitive and could be exposed if pasted into prompts, logs, or shared output.

Mitigation: Keep WENDAOYUN_API_KEY private in the environment and revoke it in the WenDaoYun platform if exposure is suspected.

Risk: Company search and evaluation queries are sent to WenDaoYun and may consume API quota.

Mitigation: Use the skill only for intended company-risk lookups, confirm the target company before detailed calls, and monitor quota usage.

Risk: The cooperation assessment can be incomplete, stale, or unsuitable as the sole basis for a business decision.

Mitigation: Treat the generated assessment as advisory and review the cited signals, limitations, and any supplementary materials before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rose-develop/skills/company-cooperate-evaluate-search-wdy)
- [WenDaoYun API key portal](https://open.wendaoyun.com/home)
- [fuzzy-search-org reference](references/fuzzy-search-org.md)
- [get-cooperate-evaluate reference](references/get-cooperate-evaluate.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise conclusions, key signals, limitations, and next actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-confirmed target company before detailed evaluation and avoids verbose raw data unless requested.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
