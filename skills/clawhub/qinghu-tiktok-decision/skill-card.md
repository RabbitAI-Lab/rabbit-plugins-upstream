## Description:

This skill guides an agent through Qinghu-powered TikTok product research, combining product, video, influencer, seller, sourcing, and optional ERP listing signals into a concise product-selection report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and agents use this skill when they need a multi-source TikTok Shop product-selection decision. It helps compare product demand, content traction, influencer supply, competitor seller activity, sourcing options, and optional listing preparation after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request or use a Qinghu API token.

Mitigation: Use a token only for Qinghu-backed research, prefer configured environment variables when available, and avoid exposing the token in reports or exported files.

Risk: The workflow can call paid Qinghu data tools.

Mitigation: List the tools and ask for user confirmation before calls, then report actual Qinghu credit consumption from the response envelope when paid calls are made.

Risk: Qinghu tool responses can look successful at the HTTP or envelope layer while the inner business payload failed.

Mitigation: Check protocol errors, result.isError, and the parsed inner code and success fields before treating returned data as usable.

Risk: Sourcing and ERP listing steps can prepare downstream commerce actions.

Mitigation: Repeat the selected links and listing template to the user and proceed only after explicit confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-decision)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu login](https://www.iqinghu.com/workbench/login?urlCode=agentch)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow permissions check](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with structured sections, optional exported tables, JSON API request examples, and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large returned datasets are expected to be exported as files rather than pasted into chat.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
