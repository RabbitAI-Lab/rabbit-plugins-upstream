## Description: <br>
一个全面的GSAP动画生成工具，提供AI驱动的意图分析、完整的API覆盖和生产就绪的动画模式，帮助开发者快速创建高性能动画。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to generate, debug, optimize, and explain GSAP animations from natural-language requests or existing animation code. It routes animation tasks to XiaoBenYang API-backed tools and returns the resulting code, setup guidance, performance advice, or troubleshooting output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends animation prompts and optional source code to the XiaoBenYang remote API. <br>
Mitigation: Do not submit proprietary code, secrets, internal URLs, customer data, or other sensitive content unless acceptable privacy, retention, and key-handling terms are in place. <br>
Risk: The skill collects and stores an XBY API key in a local .env file. <br>
Mitigation: Use a dedicated low-privilege API key where possible and remove the local .env entry when the skill is no longer needed. <br>
Risk: Stale Gaokao and school-search remnants make the implementation scope less clear. <br>
Mitigation: Review the skill files and generated outputs before deployment, especially around data sent to the external API. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/gsap-animation-generate) <br>
- [XiaoBenYang API key page](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown or structured text summarizing remote API results, often including code snippets and configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY API key and may send animation prompts or source code to the XiaoBenYang remote API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
