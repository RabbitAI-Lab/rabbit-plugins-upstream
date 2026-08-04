## Description: <br>
A unified web crawler that fetches individual pages with optional JavaScript rendering, CSS selector extraction, and fallback fetching, or crawls sites with BFS, checkpoint resume, and content cleaning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to extract clean Markdown from individual static or JavaScript-rendered pages, or to crawl documentation sites into local JSON for downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can contact external websites and render pages in Chromium, which may fetch third-party content beyond the requested page. <br>
Mitigation: Use it only for intended public or approved targets, keep same-domain crawling enabled unless broader crawling is deliberate, and set page limits for site crawls. <br>
Risk: The fetch mode can execute user-supplied JavaScript in the page context. <br>
Mitigation: Avoid custom JavaScript on sensitive or authenticated pages and review any JavaScript before running it. <br>
Risk: Crawl mode saves extracted content and checkpoint files on disk. <br>
Mitigation: Choose output directories deliberately and avoid crawling pages containing secrets, personal data, or content that should not be persisted locally. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands] <br>
**Output Format:** [Markdown text for single-page fetches; JSON objects or JSON array files for metadata-rich fetches and site crawls.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Crawl mode writes local result and checkpoint files; fetch mode can write output to a user-selected file.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
