## Description: <br>
AI-powered web scraping framework for extracting structured data from websites. Use when Codex needs to crawl, scrape, or extract data from web pages using AI-powered parsing, handle dynamic content, or work with complex HTML structures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codylrn804](https://clawhub.ai/user/codylrn804) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agents use this skill to scrape authorized web pages, handle JavaScript-driven content, and transform HTML into markdown, clean HTML, structured JSON, screenshots, links, or saved files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables broad browser-based scraping and the security review flags anti-bot bypass guidance. <br>
Mitigation: Use only on sites and pages the operator is authorized to access, respect robots.txt and terms of service, and avoid Cloudflare proxy or user-agent bypass guidance. <br>
Risk: The troubleshooting documentation includes an unrelated GitHub login instruction. <br>
Mitigation: Do not run gh auth login for this skill unless there is a separate GitHub task that requires authentication. <br>
Risk: Scraping outputs can retain sensitive data through screenshots, HTML, markdown, JSON, or saved files. <br>
Mitigation: Avoid saving screenshots or HTML from private or authenticated pages unless retention is intended and approved. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/codylrn804/skills/crawl4ai) <br>
- [Crawl4ai API Reference](references/api_reference.md) <br>
- [Crawl4ai Examples](references/examples.md) <br>
- [Crawl4ai Error Handling and Troubleshooting](references/error_handling.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, HTML, files, guidance] <br>
**Output Format:** [Markdown guidance with Python code examples, shell commands, and optional JSON, HTML, markdown, screenshot, and file outputs from scraping utilities.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include scraped page content, structured extracted data, links, status metadata, screenshots, and per-page files when using the bundled scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
