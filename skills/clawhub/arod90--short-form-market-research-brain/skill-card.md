## Description: <br>
Short-form video market research via the Virlo API — viral niche research, trend tracking, creator vetting, hashtag and sound intelligence across TikTok, YouTube Shorts, and Instagram Reels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arod90](https://clawhub.ai/user/arod90) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketers, creators, and developers use this skill to research short-form video niches, identify trends and creators, monitor recurring topics, and analyze social video performance through Virlo API data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate Virlo API requests that spend prepaid credits. <br>
Mitigation: Confirm the target, estimated cost, and current balance before paid lookups or tracking setup. <br>
Risk: Recurring monitors can continue running and spending credits over time. <br>
Mitigation: Confirm cadence before creating recurring monitors and review active monitors periodically. <br>
Risk: Research queries, social URLs, handles, and monitoring targets are sent to Virlo under the user's API key. <br>
Mitigation: Install and use the skill only when sending that information to Virlo is acceptable for the user's workflow. <br>
Risk: Autopilot, PATCH, PUT, and DELETE actions can change or remove monitored resources. <br>
Mitigation: Confirm the exact target and intended change before applying configuration changes or deletions. <br>


## Reference(s): <br>
- [Virlo API Documentation](https://dev.virlo.ai/docs) <br>
- [Virlo Full API Reference for Agents](https://dev.virlo.ai/llms-full.txt) <br>
- [Virlo Pricing](https://dev.virlo.ai/pricing) <br>
- [ClawHub Skill Page](https://clawhub.ai/arod90/skills/short-form-market-research-brain) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API call plans, research summaries, monitoring setup guidance, and cost or balance warnings.] <br>

## Skill Version(s): <br>
1.9.2 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
