## Description: <br>
用于抖音文案提取、抖音文案一键提取、抖音视频文案提取、抖音视频转文字、抖音口播转文字和抖音逐字稿，用户粘贴抖音视频链接、分享文案或 aweme_id 后，提取视频上下文、原视频简介和口播逐字稿，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit or check Douyin speech-to-text transcript jobs from a video URL, share text, aweme_id, or existing job_id. The skill returns visible video context, the original description, transcript text, copy-ready text, a concise version, and task status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the provided Douyin URL, share text, aweme_id, or job_id to SocialDataX using SOCIALDATAX_API_KEY. <br>
Mitigation: Use it only when the user is comfortable sharing that input with SocialDataX and has configured the intended SOCIALDATAX_API_KEY. <br>
Risk: Transcript jobs may remain in progress after the initial command. <br>
Mitigation: Keep the returned job_id and poll the same job instead of submitting duplicate transcript jobs. <br>
Risk: Insufficient balance errors can lead to repeated failed submissions. <br>
Mitigation: Stop submitting or polling after an insufficient balance response, show the recharge URL returned by the service, and resume only after the same account is funded. <br>


## Reference(s): <br>
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured transcript sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a job_id, current status, and a follow-up polling command when transcript processing is not complete.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
