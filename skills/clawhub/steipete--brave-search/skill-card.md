## Description: <br>
Web search and content extraction via Brave Search API. Use for searching documentation, facts, or any web content. Lightweight, no browser required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to search the web, retrieve current facts or documentation, and optionally extract readable page content as Markdown without launching a browser. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and fetched URLs are sent to external websites. <br>
Mitigation: Do not include secrets, proprietary internal terms, or internal-only URLs in queries or content extraction requests. <br>
Risk: Extracted webpage content may be inaccurate, malicious, or otherwise untrusted. <br>
Mitigation: Treat extracted content as reference material and verify important claims before acting on them. <br>
Risk: The artifact advertises BRAVE_API_KEY, but this version does not use that API key. <br>
Mitigation: Do not rely on API-key based access control or quota behavior for this release. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Plain text search results with optional Markdown page content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search output includes title, link, snippet, and optional extracted page content capped by the script.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
