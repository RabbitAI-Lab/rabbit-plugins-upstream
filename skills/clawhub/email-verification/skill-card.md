## Description: <br>
Verify email addresses with the BounceBan API, including single and bulk verification for catch-all, accept-all, and SEG-protected emails, fast email or domain checks, credit and rate-limit management, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davis-lee](https://clawhub.ai/user/davis-lee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and go-to-market teams use this skill to verify individual email addresses, clean email lists, check deliverability risk, identify disposable, free, or role-based addresses, and manage BounceBan API credits and webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email addresses, domains, bulk lists, webhook payloads, and export links may contain sensitive personal or business data. <br>
Mitigation: Confirm permission and policy approval before verification, avoid regulated or highly sensitive datasets unless approved, use trusted HTTPS webhook endpoints, and treat CSV download URLs as temporary secrets. <br>
Risk: Repeated verification submissions can consume extra BounceBan credits or trigger rate limits. <br>
Mitigation: Poll existing verification or bulk task status instead of resubmitting in-flight work, retry waterfall timeouts as documented, and follow the endpoint rate limits. <br>
Risk: Bulk task deletion is irreversible. <br>
Mitigation: Confirm with the user before calling the bulk destroy endpoint. <br>


## Reference(s): <br>
- [BounceBan API documentation](https://bounceban.com/public/doc/api.html) <br>
- [Email Verification on ClawHub](https://clawhub.ai/davis-lee/skills/email-verification) <br>
- [Introduction](references/introduction.md) <br>
- [Single Verification](references/single-verification.md) <br>
- [Bulk Verification](references/bulk-verification.md) <br>
- [Check API](references/check.md) <br>
- [Account API](references/account.md) <br>
- [Webhooks](references/webhooks.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl commands and JSON API response interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BOUNCEBAN_API_KEY and curl; may produce BounceBan API requests, status polling guidance, webhook handling guidance, and CSV export link handling guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
