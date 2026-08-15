## Description:

Generic Drug Scout V1 runs a focused China small-molecule polymorph patent-expiry screen through configured PatSnap/Zhihuiya MCP services and generates a local interactive HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts and developers use this skill to screen early generic-drug opportunities by focusing on China small-molecule crystal-form patent expiry windows. It packages first-screening results, exclusions, data notes, and sources into a standalone local HTML report for review.

### Deployment Geography for Use:

Global use, with screening scope limited to China/CN patent and drug evidence.

## Known Risks and Mitigations:

Risk: The skill reads the user's Codex MCP configuration and calls configured PatSnap/Zhihuiya MCP endpoints.

Mitigation: Review the skill before installation and use it only in environments where those configured MCP services are intended to be available to the agent.

Risk: Workflows can overwrite target output directories when --overwrite is used.

Mitigation: Run report generation in a dedicated workspace or output folder and avoid using --overwrite on important directories.

Risk: Generated reports depend on external MCP data availability and configuration.

Mitigation: Complete the documented MCP self-check before use and treat MCP failures as errors rather than substituting sample data for real screening.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/generic-drug-scout)
- [V1 scope reference](references/v1-scope.md)
- [Sample report data](references/sample-report-data.json)
- [Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [Zhihuiya MCP server marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [Zhihuiya authentication guide](https://open.zhihuiya.com/devportal/guides/authentication)
- [PatSnap developer documentation](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with inline shell commands plus generated local HTML and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces standalone interactive HTML reports with copied image assets; optional workflows generate a seeded local platform directory and first_screening_result.json audit data.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
