## Description: <br>
Look up real-estate listings, property details, price/tax history, market reports, saved homes, and photo galleries on homes.com via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and real-estate-focused agent users use this skill to query homes.com listings, resolve property addresses, inspect property records, compare homes, retrieve histories and photos, and run local mortgage or affordability calculations through an MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose account-specific saved homes and saved searches from an authenticated homes.com tab to the agent session. <br>
Mitigation: Only invoke saved-home or saved-search tools when that information is intended to be shared in the session. <br>
Risk: The MCP flow depends on a browser extension and an active homes.com browser session. <br>
Mitigation: Install fetchproxy deliberately, keep the homes.com tab under the user's control, and review extension and session state before use. <br>
Risk: Listing and market data is read from homes.com pages rather than a public consumer API. <br>
Mitigation: Verify important real-estate decisions against authoritative property, lender, tax, or listing sources before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes) <br>
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp) <br>
- [fetchproxy installation repository](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance] <br>
**Output Format:** [Markdown with JSON configuration snippets and inline tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return read-only homes.com listing data, property records, history, market summaries, saved account data when requested, and local calculator results.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
