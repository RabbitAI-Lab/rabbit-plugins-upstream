## Description:

青虎AI B 站社媒运营 helps agents use Bilibili hot-search, video, comment, and creator data to produce long-form video script analysis, audience sentiment findings, and UP creator placement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External social media and brand marketing teams use this skill to analyze Bilibili topics, long-form video structure, comment sentiment, and creator fit for Bilibili seeding campaigns. It guides agents toward concise strategy deliverables and exported data files when result sets are large.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to Qinghu's Bilibili data API and may use Qinghu API credentials.

Mitigation: Use a dedicated Qinghu API key through QINGHU_TOKEN or QHKIT_TOKEN, and only provide the key in an environment intended for this skill.

Risk: API calls can consume Qinghu credits and larger result sets may be exported to local files.

Mitigation: Confirm intended API use before calls, review credit usage in returned results, and inspect exported files before sharing them outside the workspace.

Risk: Bilibili advertising and creator-placement recommendations can be misleading if sample size, time period, or disclosure obligations are unclear.

Mitigation: Label site, time period, and sample size in conclusions, and remind users that commercial Bilibili content may require platform-compliant disclosure or filing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-bilibili-social)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu login](https://www.iqinghu.com/workbench/login?urlCode=agentch)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Guidance]

**Output Format:** [Markdown responses with optional exported spreadsheet or table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large result sets should be exported to local files with concise links, short previews, and clear data scope.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
