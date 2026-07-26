## Description: <br>
加豆AI is an enterprise marketing agent platform for AI-generated video, product photography, digital spokesperson clips, product scene images, product posters, Xiaohongshu-style notes, and social media account management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiadouai](https://clawhub.ai/user/jiadouai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketers, ecommerce operators, and content teams use this skill to generate marketing media, prepare product-focused visual assets, analyze or remix videos, and publish approved image or video posts to connected social accounts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent token access is required for the remote 加豆AI MCP service. <br>
Mitigation: Install only if the publisher is trusted, confirm the service name and endpoint with the publisher, and use the least-privileged or temporary token available. <br>
Risk: Media, prompts, and uploaded files pass through remote service and cloud storage workflows. <br>
Mitigation: Avoid sensitive files or private media, and manually approve uploads before sending content to the service. <br>
Risk: Connected social accounts can be used for image or video publishing. <br>
Mitigation: Manually confirm the destination account, post content, schedule, and platform before approving any publishing action. <br>


## Reference(s): <br>
- [加豆AI homepage](https://www.jiadouai.com) <br>
- [加豆AI ClawHub skill page](https://clawhub.ai/jiadouai/skills/jiadouai) <br>
- [Authentication and token setup](references/auth.md) <br>
- [Common interfaces and workflows](references/workflows.md) <br>
- [Video publishing](references/video_publish.md) <br>
- [Image publishing](references/image_publish.md) <br>
- [Unsupported feature reporting](references/unsupported_feature_reporting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, API Calls, Media URLs] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON arguments; service results may include generated media URLs, job IDs, status data, or social publishing task IDs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires configured mcporter access to the remote 加豆AI MCP service; generation and publishing workflows may require asynchronous status polling.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter says 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
