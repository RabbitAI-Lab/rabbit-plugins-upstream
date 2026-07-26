## Description: <br>
Extract structured data from websites, including tables, lists, prices, articles, metadata, and parsed HTML, with zero external dependencies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to turn web pages or raw HTML into structured text and data for analysis, monitoring, and downstream automation. It is useful when an agent needs tables, lists, prices, article previews, metadata, or change diffs without adding external packages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cache and watch modes can persist scraped page content, snapshots, and diffs in local workspace storage. <br>
Mitigation: Use --no-cache for normal extraction when persistence is not acceptable, avoid watch mode for sensitive pages, and remove memory/scraper-cache data when retention is no longer needed. <br>
Risk: The skill sends user-provided URLs over the network and can process sensitive, authenticated, internal, or regulated page content if directed to do so. <br>
Mitigation: Use only approved public targets unless the workspace storage, retention, and network handling are acceptable for the data being scraped. <br>


## Reference(s): <br>
- [ClawHub Smart Scraper Skill Page](https://clawhub.ai/jlacroix82/skills/smart-scraper-web) <br>
- [Release README](artifact/README.md) <br>
- [Security Audit](artifact/AUDIT.md) <br>
- [ClawHub Release Metadata](artifact/clawhub.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text and structured extraction summaries with optional JSON-like data from the Node.js API] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Network extraction supports http and https public URLs; cache and watch modes may write scraped content or snapshots to local workspace storage.] <br>

## Skill Version(s): <br>
1.3.7 (source: server release metadata and artifact/clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
