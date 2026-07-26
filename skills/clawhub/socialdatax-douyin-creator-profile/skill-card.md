## Description: <br>
用于抖音达人数据、抖音达人信息、账号资料、创作者画像、主页信息和粉丝规模查询，覆盖 Douyin creator profiles through SocialDataX. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill to look up Douyin creator profile data from SocialDataX by sec_user_id or profile URL, then report available account basics, creator positioning, audience scale, and profile facts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SOCIALDATAX_API_KEY and sends lookup parameters to the SocialDataX service. <br>
Mitigation: Confirm trust in the SocialDataX npm package and service before installation, and configure the API key only in an environment where this data sharing is acceptable. <br>
Risk: API calls may consume SocialDataX account credits. <br>
Mitigation: Use specific lookup parameters, check account balance before repeated use, and avoid repeated retries for insufficient-balance errors. <br>
Risk: Returned profile data can be incomplete or unavailable for some Douyin creators. <br>
Mitigation: Report only fields present in the response and keep profile facts separate from any strategic interpretation. <br>


## Reference(s): <br>
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-profile) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or text with shell command examples; executed SocialDataX calls return JSON profile data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only lookup output; profile fields may include names, platform IDs, bio, verification, follower counts, following counts, received likes, IP location, and gender when available.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
