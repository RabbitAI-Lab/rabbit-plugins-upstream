## Description: <br>
Ad Insight Hub Free helps agents translate advertising-intelligence requests into AdMapix API parameters, query creative search/count and app or developer profile endpoints, and return the resulting structured data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External advertising, growth, and app-market teams use this skill to query AdMapix for competitor ad creatives, creative counts, app details, and developer details from natural-language requests. It is best suited for basic API lookup and parameter translation workflows rather than analysis, recommendations, endpoint orchestration, caching, or paid-edition data products. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AdMapix API key exposure. <br>
Mitigation: Configure the key only through ADMAPIX_API_KEY or a secure secret store, and do not paste, print, or store the key in chat. <br>
Risk: Outbound requests send query parameters to AdMapix and return API data directly. <br>
Mitigation: Review request inputs before execution, run only against the intended AdMapix account, and treat returned data according to the account's data-handling requirements. <br>
Risk: The artifact includes file-processing claims that the server evidence flags as unrelated boilerplate. <br>
Mitigation: Scope use to the documented AdMapix API query behavior unless the publisher provides narrower documentation for file handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ad-insight-hub-free) <br>
- [AdMapix website](https://www.admapix.com) <br>
- [AdMapix API base URL](https://api.admapix.com) <br>
- [AdMapix creative search endpoint](https://api.admapix.com/api/data/search) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns AdMapix API data directly; page_size is documented with a maximum of 10 and no result caching.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
