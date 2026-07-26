## Description: <br>
Find Telegram groups/channels by topic using web search and fetch. Use when you need to locate Telegram communities for specific subjects (e.g., payment channels, niche interests). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiiang0529](https://clawhub.ai/user/xiiang0529) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, marketers, and community operators use this skill to find public Telegram groups or channels related to a topic, extract Telegram handles or t.me links, and return a deduplicated list with brief descriptions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search results can include misleading, unsafe, illegal, or impersonated Telegram communities, especially for payment-related topics. <br>
Mitigation: Verify the legality, safety, and authenticity of discovered groups before joining, contacting members, or acting on their content. <br>
Risk: The skill returns public group and channel links discovered through web search, which may be stale, duplicated, or context-poor. <br>
Mitigation: Review fetched page context, deduplicate handles, and present uncertainty when a link or description cannot be confirmed. <br>


## Reference(s): <br>
- [Reference Documentation for Telegram Group Finder](references/api_reference.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/xiiang0529/skills/telegram-group-finder) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown numbered list of deduplicated Telegram group or channel links with brief descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include public Telegram usernames or t.me links; no credentials or persistent state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
