## Description: <br>
Web data for everyone. Powered by Firecrawl. Scrape, search, crawl, interact with websites — all in plain language. No technical skills needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search the web, scrape pages, map or crawl sites, interact with pages, and extract structured data through Firecrawl. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requested URLs, search terms, page contents, extraction prompts, and interaction instructions are sent to Firecrawl. <br>
Mitigation: Avoid confidential pages or sensitive inputs unless the user understands and accepts the third-party data flow. <br>
Risk: Interactive actions can click, fill forms, log in, or download files on a target site. <br>
Mitigation: Confirm the target site, intended action, and authorization with the user before running interact. <br>
Risk: Crawling can visit many pages and may burden target sites or violate site terms. <br>
Mitigation: Respect robots.txt and terms of service, keep page limits conservative, and ask before large crawls. <br>


## Reference(s): <br>
- [ClawHub Firecrawl Wrapper listing](https://clawhub.ai/tobewin/skills/firecrawl-wrapper) <br>
- [Firecrawl documentation](https://docs.firecrawl.dev) <br>
- [Firecrawl open source project](https://github.com/firecrawl/firecrawl) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use FIRECRAWL_API_KEY. Command responses can include search results, scraped markdown, crawl status, interaction output, or extracted structured data.] <br>

## Skill Version(s): <br>
1.1.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
