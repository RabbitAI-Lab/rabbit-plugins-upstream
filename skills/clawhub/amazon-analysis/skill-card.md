## Description: <br>
Amazon-domain general analysis and multi-endpoint research engine for broad or composite Amazon market and product research requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run Amazon seller and product research workflows, including market analysis, product selection, competitor review, ASIN evaluation, pricing reference, and composite opportunity reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad or composite analyses can consume ZooData API credits. <br>
Mitigation: Confirm the scope and estimated credit cost before running multi-call scans. <br>
Risk: The skill requires a ZooData API key for live API calls. <br>
Mitigation: Install and use it only when comfortable providing the required key, and stop rather than fabricating results when the key is missing, invalid, or out of credits. <br>
Risk: Amazon seller research outputs may be incomplete, sampled, delayed, or partly inferred. <br>
Mitigation: Treat reports as decision support, require data provenance and confidence labels, and validate important business decisions with additional sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/apiclaw) <br>
- [Metadata homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>
- [ZooData API endpoint](https://api.zoodata.ai/openapi/v2) <br>
- [Execution guide](references/execution-guide.md) <br>
- [API field reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown reports with tables, confidence labels, data provenance, API usage, and occasional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should match the user's language and disclose estimated API credit use, sampling limits, missing data, and fallback methods.] <br>

## Skill Version(s): <br>
1.1.10 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
