## Description: <br>
Smart Search MCP 是一个专注于技术领域的智能搜索工具集，提供14个增强型搜索工具，覆盖国际和国内主流技术平台，具备智能URL生成、输入验证、高级搜索技巧等功能，适用于开发者快速查找技术文档、API参考、开源项目等。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to route search requests across general web search, GitHub, StackOverflow, package registries, technical documentation, API references, and Chinese developer platforms. It helps an agent collect search URLs and API responses that can be summarized for technical research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a XiaoBenYang API key locally in .env. <br>
Mitigation: Keep .env out of commits and shared workspaces, rotate exposed keys, and limit use to environments where local credential storage is acceptable. <br>
Risk: Search terms are sent to the XiaoBenYang backend and may be forwarded to downstream search sites. <br>
Mitigation: Avoid sensitive internal, confidential, regulated, or personal queries unless the data sharing path is approved. <br>
Risk: The security summary notes stale admissions-related references that do not match the search-tool purpose. <br>
Mitigation: Review the instructions before deployment and remove or correct stale gaokao references so agents do not follow irrelevant workflow cues. <br>
Risk: The security guidance recommends dependency pinning before broad use. <br>
Mitigation: Pin and review Python dependencies in requirements.txt for production or enterprise deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/xby-smart-search) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown summaries from JSON API responses and generated search URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value and returns success, raw, and message fields from the upstream API wrapper.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
