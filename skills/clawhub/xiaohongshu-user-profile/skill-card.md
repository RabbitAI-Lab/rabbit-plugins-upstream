## Description: <br>
Fetch Xiaohongshu (RedNote / xhs) user profile information and their published notes list by user ID, returning nickname, bio, follower/following counts, engagement totals, tags, and paginated notes with engagement stats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to collect Xiaohongshu creator profile details and visible published-note engagement data for user-directed profile, influencer, or blogger analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Xiaohongshu login in an agent-controlled browser. <br>
Mitigation: Use only for user-directed lookups where the user is comfortable authenticating and where access to the viewed profile data is authorized. <br>
Risk: The skill includes guidance for scaled scraping with multiple stealth browser sessions. <br>
Mitigation: Avoid batch and stealth multi-session use unless there is clear authorization, platform rules are understood, and the user explicitly approves the approach. <br>
Risk: The skill may write operational notes to a local memory file when unexpected execution issues occur. <br>
Mitigation: Check, disable, or delete the local memory file behavior if persistent operational notes in the working directory are not acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/xiaohongshu-user-profile) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, guidance] <br>
**Output Format:** [JSON objects returned through browser automation steps, with supporting shell commands and operational guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Profile output includes user ID, nickname, bio, gender, IP location, avatar URL, follow counts, fan count, interaction count, and tags. Notes output includes title, type, engagement counts, cover URL, total count, and pagination state.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
