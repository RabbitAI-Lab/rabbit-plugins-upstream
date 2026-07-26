## Description: <br>
Fliz AI Video Generator helps agents guide developers through Fliz REST API workflows for creating, monitoring, translating, duplicating, and receiving webhook notifications for AI-generated videos from text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jb-fliz](https://clawhub.ai/user/jb-fliz) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and automation builders use this skill to integrate Fliz video generation into agents, custom apps, CMS workflows, and automation platforms. It covers API authentication, video creation from text, status polling, translation, duplication, resource listing, and webhook handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text, URLs, and metadata supplied to the skill may be sent to Fliz for video generation. <br>
Mitigation: Use only content your organization permits sharing with Fliz, and avoid secrets, private documents, regulated data, or proprietary material unless that sharing is approved. <br>
Risk: The webhook example includes history and test endpoints intended for local debugging. <br>
Mitigation: Remove, authenticate, or otherwise lock down debug and history endpoints before exposing a webhook handler beyond local development. <br>
Risk: Video generation can require manual intervention or enter failed states. <br>
Mitigation: Implement status polling, error handling, and user-action handling before relying on generated videos in an automated workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jb-fliz/skills/fliz-ai-video-generator) <br>
- [Publisher Profile](https://clawhub.ai/user/jb-fliz) <br>
- [Fliz Website](https://fliz.ai) <br>
- [Fliz API Documentation](https://app.fliz.ai/api-docs) <br>
- [API Reference](references/api-reference.md) <br>
- [Enum Values](references/enums-values.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with JSON, Python, JavaScript, and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Fliz API key, commonly provided through FLIZ_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
