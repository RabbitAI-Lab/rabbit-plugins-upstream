## Description: <br>
Operate Hypertxt articles and Google Search Console through the Hypertxt MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[julianengel](https://clawhub.ai/user/julianengel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content operators and developers use this skill to inspect Hypertxt projects, credits, articles, integrations, and GSC data, then prepare article plans, generate content, review editorial state, export content, or publish through connected destinations with explicit approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate account-impacting Hypertxt operations such as spending article credits, syncing GSC, changing editorial state, or publishing content. <br>
Mitigation: Require explicit approval immediately before each generation, sync, state change, or publishing action, and state the selected project, article, destination, mode, and credit impact before acting. <br>
Risk: Using the wrong project, article template, article, GSC connection, or publishing destination could affect unintended content or accounts. <br>
Mitigation: Discover identifiers with list tools, verify the selected project and destination with the user, and never guess IDs. <br>
Risk: The Hypertxt API key is sensitive account access material. <br>
Mitigation: Keep the API key in secret configuration as HYPERTXT_API_KEY and do not request, expose, or echo it in agent output. <br>


## Reference(s): <br>
- [Hypertxt OpenClaw Guide](https://www.hypertxt.ai/guides/openclaw/) <br>
- [ClawHub Skill Page](https://clawhub.ai/julianengel/skills/hypertxt) <br>
- [Publisher Profile](https://clawhub.ai/user/julianengel) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown, API calls, configuration] <br>
**Output Format:** [Markdown and structured agent instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured Hypertxt MCP server and HYPERTXT_API_KEY secret; account-impacting operations require explicit user approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
