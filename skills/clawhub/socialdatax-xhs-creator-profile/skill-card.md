## Description: <br>
用于小红书博主数据、小红书博主信息、账号资料、达人画像、主页信息和粉丝规模查询，覆盖 Xiaohongshu / XHS / RedNote creator profiles，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to look up Xiaohongshu / XHS / RedNote creator profile facts through SocialDataX, including account basics, creator positioning, audience scale, and profile metadata. It is intended for read-only profile information retrieval using the user's SocialDataX API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends lookup requests through the SocialDataX npm package using the user's SOCIALDATAX_API_KEY. <br>
Mitigation: Install only if you trust the SocialDataX package and provide only an API key intended for these read-only lookups. <br>
Risk: API errors, malformed profile links, or insufficient account balance can prevent profile data retrieval. <br>
Mitigation: Check the API key, request parameters, and returned error message; avoid repeated retries on insufficient-balance errors and use the recharge URL returned by the service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-creator-profile) <br>
- [SocialDataX API access page](https://socialdatax.com/ai?from=clawhub) <br>
- [Publisher profile](https://clawhub.ai/user/devinchen2014) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and node/npm; reports available creator profile fields while separating profile facts from strategic interpretation.] <br>

## Skill Version(s): <br>
0.1.14 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
