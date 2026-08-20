## Description:

青虎AI TikTok 达人带货建联 helps agents find and evaluate TikTok Shop influencers by category, region, competitor product, and seller relationship so users can prioritize higher-ROI outreach and avoid blind sampling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External TikTok Shop operators and ecommerce teams use this skill to identify, compare, and prioritize creators for product seeding or outreach. It supports both forward discovery from influencer lists and reverse discovery from competitor products or stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Qinghu API credentials may be present in environment variables or entered by users during operation.

Mitigation: Use a dedicated low-privilege Qinghu API key, restrict environment access, and rotate the key if it may have been exposed.

Risk: Influencer and competitor research results may be written automatically to local spreadsheet or cache files.

Mitigation: Install only in workspaces where local exports are acceptable, restrict file sharing, and remove exported or cached files when they are no longer needed.

Risk: Paid Qinghu tool calls may consume account credits if authorization prompts are not monitored.

Mitigation: Review paid-tool authorization prompts, keep per-session call counts bounded, and verify reported point costs after calls complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-influencer)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with ranked influencer lists, optional spreadsheet exports, and HTTP/JSON request examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local spreadsheet or cache files for result sets of 10 or more records; requires Qinghu API credentials for live data.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
