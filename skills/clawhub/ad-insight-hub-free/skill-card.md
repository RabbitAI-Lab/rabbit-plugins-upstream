## Description: <br>
Ad Insight Hub Free helps agents translate ad-intelligence requests into AdMapix API parameters, run basic creative search/count and app or developer profile queries, and return structured JSON results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, advertising operations teams, marketers, and developers use this skill to query AdMapix for competitor ad creatives, creative counts, application details, and developer profile data from natural-language requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends search parameters and query context to the AdMapix API. <br>
Mitigation: Use it only for data you are comfortable sending to api.admapix.com and review query contents before execution. <br>
Risk: The skill requires an AdMapix API key for authenticated requests. <br>
Mitigation: Store ADMAPIX_API_KEY in an environment variable or secret store, never paste it into chat, and avoid printing or logging the value. <br>
Risk: Generic file-handling and command-execution language in the artifact could be read too broadly. <br>
Mitigation: Limit execution to the documented AdMapix workflow and do not treat the skill as permission for unrelated local file access. <br>
Risk: The free skill has functional limits including no caching, no endpoint orchestration, no analysis or recommendations, and a page_size cap of 10. <br>
Mitigation: Use pagination and manual endpoint calls where needed, and do not rely on the skill for market analysis, revenue estimates, or recommendation reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ad-insight-hub-free) <br>
- [AdMapix website](https://www.admapix.com) <br>
- [AdMapix API endpoint](https://api.admapix.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash/curl commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses ADMAPIX_API_KEY as an environment variable and passes AdMapix API responses through as structured JSON.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
