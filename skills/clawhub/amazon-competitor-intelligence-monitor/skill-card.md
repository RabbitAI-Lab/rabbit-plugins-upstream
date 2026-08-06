## Description: <br>
Amazon Competitor Intelligence Monitor helps agents run focused ZooData-powered competitor scans or monitoring checks for Amazon keywords, ASINs, brands, and defined competitor sets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketplace operators, and agent users use this skill to analyze known Amazon competitors, compare market position, identify pricing and review patterns, and monitor tracked ASINs for changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The runtime can resolve credentials from legacy APICLAW_API_KEY or ~/.apiclaw/config.json sources. <br>
Mitigation: Run the skill with a dedicated ZOODATA_API_KEY and do not expose unrelated legacy API keys or ~/.apiclaw/config.json to the agent environment. <br>
Risk: Monitoring state and review fallback work files can leave competitor targets or review data in local directories. <br>
Mitigation: Periodically clean monitor-data and /tmp review work directories, especially in shared or long-lived agent runtimes. <br>
Risk: Broad competitor scans can consume account credits quickly. <br>
Mitigation: Confirm estimated credit cost before multi-call scans and prefer granular commands when operating under a credit cap. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-competitor-intelligence-monitor) <br>
- [Project homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>
- [ZooData pricing](https://zoodata.ai/en/pricing) <br>
- [ZooData API field reference](artifact/references/reference.md) <br>
- [ZooData CLI contract](artifact/references/cli-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with tables, status messages, and optional shell commands; the bundled CLI produces JSON evidence for the agent to summarize.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports should match the user's language, include confidence labels, data provenance, API usage, and credit consumption when API calls run.] <br>

## Skill Version(s): <br>
1.1.8 (source: skill metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
