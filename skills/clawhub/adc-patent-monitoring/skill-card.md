## Description:

监控ADC新申请、专利族、法律状态和竞争风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent intelligence teams and ADC portfolio owners use this skill in Eureka Desktop to generate weekly or monthly ADC patent monitoring reports covering new WO applications, patent family expansion, legal status, applicant activity, and competitive risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports can be incomplete or fail to generate if the required PatSnap/Eureka MCP access is missing, credentials are invalid, or the required weekly patent-query workflow is not followed.

Mitigation: Confirm the intended PatSnap/Eureka access before installation and review report outputs against the structured patent evidence used for generation.

Risk: Generated HTML reports load Chart.js from a public CDN unless the template is changed.

Mitigation: Use an approved network path for the CDN or replace the template reference with a locally hosted Chart.js copy before use in restricted environments.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/yuanzhian-patsnap/skills/adc-patent-monitoring)
- [ADC report HTML template](artifact/references/adc_report_template_v4.1.html)
- [Chart.js CDN used by generated reports](https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown-style agent guidance plus generated HTML patent report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports depend on structured PatSnap/Eureka patent data and the bundled HTML template.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
