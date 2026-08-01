## Description: <br>
Query the On the Cheap network from the shell with curl and jq for daily local event listings with times, prices, and venues, plus searchable articles on free and cheap things to do when the onthecheap MCP server is unavailable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve local events, deals, and related article data from public On the Cheap WordPress sites using shell commands. It is most useful as a fallback when the onthecheap MCP server is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill proposes shell commands that make live web requests and parse public HTML or JSON from On the Cheap sites. <br>
Mitigation: Review commands before running them, keep requests to public site URLs, and avoid adding sensitive data to command lines. <br>
Risk: Incorrect event or deal results can occur if expired posts are not filtered, site-specific IDs are reused, date paths use ISO format, HTML entities are left encoded, or month grids are treated as complete schedules. <br>
Mitigation: Resolve IDs per site, exclude the expired category, confirm the rendered day heading, decode entities before presenting titles, and fetch day pages for complete event listings. <br>


## Reference(s): <br>
- [Ready-to-run recipes](references/recipes.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/otc-curl) <br>
- [Charlotte On the Cheap](https://www.charlotteonthecheap.com) <br>
- [Mile High on the Cheap](https://www.milehighonthecheap.com) <br>
- [Triangle on the Cheap](https://triangleonthecheap.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Code, Configuration] <br>
**Output Format:** [Markdown with inline bash, jq, and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-only command recipes and parsing guidance for public web content; no API key or login is required.] <br>

## Skill Version(s): <br>
0.3.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
