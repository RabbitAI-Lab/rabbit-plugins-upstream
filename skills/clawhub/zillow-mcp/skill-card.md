## Description: <br>
Look up real-estate listings, property details, Zestimates, saved searches/homes, and market reports on Zillow via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query Zillow property listings, property details, Zestimates, market reports, and their own saved Zillow homes or searches through an MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved homes and saved searches can use the user's signed-in Zillow browser session and may reflect account-linked activity. <br>
Mitigation: Use explicit prompts for saved-home or saved-search requests, and avoid broad Zillow requests when account-linked activity should not be considered. <br>
Risk: Zillow access may fail or return incomplete results because the service can present captcha challenges or change private web endpoints. <br>
Mitigation: Treat returned property and market data as assistive, and verify important real-estate decisions in Zillow or other authoritative sources. <br>


## Reference(s): <br>
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Zillow data access; saved-home and saved-search results can depend on the user's signed-in Zillow browser session.] <br>

## Skill Version(s): <br>
0.10.6 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
