## Description: <br>
Tavily Search Pro lets agents use Tavily for web, news, and finance search, URL extraction, site crawling, sitemap discovery, and deep research with citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaharsha](https://clawhub.ai/user/shaharsha) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to run Tavily-powered search, extraction, crawling, site mapping, finance/news lookup, and research workflows from shell commands. It returns readable text, Markdown, or structured JSON for downstream agent use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches, URLs, crawl targets, and research prompts are sent to Tavily. <br>
Mitigation: Use a revocable Tavily API key, consider an isolated Python environment, and avoid confidential, private, regulated, or internal-only material unless the organization has approved that disclosure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shaharsha/skills/tavily-search-pro) <br>
- [Publisher profile](https://clawhub.ai/user/shaharsha) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands] <br>
**Output Format:** [Plain text, Markdown, or structured JSON emitted by a Python CLI.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TAVILY_API_KEY and may include source URLs, citations, images, raw page content, crawl results, or research reports depending on command options.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
