## Description:

Generates an automotive NVH acoustic sealing and structural reinforcement competitive intelligence HTML report from company, competitor, product, industry, report-period, and patent-search inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Business, patent, and strategy teams use this skill to create a structured competitive intelligence report for automotive acoustic sealing and structural reinforcement products. It is intended to package user-provided company, competitor, and patent-search inputs into an offline HTML brief with KPI, SWOT, patent landscape, threat, and recommendation sections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may present a static report template as data-driven competitive intelligence.

Mitigation: Review generated reports before relying on them, and treat competitive, patent, infringement-risk, and market recommendations as static unless the agent separately performs and cites fresh PatSnap or Zhihuiya searches.

Risk: Generated reports may influence business or patent strategy without enough source validation.

Mitigation: Require human review and cross-check patent, market, and competitor claims against current authoritative sources before using the report for decisions.

Risk: The report generation script writes to a configurable output path.

Mitigation: Run the script with output restricted to a dedicated reports directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/competitive-intel-report)
- [Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [V12 HTML report template](references/template_v12.html)
- [V11 HTML report template](references/template_v11.html)
- [V8 HTML report template](references/template_v8.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [HTML report file with supporting text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated HTML is designed as a single offline report and can be downloaded or printed to PDF.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
