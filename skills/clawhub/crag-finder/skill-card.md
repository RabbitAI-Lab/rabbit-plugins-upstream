## Description: <br>
Helps agents search theCrag.com for outdoor climbing and bouldering areas, then summarize crag names, route counts, grades, climbing types, access notes, GPS details, and useful links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lixin0217](https://clawhub.ai/user/lixin0217) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Climbers, trip planners, and climbing-focused agents use this skill to find outdoor climbing destinations by country, region, city, or crag name and present Chinese-first summaries with relevant theCrag.com links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: theCrag.com data is community maintained and may be incomplete, outdated, or missing current route, access, seasonal, or safety details. <br>
Mitigation: Verify climbing conditions, access rules, seasonal closures, and safety information against current local sources before relying on the results outdoors. <br>
Risk: theCrag.com pages may block automated fetching, which can leave the agent with search snippets or constructed links rather than full page details. <br>
Mitigation: Treat fallback summaries as preliminary and open the provided theCrag.com links directly for the most complete available information. <br>


## Reference(s): <br>
- [theCrag.com URL patterns](references/url_patterns.md) <br>
- [theCrag API documentation](https://www.thecrag.com/en/article/api) <br>
- [ClawHub skill page](https://clawhub.ai/lixin0217/skills/crag-finder) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown summaries with direct links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-first responses; falls back to search-result summaries and direct URLs when theCrag.com pages cannot be fetched.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
