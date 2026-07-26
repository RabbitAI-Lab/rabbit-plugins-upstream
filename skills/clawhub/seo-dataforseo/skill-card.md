## Description: <br>
SEO keyword research using the DataForSEO API for keyword analysis, YouTube keyword research, competitor analysis, SERP analysis, and trend tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adamkristopher](https://clawhub.ai/user/adamkristopher) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, SEO practitioners, and content strategists use this skill to call DataForSEO APIs for keyword metrics, SERP rankings, competitor research, trends, and saved research summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SEO queries, domains, location choices, and related research inputs are sent to DataForSEO. <br>
Mitigation: Use only approved research inputs and avoid sending client-sensitive, private, or strategy-sensitive data unless permitted. <br>
Risk: DataForSEO credentials are loaded from a .env file. <br>
Mitigation: Keep .env credentials out of version control and restrict local access to the workspace. <br>
Risk: Saved results may contain client, competitor, or strategy-sensitive research data. <br>
Mitigation: Delete or restrict access to results/ files when they contain sensitive research outputs. <br>
Risk: Broad analyses can consume DataForSEO API quota or create billing impact. <br>
Mitigation: Confirm account limits before large runs and use available limits or skip flags to scope requests. <br>


## Reference(s): <br>
- [API Reference](references/api-reference.md) <br>
- [DataForSEO API Access](https://app.dataforseo.com/api-access) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON files, Markdown, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Python function calls, saved JSON result files, and Markdown summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DataForSEO credentials; results are saved locally under results/ by category.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
