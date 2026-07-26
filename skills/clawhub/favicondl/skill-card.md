## Description: <br>
通过 HTTPS API 或零依赖 CLI 下载任意网站的可用 favicon，支持尺寸偏好、图片重定向、JSON 元数据和 Windows/Linux/macOS。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sweesama](https://clawhub.ai/user/sweesama) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to fetch favicon images or favicon metadata for arbitrary domains and URLs through the FaviconDL HTTPS API or local CLI wrappers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Favicon requests disclose the target domain or URL to favicondl.com. <br>
Mitigation: Use the skill only for domains or URLs that are appropriate to share with the service. <br>
Risk: The CLI and API may save image files locally, and the returned image format is controlled by the target site. <br>
Mitigation: Keep the neutral .img extension or inspect the content type before treating a downloaded file as a specific image format. <br>
Risk: Optional GitHub raw script downloads are not pinned to immutable release hashes. <br>
Mitigation: Prefer the packaged script when available, and review downloaded scripts before executing them. <br>


## Reference(s): <br>
- [FaviconDL API home](https://favicondl.com) <br>
- [FaviconDL API documentation](https://favicondl.com/documentation.html) <br>
- [OpenAPI specification](https://favicondl.com/openapi.yaml) <br>
- [LLM guidance](https://favicondl.com/llms.txt) <br>
- [Local MCP adapter README](https://github.com/sweesama/favicondl.com/blob/main/mcp/README.md) <br>
- [ClawHub skill page](https://clawhub.ai/sweesama/skills/favicondl) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with REST URLs, JSON examples, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI may save favicon image files locally with a .img extension; API metadata mode returns JSON.] <br>

## Skill Version(s): <br>
2.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
