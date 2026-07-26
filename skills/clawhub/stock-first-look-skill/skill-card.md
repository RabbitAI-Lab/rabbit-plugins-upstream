## Description: <br>
Helps users quickly form an initial view of an unfamiliar stock by summarizing the business, market focus, key metrics, valuation position, and major risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iwasnotalone](https://clawhub.ai/user/iwasnotalone) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and investors use this skill for first-pass stock screening, quick research preparation, and deciding whether a candidate stock is worth deeper follow-up. It is intended as screening research, not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A first-look stock report may be mistaken for investment advice or used without verifying current financial data. <br>
Mitigation: Treat the output as screening research, verify important financial data independently, and make investment decisions outside the skill output. <br>
Risk: The optional Wind MCP global install adds an external dependency to the agent environment. <br>
Mitigation: Approve the install only if the dependency is trusted and needed; otherwise use an already approved market data source. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iwasnotalone/skills/stock-first-look-skill) <br>
- [Wind skills Gitee mirror](https://gitee.com/wind_info/wind-skills.git) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with tables, bullet lists, and optional installation commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Final answer only; intermediate search paths and drafts are not shown.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
