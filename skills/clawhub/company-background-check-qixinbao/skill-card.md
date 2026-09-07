## Description:

Generates Chinese company background-check reports from a bidding and procurement perspective, covering business profile, customers and suppliers, winning-bid strength, competitors, public-risk signals, and optional company comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to evaluate a company from public bidding and procurement data, including supplier/customer relationships, bidding strength, competitive overlap, and public-risk references. It supports single-company deep-dive reports and two-company comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company queries are sent to the vendor API.

Mitigation: Install only when users are comfortable sharing company names and query parameters with the vendor service.

Risk: The skill stores and uses an API key from the environment or a local home-directory config file.

Mitigation: Use least-privilege credential handling, avoid exposing keys in chat or reports, and review the local config location before deployment.

Risk: Reports can contain signed login-free company or announcement links.

Mitigation: Treat generated reports as shareable but sensitive artifacts and review recipients before distributing links.

Risk: The optional signup flow hashes and transmits a device MAC address after user consent.

Mitigation: Require explicit user consent before registration and skip auto-registration when a preconfigured API key is available.

Risk: Generated HTML reports should be treated cautiously until link escaping and URL validation are fixed.

Mitigation: Review generated HTML and avoid opening or sharing reports from untrusted or unvalidated input sources.

Risk: The skill can display contact data returned by the vendor API.

Mitigation: Display contact data only in the returned form, preserve masking, and avoid supplementing masked contacts from other sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/company-background-check-qixinbao)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [API quick reference](references/api-quick.md)
- [Workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun registration API](https://ai.zhiliaobiaoxun.com/web-api/)
- [Zhiliaobiaoxun agent portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report in chat with optional self-contained HTML report file and supporting JSON for rendering]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include signed source links, data citations, cost notes, and disclaimer text; generated HTML reports are written to a local report directory.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
