## Description: <br>
Convertible Bond Research helps agents conduct Chinese convertible bond and issuer research, including screening, single-bond analysis, clause-event assessment, equity and industry research, valuation, and investment-summary reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jackluson](https://clawhub.ai/user/jackluson) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Financial analysts, investors, and research agents use this skill to research convertible bonds, evaluate clause-event probabilities such as downward conversion-price revision or forced redemption, and connect bond signals to issuer fundamentals, industry cycles, valuation, and research summaries. Outputs are research references and should not be treated as investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an external Anchor Data MCP integration that requires a user-provided bearer token. <br>
Mitigation: Install only if the user trusts the Anchor Data MCP service, use a least-privilege token where available, avoid sharing configs that contain the bearer token, and rotate or revoke the token if exposure is suspected. <br>
Risk: Prompts, tool requests, and results may be handled by the external MCP service. <br>
Mitigation: Avoid sending sensitive or confidential research context unless the user is comfortable with that service handling it. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/jackluson/convertible-bond-research) <br>
- [ClawHub skill page](https://clawhub.ai/jackluson/skills/convertible-bond-research) <br>
- [Anchor Data](https://www.anchor-data.cn) <br>
- [Anchor Data MCP introduction](https://www.anchor-data.cn/blog/anchor-mcp-intro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and HTML-style research reports with tables, charts, configuration snippets, tool-call guidance, and risk notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require external MCP data from anchor-bond and supplemental web or market-data research; large bond_detail results may be handled as files.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
