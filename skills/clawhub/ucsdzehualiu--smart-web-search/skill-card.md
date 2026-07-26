## Description: <br>
Smart web search with auto region detection and dual-tier content fetching. Works in both China and international networks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ucsdzehualiu](https://clawhub.ai/user/ucsdzehualiu) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and agent users use this skill to search the web across China and international networks, fetch selected result content, and return source material for research or troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms, public IP address, and visited result URLs may be exposed to external search engines, IP lookup services, and destination websites. <br>
Mitigation: Use the skill only for searches appropriate for external services, disable fetching with --fetch=0 or --no-fetch for sensitive searches, and select an explicit region when needed. <br>
Risk: Automatic content fetching can visit arbitrary result pages. <br>
Mitigation: Review returned URLs and run the skill in a contained environment before using fetched content in downstream work. <br>
Risk: The browser fallback disables Chromium sandboxing. <br>
Mitigation: Run browser fallback in an isolated environment with least-privilege permissions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ucsdzehualiu/smart-web-search) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain text search results with URLs and fetched page excerpts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts query, max result count, fetch count, and region controls.] <br>

## Skill Version(s): <br>
3.2.2 (source: frontmatter, package.json, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
