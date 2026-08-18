## Description:

Generates traceable patent Freedom to Operate reports from a risk-point Word document and user-provided PatSnap search queries, using PatSnap patent search, claim retrieval, and AI-assisted infringement comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent risk analysts and IP teams use this skill to convert product or technology risk-point documents and explicit PatSnap search strings into analyst-ready FTO reports. It preserves search inputs, patent retrieval records, claim 1 sources, AI07 comparison records, and report traceability for later review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product technical descriptions, search strategy, patent claim excerpts, and generated analysis may be sent to Zhihuiya/PatSnap services.

Mitigation: Use only when those data flows are acceptable, minimize sensitive input, and keep generated JSON/report files in access-controlled storage or delete them when no longer needed.

Risk: The security evidence flags inconsistent MCP-versus-internal-script setup that could confuse deployment or data-flow expectations.

Mitigation: Resolve the setup before use, confirm the intended PatSnap connection path, and store the required API key securely outside public releases.

Risk: Automated FTO conclusions can be incomplete when claim 1, legal status, or AI-assisted comparison output is missing.

Mitigation: Require analyst or patent-counsel review before business decisions, and treat missing claim or AI output as blocked or pending rather than low risk.

## Reference(s):

- [Skill page](https://clawhub.ai/yuanzhian-patsnap/skills/generic-fto-report)
- [API call policy](artifact/references/api_call_policy.md)
- [PatSnap OpenAPI reference](artifact/references/api_reference.md)
- [Claim chart schema](artifact/references/claim_chart_schema.md)
- [Report requirements](artifact/references/report_requirements.md)
- [PatSnap Open Platform authentication](https://open.zhihuiya.com/devportal/guides/authentication)
- [PatSnap MCP services marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash commands; generated JSON, HTML, and DOCX report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes traceability artifacts such as queries.json, patent_list.json, and fto_structured_data.json alongside the generated FTO report.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
