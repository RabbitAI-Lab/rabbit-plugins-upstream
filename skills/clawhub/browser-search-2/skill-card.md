## Description: <br>
Browser Search gives agents multi-engine web search plus browser-based page reading and scraping for web research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johell1ns](https://clawhub.ai/user/johell1ns) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search the web, browse JavaScript-heavy pages, extract page content, and compile multi-source research findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives agents broad browser, scraping, and safety-bypass capabilities. <br>
Mitigation: Use it only for authorized web research, keep default protections enabled, and review targets before escalating to protected-site browsing. <br>
Risk: Browser sessions, local API keys, persistent profiles, and evaluated page JavaScript can expose sensitive context. <br>
Mitigation: Use non-sensitive browser contexts, store keys only in environment variables, and clear tabs, sessions, and persistent profiles after use. <br>
Risk: Bulk scraping or disabled rate limits can violate site policies or create operational risk. <br>
Mitigation: Keep rate limits enabled by default and require explicit approval before using bulk scraping, proxies, or unsafe flags. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/johell1ns/skills/browser-search-2) <br>
- [Source repository](https://github.com/Johell1NS/browser-search) <br>
- [Server-resolved source commit](https://github.com/Johell1NS/browser-search/tree/594d151c6a3de3aa92104cfe9cb5cf7436735e1d) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command templates and JSON or text browser outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save PNG screenshots when explicitly requested by a documented browser command.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
