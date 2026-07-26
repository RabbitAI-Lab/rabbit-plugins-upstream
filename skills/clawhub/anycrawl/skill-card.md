## Description: <br>
Perform high-performance web scraping, crawling, and Google search with multi-engine support and structured data extraction via the AnyCrawl API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[techlaai](https://clawhub.ai/user/techlaai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to call AnyCrawl for Google search, single-page scraping, and scoped website crawling that returns structured, LLM-ready web content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends target URLs and scraped content requests to a third-party crawling service using an API key. <br>
Mitigation: Use a revocable API key stored in a trusted secret mechanism, and avoid submitting private URLs, internal endpoints, secrets, or confidential content unless approved. <br>
Risk: Broad crawl settings can increase cost, rate-limit exposure, or collect more site content than intended. <br>
Mitigation: Keep crawl limits narrow and use depth, path include, and path exclude controls to scope crawling to approved targets. <br>


## Reference(s): <br>
- [AnyCrawl API Documentation](https://docs.anycrawl.dev) <br>
- [AnyCrawl Website](https://anycrawl.dev) <br>
- [ClawHub Skill Page](https://clawhub.ai/techlaai/skills/anycrawl) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Text, Markdown, JSON, Configuration instructions] <br>
**Output Format:** [JSON response objects containing structured search, scrape, crawl status, and crawled content; scrape content can include markdown, HTML, text, JSON, or screenshots depending on requested formats.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ANYCRAWL_API_KEY; rate limits, crawl limits, and crawl-result retention depend on the AnyCrawl plan.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact/package.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
