## Description:

Recommends comparable Xiaohongshu accounts for creators, operators, brands, and MCNs using an account ID or niche, follower count, and account level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, content operations teams, MCNs, and brands use this skill to find same-tier Xiaohongshu benchmark accounts and higher-tier reference accounts for account growth, content planning, and KOL screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports that queries and the API key are sent to RedFox while TLS certificate verification is disabled, which can allow credential interception or response tampering.

Mitigation: Use only after the publisher restores TLS certificate verification; rotate any API key used with an unverified connection.

Risk: Xiaohongshu account IDs, targeting criteria, and generated JSON/HTML reports may expose business or creator research locally or to redfox.hk.

Mitigation: Share only data approved for RedFox processing, store generated reports in an appropriate location, and delete reports when no longer needed.

Risk: The security guidance says the documentation should clarify that the skill calls a remote API despite not using web search and should fix the documented script path.

Mitigation: Review the remote API behavior and invoke the actual bundled script path before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/xiaohongshu-similar-account)
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFox similar accounts API](https://redfox.hk/story/api/xhsUser/querySimilarAccounts)
- [HTML report template](artifact/references/account_template.html)

## Skill Output:

**Output Type(s):** [text, markdown, html, json, guidance]

**Output Format:** [Markdown tables and analysis text, plus generated local JSON and HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY and sends Xiaohongshu account IDs or targeting criteria to redfox.hk.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
