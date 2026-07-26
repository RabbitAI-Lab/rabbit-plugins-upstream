## Description: <br>
Generate, schedule, and publish posts across 15 platforms in the user's voice, while managing post queues, preferences, billing, quota, media, replies, ideas, and content plans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmoon90](https://clawhub.ai/user/jmoon90) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, marketers, and social media operators use this skill to draft, schedule, publish, review, and manage social posts across connected XreplyAI accounts. It also helps agents inspect account, quota, style, schedule, media, rule, idea, and plan context before taking posting actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing without a schedule can immediately post to connected social accounts. <br>
Mitigation: Require explicit user approval before any xreply_posts_publish call that omits scheduled_at. <br>
Risk: Delete actions can remove posts or writing rules from the connected XreplyAI account. <br>
Mitigation: Confirm the target ID and intended deletion before calling post or rule delete tools. <br>
Risk: Media upload tools can read local image or video files and send them to the service. <br>
Mitigation: Confirm the local file path and user intent before uploading media. <br>
Risk: Context tools may expose connected account details, billing, quota, schedules, and preferences. <br>
Mitigation: Limit requests to the information needed for the task and avoid sharing returned account or billing details unnecessarily. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jmoon90/skills/xreplyai) <br>
- [Publisher Profile](https://clawhub.ai/user/jmoon90) <br>
- [XreplyAI Homepage](https://xreplyai.com) <br>
- [mcporter npm Package](https://www.npmjs.com/package/mcporter) <br>
- [XreplyAI MCP npm Package](https://www.npmjs.com/package/@xreplyai/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and API result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XREPLY_TOKEN and mcporter or npx to call the XreplyAI MCP server.] <br>

## Skill Version(s): <br>
0.3.23 (source: server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
