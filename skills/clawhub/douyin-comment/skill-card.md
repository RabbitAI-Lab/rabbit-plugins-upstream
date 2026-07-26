## Description: <br>
Guides an agent through searching Douyin for keyword-relevant popular videos and posting comments from an already logged-in browser profile. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mars82311111](https://clawhub.ai/user/mars82311111) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and social-media operators use this skill to guide an agent through Douyin search, popular-video selection, and comment submission tasks. It assumes an already logged-in Douyin account in the OpenClaw browser profile. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can post public Douyin comments through an already logged-in account. <br>
Mitigation: Require manual confirmation before each comment is submitted and review comment text for account, brand, and platform-policy impact. <br>
Risk: The skill may restart local OpenClaw gateway processes after browser timeouts. <br>
Mitigation: Allow automatic gateway restart commands only in environments where the user intentionally permits the skill to manage local OpenClaw processes. <br>


## Reference(s): <br>
- [Douyin](https://www.douyin.com) <br>
- [ClawHub skill page](https://clawhub.ai/mars82311111/douyin-comment) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands] <br>
**Output Format:** [Markdown instructions with browser actions, JavaScript snippets, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces step-by-step agent guidance for browser automation; does not create files as its normal output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
