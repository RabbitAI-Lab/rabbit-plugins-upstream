## Description:

HuaHuaDailyMCP lets agents query and analyze HuahuaDaily fund holdings, market, transaction, quantitative, and community data, and create trade or batch-import requests that users must confirm in the app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baiye1997](https://clawhub.ai/user/baiye1997)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to HuahuaDaily for portfolio review, fund and market lookup, transaction or import request preparation, and bounded quantitative analysis while keeping final trade or import confirmation in the app.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive investment data such as holdings, costs, amounts, transaction history, and returns.

Mitigation: Install only when the user trusts HuahuaDaily and publisher baiye1997, prefer the official remote MCP or a pinned release or commit, use the core profile when possible, and revoke or rotate the Agent Token when access is no longer needed.

Risk: The skill can create pending trade or import requests and can perform some user-authorized account actions that are not final trades.

Mitigation: Require explicit user intent before state-changing actions, make clear when app confirmation is still required, and treat community authorization, following, report submission, snapshots, and backtests as real account actions.

Risk: Changing service endpoints or handling local files incorrectly could expose data to unintended systems or include unnecessary sensitive content in the conversation.

Mitigation: Keep HUAHUA_API_BASE on the official service unless operating the backend, use only user-provided file paths for CLI workflows, and avoid pasting large exports or image Base64 into agent context.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/baiye1997/skills/huahua-daily)
- [CLI File and Export Workflows](references/cli-artifacts.md)
- [Community and Reports Guidance](references/community-reports.md)
- [Date Safety Guidance](references/date-safety.md)
- [Fund and Market Guidance](references/fund-market.md)
- [Portfolio Guidance](references/portfolio.md)
- [Quantitative Analysis Guidance](references/quant.md)
- [Trade and Import Guidance](references/trade-import.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with tool-call guidance, JSON snippets, configuration examples, and shell commands for local CLI workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON result or export files through the huahua CLI; transaction and import requests still require user confirmation in the HuahuaDaily app.]

## Skill Version(s):

4.1.7 (source: frontmatter, release evidence, pyproject dynamic version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
