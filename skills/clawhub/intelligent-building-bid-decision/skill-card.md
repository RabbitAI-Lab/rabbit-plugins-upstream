## Description:

This skill helps bid teams evaluate weak-current and intelligent-building security monitoring tenders by analyzing whether to bid, buyer history, incumbent suppliers, likely competitors, pricing benchmarks, qualification thresholds, and rejection risks from public bidding data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams, security monitoring contractors, and intelligent-building system integrators use this skill to decide whether to participate in a specific tender and to prepare a data-backed bidding posture. It produces a decision report covering buyer behavior, competitor signals, comparable award prices, suggested pricing bands, qualification constraints, and data gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration can send a device-linked MAC-address hash and store the returned API key locally.

Mitigation: Prefer a user-supplied ZLBX_API_KEY; only approve automatic registration after reviewing the privacy notice, and protect the local API key configuration file.

Risk: Project names, company names, and related search terms are sent to ZLBX services during analysis.

Mitigation: Avoid entering confidential or non-public bidding information unless disclosure to the service is acceptable.

Risk: Generated HTML reports are flagged for unsafe link handling when report data may come from untrusted sources.

Mitigation: Review generated HTML before sharing or opening it in higher-trust contexts, and treat links from report data cautiously until URL escaping and validation are fixed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/intelligent-building-bid-decision)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [API Quick Reference](artifact/references/api-quick.md)
- [Workflow Guide](artifact/references/workflow.md)
- [Report Template](artifact/references/report-template.md)
- [Auto Registration Guide](artifact/references/auto-register.md)
- [ZLBX API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZLBX Skill Documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report in conversation, with optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public bidding-data citations when available; complete mode estimates 12-25 API calls and quick mode estimates 5-8 API calls.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
