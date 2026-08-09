## Description: <br>
Analyzes Amazon ads search term reports to identify zero-order spend, test common keyword-management assumptions within the account, and guide budget structure by search intent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mikeli20221102-ux](https://clawhub.ai/user/mikeli20221102-ux) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers and advertising operators use this skill to prepare Amazon search term reports for Lingxiao's MCP tools and interpret account-internal waste and keyword-myth checks. It is intended for ad diagnostics and human-reviewed optimization decisions, not automatic bulk changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided Amazon ads search term reports are sent to the external lingxiaochuhai.com MCP service. <br>
Mitigation: Upload only reports the user is allowed to share, and remove sensitive or unauthorized data before using the MCP tools. <br>
Risk: Keyword recommendations can be misleading if search terms are treated without campaign, ad group, and match-type context. <br>
Mitigation: Keep negative-keyword decisions under human review and apply them row by row with campaign and ad group context. <br>
Risk: Recent attribution delays and missing cost data can lead to premature or unsupported conclusions. <br>
Mitigation: Avoid negative-keyword decisions based on the most recent 7 days and do not infer profitability without cost inputs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mikeli20221102-ux/skills/lingxiao-amazon-ads-check) <br>
- [Lingxiao MCP Endpoint](https://www.lingxiaochuhai.com/mcp) <br>
- [Ads Waste Check Web Tool](https://www.lingxiaochuhai.com/tools/ads-waste-check) <br>
- [Ads Myth Check Web Tool](https://www.lingxiaochuhai.com/tools/ads-myth-check) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON MCP configuration and tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided Amazon ads search term report content; free-tier analyses avoid store authorization and cost-based profit claims.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
