## Description: <br>
Retrieves Amazon seller policy and regulation updates with site and date filters, AI-generated Chinese summaries, original URLs, and full Markdown article details by record ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External cross-border sellers, ecommerce operators, and their agents use this skill to monitor Amazon official seller policy and regulation updates, scan Chinese summaries, and retrieve full article text for a selected feed record. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated requests send the LinkFox API key and session metadata to a gateway selected by LINKFOX_TOOL_GATEWAY. <br>
Mitigation: Install only if you trust LinkFox, and review or pin LINKFOX_TOOL_GATEWAY before use. <br>
Risk: The scripts persist full API responses and cache data under local linkfox directories. <br>
Mitigation: Use the skill in a controlled workspace, avoid shared environments for sensitive lookups, and clean generated linkfox data and cache directories when needed. <br>
Risk: Authentication or credit recovery may involve a separate onboarding skill download path. <br>
Mitigation: Accept that path only if you trust LinkFox and review the onboarding source before installation. <br>


## Reference(s): <br>
- [API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-policy-feed) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [JSON feed records for list results and Markdown article bodies for detail results, with full JSON responses saved to local files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may be summarized on stdout when payloads exceed 8 KB; scripts use a 24-hour local cache and support paginated list retrieval up to 100 items per page.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
