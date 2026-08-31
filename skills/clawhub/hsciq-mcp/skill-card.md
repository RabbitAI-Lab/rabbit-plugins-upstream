## Description:

Provides HSCIQ MCP API workflows for HS code lookup, tariff and declaration details, regulatory requirements, and classification consultation requests with product image upload for expert review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[toucao](https://clawhub.ai/user/toucao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trade compliance users use this skill to query customs classification data and manage HSCIQ classification consultation forms. It supports guided HS code search, detail lookup, prior-case search, and expert-review submission workflows for Chinese products and related customs questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit product details and product images to HSCIQ for external processing and possible human review.

Mitigation: Require explicit user confirmation before create_guilei_form actions and avoid submitting confidential product photos, specifications, supplier details, brand/model data, or customs questions unless the user intends to share them with HSCIQ.

Risk: The skill can post discussion messages to classification consultation records.

Mitigation: Confirm the target consultation form, field, and message content with the user before any discussion-posting action.

## Reference(s):

- [HSCIQ MCP API Documentation](https://www.hsciq.com/MCP/Docs)
- [HSCIQ Service](https://www.hsciq.com)
- [ClawHub Skill Page](https://clawhub.ai/toucao/skills/hsciq-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and JSON/API response content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an HSCIQ API key and may return customs-code details, tariff data, declaration elements, consultation form status, and discussion messages from HSCIQ.]

## Skill Version(s):

3.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
