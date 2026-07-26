## Description: <br>
用于快手达人数据、快手达人信息、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Kuaishou / Kwai creator profiles，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search Kuaishou creator accounts and retrieve profile facts such as identifiers, bio, verification, follower counts, following counts, received likes, IP location, and gender when available. It supports discovery by keyword before profile lookup when only a creator name, account keyword, or niche is known. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Kuaishou lookup terms, profile URLs, or user IDs are sent to SocialDataX under the user's API key. <br>
Mitigation: Confirm the user is comfortable with SocialDataX data handling before lookup and keep SOCIALDATAX_API_KEY scoped to the runtime environment. <br>
Risk: The direct CLI path runs the SocialDataX npm package with npx. <br>
Mitigation: Review the npm package and run the command in a controlled environment before production use. <br>


## Reference(s): <br>
- [SocialDataX API access page](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-creator-profile) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY plus node and npm when using the direct CLI.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
