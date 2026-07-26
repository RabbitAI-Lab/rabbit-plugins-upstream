## Description: <br>
Twitter Search fetches tweets by keyword or advanced Twitter/X queries, processes up to 1000 results, and supports social media analysis reports with metrics, insights, and recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyfoxci](https://clawhub.ai/user/flyfoxci) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, analysts, marketers, and developers use this skill to run Twitter/X searches, collect tweet metrics, and produce data-driven social listening, trend, influencer, sentiment, and topic reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The wrapper reads and evaluates shell profile content while looking for TWITTER_API_KEY. <br>
Mitigation: Avoid the wrapper as written; pass TWITTER_API_KEY through the process environment or call the Python script directly after removing eval-based profile parsing. <br>
Risk: The wrapper may install a Python dependency during normal use. <br>
Mitigation: Install and pin dependencies in a controlled environment before use instead of allowing runtime package installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/flyfoxci/skills/twitter-search-skill) <br>
- [Twitter API reference](references/twitter_api.md) <br>
- [TwitterAPI.io advanced search endpoint](https://docs.twitterapi.io/api-reference/endpoint/tweet_advanced_search) <br>
- [Twitter advanced search syntax reference](https://github.com/igorbrigadir/twitter-advanced-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [JSON tweet data from the search script and Markdown analysis reports with tables, metrics, recommendations, and tweet links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TWITTER_API_KEY and supports query, max-results, query-type, and format options.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
