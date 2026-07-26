## Description: <br>
Searches and reads X/Twitter profiles, timelines, mentions, followers, tweet search, trends, lists, communities, and Spaces, and publishes posts after the user completes OAuth authorization in the browser. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xjordansg-yolo](https://clawhub.ai/user/0xjordansg-yolo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to monitor X/Twitter activity, search social data, inspect profiles and conversations, and publish text or media posts through an AIsa-backed OAuth workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that the AISA API key is exposed in normal command output. <br>
Mitigation: Use a scoped AISA key and avoid running status, authorize, or post commands where logs or terminal output may be shared. <br>
Risk: Posting sends text and local image or video files to AIsa and may publish them publicly on X/Twitter. <br>
Mitigation: Authorize only the intended X/Twitter account and review post text, media paths, and quote or reply targets before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/0xjordansg-yolo/skills/openclaw-twitter) <br>
- [OpenClaw Twitter OAuth Posting Reference](references/post_twitter.md) <br>
- [AIsa API Reference](https://docs.aisa.one/reference/) <br>
- [OpenClaw Homepage](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses from the Twitter/X clients] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, curl, and AISA_API_KEY; posting can return authorization URLs, tweet IDs, tweet links, or error details.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
