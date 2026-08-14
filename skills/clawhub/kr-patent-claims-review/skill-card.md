## Description:

Reviews Korean patent application claims from uploaded patent documents against Korean Patent Act and KIPO examination practice, then produces a structured report with claim-by-claim revision suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent professionals and IP teams use this skill to review Korean patent claim sets, identify legal compliance, support, wording, examination-practice, and invalidity risks, and draft actionable revisions. When PatSnap access is configured, it can incorporate global prior-art search results into the robustness assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent claim content or derived technical features may be sent to PatSnap MCP for prior-art search without a clear consent step.

Mitigation: Require explicit user approval before external search, and use a local-only review mode for unpublished or confidential patent applications when disclosure is not acceptable.

Risk: The invalidity and robustness assessment depends on PatSnap search access and may be incomplete when that service is not configured.

Mitigation: State when external search was not performed and limit conclusions to document-based review until authorized search results are available.

Risk: Patent prosecution recommendations can affect legal strategy if treated as final legal advice.

Mitigation: Have a qualified patent professional review the report before filing, amendment, response, or enforcement decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/kr-patent-claims-review)
- [ClawHub publisher profile](https://clawhub.ai/user/yuanzhian-patsnap)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, Guidance]

**Output Format:** [Structured Markdown report with tables and claim-by-claim revision examples; optional HTML report file when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains the user's input language and includes a claim structure table, six review dimensions, prioritized issues, and revision recommendations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
