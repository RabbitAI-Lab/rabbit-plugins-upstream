## Description:

A self-learning quantitative analysis skill for A-share stocks that gathers market, technical, capital-flow, research, financial, and governance data, computes historical signal match rates and pattern summaries, and can generate structured DOCX reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunbinpy](https://clawhub.ai/user/sunbinpy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze Chinese A-share stocks, retrieve multi-source market and company data, compare historical signal outcomes, and produce concise analysis or DOCX reports. It is intended for statistical reference and report generation, not investment advice or guaranteed forecasting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports unsafe API-key handling, including local key creation and generated reports or logs that may contain a full API key.

Mitigation: Use a dedicated, rotatable key; review ~/.ghdata/ghdataapikey, logs, and generated reports before sharing; rotate the key after testing or if exposure is suspected.

Risk: The security scan reports undisclosed hardcoded database credentials that are not necessary for normal stock analysis.

Mitigation: Review and remove or disable bundled direct database credentials before deployment, and block database network access unless it is explicitly required.

Risk: The security guidance notes broad outbound network calls to public stock-data sources and a WebAPI endpoint.

Mitigation: Run the skill in a network-controlled environment, approve expected stock-data and WebAPI domains, and monitor outbound requests during evaluation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sunbinpy/skills/gh-data)
- [Publisher profile](https://clawhub.ai/user/sunbinpy)
- [股海罗盘 homepage](https://www.oraskl.com/ghdata-admin)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown stock-analysis summaries with Python snippets and optional DOCX report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local API-key state, charts, logs, and DOCX reports; results depend on outbound stock-data and WebAPI availability.]

## Skill Version(s):

2.2.49 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
