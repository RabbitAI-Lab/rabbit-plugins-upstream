## Description: <br>
每日英语诗歌推送。每天从多个英文诗歌网站抓取当日推荐诗歌（Poem of the Day），包含诗歌全文、作者介绍和深度赏析，推送至飞书。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cantoneyes](https://clawhub.ai/user/cantoneyes) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and personal productivity users can use this skill to fetch a daily English poem, enrich it with poet background and literary appreciation, and publish the formatted result to Feishu. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated poem messages may include private prompts or sensitive business data if used in the wrong chat context. <br>
Mitigation: Use the skill only in a dedicated daily poem workflow and avoid invoking it in conversations that contain private or sensitive information. <br>
Risk: The skill posts content to Feishu and depends on user-configured destination and credentials. <br>
Mitigation: Configure the Feishu destination and credentials manually, and review the target channel before enabling the scheduled workflow. <br>
Risk: External poem sources can be unavailable or return incomplete content. <br>
Mitigation: Use the documented source fallback order and send a Feishu failure notice when all sources fail. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cantoneyes/skills/daily-english-poem) <br>
- [Poem Analysis - Poem of the Day](https://poemanalysis.com/poem-of-the-day/) <br>
- [Poets.org - Poem-a-Day](https://poets.org/poem-a-day) <br>
- [Poetry Daily](https://poems.com/) <br>
- [Discover Poetry - Poem of the Day](https://discoverpoetry.com/poems/poem-of-the-day/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Formatted Feishu message content with poem text, poet background, and reading appreciation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves the original poem text format and avoids Markdown tables for Feishu compatibility.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
