## Description: <br>
Searches DuckDuckGo for web pages, news, images, and videos with configurable filters and text, markdown, JSON, or saved-file outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anisafifi](https://clawhub.ai/user/anisafifi) <br>

### License/Terms of Use: <br>
Proprietary <br>


## Use Case: <br>
Developers and external agent users use this skill to gather current web, news, image, and video search results through a DuckDuckGo-backed command-line helper. It is suited for research, fact-checking, current-event checks, visual-resource discovery, and saved search reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to an external search provider. <br>
Mitigation: Avoid sending sensitive, confidential, or regulated information in search queries. <br>
Risk: Saved search output can overwrite files or unintentionally persist sensitive research topics. <br>
Mitigation: Use explicit intended output paths and review saved files before sharing or committing them. <br>
Risk: Dependency installation can affect system Python environments. <br>
Mitigation: Install dependencies from trusted sources in a virtual environment. <br>


## Reference(s): <br>
- [Web Search Hub on ClawHub](https://clawhub.ai/anisafifi/skills/web-search-hub) <br>
- [OpenClawCLI](https://clawhub.ai/) <br>
- [DuckDuckGo Search Python Package](https://pypi.org/project/duckduckgo-search/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Plain text, Markdown, JSON, or saved result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include URLs, summaries, image metadata, video metadata, source names, dates, and optional file paths.] <br>

## Skill Version(s): <br>
0.1.3 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
