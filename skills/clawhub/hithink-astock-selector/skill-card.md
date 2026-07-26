## Description: <br>
Screens A-share stocks from natural-language queries using market, technical, financial, industry, and concept conditions, returning matching stock data from iWencai. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to translate A-share screening requests into iWencai queries, retrieve matching stock records, and present paginated results with the data source identified. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user stock-screening queries to the third-party iWencai service with an IWENCAI_API_KEY. <br>
Mitigation: Install only if the user trusts iWencai for these queries and provide the key through the IWENCAI_API_KEY environment variable. <br>
Risk: Passing the API key on the command line can expose it through shell history or process listings. <br>
Mitigation: Prefer environment-variable configuration and avoid including secrets directly in command invocations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chen6896qqwee/skills/hithink-astock-selector) <br>
- [iWencai web query interface](https://www.iwencai.com/unifiedwap/chat) <br>
- [iWencai SkillHub](https://www.iwencai.com/skillhub) <br>
- [iWencai OpenAPI query endpoint](https://openapi.iwencai.com/v1/query2data) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns paginated stock data, query metadata, trace IDs, and retry guidance when no matching data is found.] <br>

## Skill Version(s): <br>
1.0.0 (source: clawhub.json, release evidence, and skill documentation) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
