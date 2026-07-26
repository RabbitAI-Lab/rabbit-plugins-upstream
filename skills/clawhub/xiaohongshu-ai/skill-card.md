## Description: <br>
Creates Xiaohongshu promotional images, carousel note copy, structured publishing metadata, and can publish user-provided local MP4 video notes only when the user explicitly asks to publish. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[youteacherasia](https://clawhub.ai/user/youteacherasia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and agents use this skill to turn a product, service, event, knowledge point, or personal story prompt into Xiaohongshu-ready promotional images, note text, tags, and a manifest. When explicitly authorized, it can publish generated image notes or a user-provided local MP4 video to Xiaohongshu. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses AI provider API keys and sends prompts or generated visual instructions to third-party AI services. <br>
Mitigation: Avoid confidential, personal, or unreleased information in prompts and configure only the provider key needed for the run. <br>
Risk: XHS_COOKIE can act as the user's Xiaohongshu account for publishing actions. <br>
Mitigation: Keep XHS_COOKIE in environment variables only, exclude it from files and version control, rotate it regularly, and remove it from environments that no longer need publishing access. <br>
Risk: Publishing can post content to Xiaohongshu when explicitly invoked. <br>
Mitigation: Use --dry-run first and review the generated title, description, tags, images, or video before running a real publish command. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/youteacherasia/skills/xiaohongshu-ai) <br>
- [Publisher profile](https://clawhub.ai/user/youteacherasia) <br>
- [Xiaohongshu](https://www.xiaohongshu.com) <br>
- [Volcengine Ark API endpoint](https://ark.cn-beijing.volces.com/api/v3) <br>
- [Artifact README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, files, images, guidance] <br>
**Output Format:** [Markdown guidance with shell commands plus generated PNG files, manifest JSON, note copy, tags, and optional Xiaohongshu publish result links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated image-note output is capped at 9 images; video publishing accepts one local MP4 and optional cover image.] <br>

## Skill Version(s): <br>
1.1.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
