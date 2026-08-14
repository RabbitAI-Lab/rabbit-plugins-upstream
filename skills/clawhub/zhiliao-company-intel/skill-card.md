## Description:

Generates company background intelligence reports from a bidding and procurement perspective, including business profile, customer and supplier relationships, award history, competitor overlap, public-risk notes, and a shareable local HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, business teams, procurement teams, and analysts use this skill to assess a named company through public bidding data, compare two companies, and generate concise due-diligence reports. The skill is designed for company-level background checks, supplier qualification review, competitor analysis, and lightweight commercial due diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may contain sign-in-bypass links intended for report viewing.

Mitigation: Share generated reports only with trusted recipients and treat embedded platform links as sensitive.

Risk: The skill stores account credentials for API access.

Mitigation: Prefer a preconfigured ZLBX_API_KEY, keep credential files private, and rotate the key if it is exposed.

Risk: Company contact lookups can expose business contact information.

Mitigation: Request contact lookups only for legitimate business needs and preserve the backend-provided masking or access tier.

Risk: Company background conclusions can be misleading if treated as definitive business or legal judgments.

Mitigation: Use the skill's cited data boundaries and public-source links, and independently verify important findings before making decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-company-intel)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Automatic registration flow](artifact/references/auto-register.md)
- [ZLBX API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Zhiliao business intelligence portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report in chat plus a generated self-contained HTML report file; may also prepare JSON input for the bundled report renderer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a ZLBX_API_KEY credential, may call Zhiliao Biaoxun APIs and WebSearch, and writes generated HTML reports to a local output directory.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
