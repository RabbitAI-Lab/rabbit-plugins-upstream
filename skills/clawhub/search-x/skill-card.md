## Description: <br>
Real-time X/Twitter search powered by Grok-4 that helps agents find tweets, trends, and discussions with citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mvanhorn](https://clawhub.ai/user/mvanhorn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to search X/Twitter for recent posts, trends, account-specific discussions, and links that can be cited in downstream work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms, handle filters, and date filters are sent to xAI using the configured API key. <br>
Mitigation: Avoid entering secrets, confidential project names, personal data, or sensitive investigative terms unless sharing them with xAI is acceptable. <br>
Risk: The skill can search X/Twitter when invoked, so ambiguous prompts may expose unintended topics to the external API. <br>
Mitigation: Invoke the skill explicitly only when X/Twitter search is intended and review search terms before execution. <br>


## Reference(s): <br>
- [Search X on ClawHub](https://clawhub.ai/mvanhorn/skills/search-x) <br>
- [xAI Documentation](https://docs.x.ai) <br>
- [xAI Console](https://console.x.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Plain text or Markdown search summaries with X/Twitter citations, optional links-only output, or full JSON responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XAI_API_KEY; supports date ranges, allowed handles, excluded handles, compact output, links-only output, JSON output, and model override.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
