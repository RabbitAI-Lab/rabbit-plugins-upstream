## Description: <br>
Firecrawler uses the Firecrawl API to scrape pages as markdown, capture screenshots, extract structured data, search the web, crawl documentation sites, and map site URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[capt-marbles](https://clawhub.ai/user/capt-marbles) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use Firecrawler to collect webpage content, screenshots, search results, structured extracts, and documentation crawls through Firecrawl-backed commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: URLs, search terms, schemas, and extraction prompts may be sent to Firecrawl. <br>
Mitigation: Use only approved public or non-sensitive inputs unless Firecrawl is approved for the relevant data. <br>
Risk: Large crawls or searches can consume credits and collect more content than intended. <br>
Mitigation: Set reasonable crawl, search, and map limits before running commands. <br>
Risk: Screenshots and crawl results can write files into user-selected output paths. <br>
Mitigation: Choose trusted output locations and review generated files before reusing or sharing them. <br>
Risk: An unpinned Firecrawl SDK version can change behavior across environments. <br>
Mitigation: Pin the Firecrawl SDK version when installing the dependency for repeatable use. <br>


## Reference(s): <br>
- [Firecrawl](https://firecrawl.dev) <br>
- [Firecrawl API Keys](https://www.firecrawl.dev/app/api-keys) <br>
- [Firecrawler on ClawHub](https://clawhub.ai/capt-marbles/skills/firecrawler) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown and text output, JSON extracts, URL lists, and optional PNG or markdown files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires FIRECRAWL_API_KEY and the firecrawl Python SDK; crawl and map commands accept user-selected limits.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
