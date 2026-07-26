## Description: <br>
Searches Kalodata TikTok creator leaderboards and retrieves an individual creator's profile, commerce performance, contact, product, and shop details by creatorId. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External commerce analysts, sellers, and agents use this skill to discover TikTok Shop creators by market and time window, then inspect a selected creator's audience, sales, content, live, contact, product, and shop metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creator lookup queries and API credentials are sent to the configured service endpoint. <br>
Mitigation: Use approved credentials only, avoid sensitive queries, and restrict LINKFOX_TOOL_GATEWAY overrides to trusted endpoints. <br>
Risk: Creator responses may include contact fields and are saved as JSON files in the workspace session data directory and cache. <br>
Mitigation: Run the skill in a private workspace, protect or remove saved linkfox data before sharing a repository, and avoid shared workspaces for sensitive lookups. <br>
Risk: Feedback reporting may send user experience details outside the local environment when the skill supports it. <br>
Mitigation: Disable or constrain feedback reporting where user comments or operational context should remain internal. <br>
Risk: Repeated creator lookups and pagination consume paid credits. <br>
Mitigation: Use the built-in cache, avoid automatic parameter changes, and ask the user before performing additional paid lookups. <br>


## Reference(s): <br>
- [Kalodata TikTok Creator API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Release Page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-creator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries or tables plus JSON responses saved to files; scripts may print full JSON or a compact text summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY. Each API call consumes credits. Responses are cached for 24 hours by parameter set and saved under the current workspace's linkfox session data directory when writable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
