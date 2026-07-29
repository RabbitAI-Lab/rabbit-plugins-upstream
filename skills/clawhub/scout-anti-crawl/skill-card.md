## Description: <br>
Scout Anti-Crawl v3 helps agents fetch web pages through a six-layer fallback flow for static HTTP, browser rendering, stealth browsing, local Obscura, Olostep, and Firecrawl. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[garisonli](https://clawhub.ai/user/garisonli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to retrieve web content, extract text, save fetched pages, and search WeChat/Sogou results when ordinary HTTP fetching is blocked by JavaScript rendering, login walls, or anti-crawl systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release embeds a third-party Olostep API key. <br>
Mitigation: Remove and rotate the embedded key before use; require users to provide their own credential through an approved secret-management path. <br>
Risk: Automatic cloud fallbacks can send user-selected URLs to third-party scraping services without a clear opt-in step. <br>
Mitigation: Disable cloud fallbacks by default or require explicit user approval before routing URLs to Olostep or Firecrawl, especially in sensitive workspaces. <br>
Risk: The skill is intended for public URL scraping and may be unsuitable for sensitive or private targets. <br>
Mitigation: Use only for public URLs the user is comfortable routing through a local proxy and third-party scraping services. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/garisonli/skills/scout-anti-crawl) <br>
- [Olostep](https://olostep.com) <br>
- [Scrapling](https://github.com/D4Vinci/Scrapling) <br>
- [Firecrawl](https://github.com/firecrawl/firecrawl) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files] <br>
**Output Format:** [CLI output containing fetched HTML, extracted plain text, Markdown, JSON-like search results, or saved page content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route user-selected URLs through a local proxy and third-party scraping services depending on fallback layer.] <br>

## Skill Version(s): <br>
3.0.0 (source: ClawHub release, SKILL.md frontmatter, skill.json, _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
