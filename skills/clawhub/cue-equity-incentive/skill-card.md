## Description:

Uses Cue to query and analyze listed-company equity incentive plans, including plan elements, implementation effects, peer comparisons, and competitiveness assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Public-company secretaries, HR and compensation leaders, investors, analysts, and consultants use this skill to request Cue reports on A-share listed-company equity incentive plans, peer benchmarks, and plan competitiveness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, research prompts, health checks, and authenticated Cue API calls are sent to cuecue.cn.

Mitigation: Avoid confidential company lists or internal-only research targets unless Cue's data handling terms fit the intended use.

Risk: Generated reports are saved locally and may contain compensation, investment, or peer-comparison analysis based on public data.

Mitigation: Review report sources and the local output path before sharing results or using them in decisions.

Risk: Cue service availability and external public data sources can affect run time, freshness, and completeness.

Mitigation: Run the documented health checks, wait for a completed '[cue-research] RESULT ok' response, and keep source links with the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-equity-incentive)
- [Cue service](https://cuecue.cn)
- [Cue sample equity incentive report](https://cuecue.cn/share/TIxQDFYs)
- [CNInfo](https://www.cninfo.com.cn)
- [Eastmoney data](https://data.eastmoney.com)
- [SEC EDGAR](https://www.sec.gov/edgar)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with shell command examples and local file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key; report content is generated through cuecue.cn and saved to the configured local output path.]

## Skill Version(s):

1.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
