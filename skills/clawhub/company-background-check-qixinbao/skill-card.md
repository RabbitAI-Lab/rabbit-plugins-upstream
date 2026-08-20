## Description:

This skill helps agents produce Chinese-language company background reports and company comparisons from public bid and tender data, including business profile, customers, suppliers, contract evidence, competitors, and public risk signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business teams use this skill to investigate a company, assess bid and tender history, identify customers and competitors, review public risk signals, or compare two companies. The skill is aimed at company due diligence from a bid-and-tender perspective rather than general corporate registry lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store an API key in local configuration and may create an account when no key is configured.

Mitigation: Review before installing if credential storage or account creation is not acceptable; prefer setting your own ZLBX_API_KEY manually.

Risk: Generated reports can be persistent HTML files and may contain login-free signed platform links.

Mitigation: Avoid sharing generated reports broadly; treat signed links as access-bearing URLs and remove reports when they are no longer needed.

Risk: The skill can request company contact details and display the contact data returned by the service.

Mitigation: Request contact details only for a legitimate business purpose and do not use other sources to complete masked contact information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/company-background-check-qixinbao)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [API quick reference](artifact/references/api-quick.md)
- [Workflow guide](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration guide](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Manual account registration](https://ai.zhiliaobiaoxun.com/?ch=s114)
- [Zhiliaobiaoxun agent platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown company intelligence report plus optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include sourced findings, data-boundary notes, disclaimers, and full output paths for generated HTML files.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
