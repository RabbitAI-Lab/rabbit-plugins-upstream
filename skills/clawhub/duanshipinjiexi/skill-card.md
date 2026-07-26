## Description: <br>
One-stop short-video parsing and platform watermark-removal guidance for Douyin, Kuaishou, Xiaohongshu, and Pipixia links, with API workflows for retrieving original media, identity-code status, and purchase status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kangleizhui](https://clawhub.ai/user/kangleizhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to parse supported short-video links, retrieve no-watermark media or music assets, and manage identity codes, quotas, and paid package status through the operator's API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send user-supplied video links, generated identity codes, and purchase or status information to a third-party service operator. <br>
Mitigation: Review the operator and service endpoint before use, and avoid sharing sensitive or private links or payment-related details unless the service is approved. <br>
Risk: The automatic connection fallback can discover and use a changed backend host for future parsing requests. <br>
Mitigation: Disable or manually approve fallback host changes unless the new backend source has been verified. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kangleizhui/skills/duanshipinjiexi) <br>
- [API Documentation](artifact/references/api-docs.md) <br>
- [Platform Field Map](artifact/references/field-map.md) <br>
- [Identity Code Rules](artifact/references/key-rules.md) <br>
- [Troubleshooting Guide](artifact/references/troubleshooting.md) <br>
- [Connection Fallback Flow](artifact/references/url-fallback.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API Calls, markdown] <br>
**Output Format:** [Markdown with inline shell commands and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include direct media URLs, status summaries, QR-code generation instructions, and per-platform field handling guidance.] <br>

## Skill Version(s): <br>
1.7.6 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
