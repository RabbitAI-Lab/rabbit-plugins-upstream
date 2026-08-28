## Description:

Quant-X v13 analyzes a Chinese A-share stock with Tencent and Eastmoney market data, combining OBI, OBV, longhubang validation, main-force accumulation checks, factor scoring, and trading guidance.

This skill is for research and development only.

## Publisher:

[43906351-debug](https://clawhub.ai/user/43906351-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research users can run this skill to fetch public Chinese equity market data for sh600330 and generate a structured quantitative analysis. The generated trading guidance should be treated as research output, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts Tencent and Eastmoney market-data endpoints during execution.

Mitigation: Run it only in an environment where those outbound requests are expected and permitted.

Risk: The script writes results to the fixed path /workspace/v13/analysis_result.json, which can create persistence or overwrite an existing file.

Mitigation: Review or change the output path before running in shared or persistent workspaces.

Risk: The skill produces trading guidance for a public stock.

Mitigation: Treat outputs as research only and require human financial review before any investment decision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/43906351-debug/skills/quant-x-v13)
- [Tencent quote data endpoint](https://qt.gtimg.cn)
- [Tencent minute data endpoint](https://web.ifzq.gtimg.cn)
- [Eastmoney push2 data endpoint](https://push2.eastmoney.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Shell commands]

**Output Format:** [Console text with Markdown-style headings and a JSON result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes analysis output to /workspace/v13/analysis_result.json when executed.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter states 13.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
