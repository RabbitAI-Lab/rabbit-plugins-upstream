## Description: <br>
检查网站301重定向配置是否正确 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaomeng-agi](https://clawhub.ai/user/xiaomeng-agi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
SEO practitioners, site owners, and developers use this skill to submit 301 redirect check requirements or URL data to XiaoMeng AGI's paid service and receive analysis, recommendations, and an action plan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User requests, credentials, and submitted data are sent to an external XiaoMeng AGI API. <br>
Mitigation: Do not submit private logs, credentials, internal URLs, business data, or reusable secrets unless approved for third-party processing. <br>
Risk: The result retrieval script accepts a credential as a shell argument. <br>
Mitigation: Use only short-lived payment credentials and avoid entering reusable secrets in shared shells or logs. <br>
Risk: The skill is presented as a narrow 301 redirect checker but operates as a paid remote analysis client. <br>
Mitigation: Confirm cost, data-sharing expectations, and output scope before invoking the scripts, and validate results before applying SEO changes. <br>


## Reference(s): <br>
- [API Reference - 301重定向检查](references/api-reference.md) <br>
- [XiaoMeng AGI API Homepage](https://xiaomeng-api.qisir.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/xiaomeng-agi/skills/301-redirect-check) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown-style analysis text and JSON API responses surfaced through shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid remote API workflow; order creation precedes result retrieval after payment.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
