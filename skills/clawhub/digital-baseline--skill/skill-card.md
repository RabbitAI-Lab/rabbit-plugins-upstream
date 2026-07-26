## Description: <br>
BuildStack Site Builder helps agents create, deploy, edit, and optimize BuildStack websites through the BuildStack API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[digital-baseline](https://clawhub.ai/user/digital-baseline) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and site operators use this skill to have an agent gather site requirements, call BuildStack APIs, publish generated websites, manage CMS content, and run SEO/GEO maintenance tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publish and edit actions can make live public-site changes. <br>
Mitigation: Ask for a preview or explicit confirmation before publishing or modifying a live site, and review generated content before it goes public. <br>
Risk: The BUILDSTACK_API_KEY grants access to BuildStack site-management actions if exposed. <br>
Mitigation: Keep the API key out of chat, logs, screenshots, and command history; rotate it immediately if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/digital-baseline/skills/skill) <br>
- [BuildStack homepage](https://buildstack.com.cn) <br>
- [BuildStack API base URL](https://buildstack.com.cn/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return BuildStack site URLs, deployment status, CMS update summaries, SEO/GEO diagnostics, and user-facing upgrade or recovery guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skillhub metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
