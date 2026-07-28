## Description: <br>
Google Search (Free) helps an agent run browser-based Google searches without a Google API key, parse titles, URLs, and snippets, apply basic filtering, and export results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and automation agents can use this skill for lightweight Google search, SEO keyword checks, quick information retrieval, research collection, result parsing, basic filtering, and export workflows. It is not intended for black-hat SEO tactics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup guidance includes an unsafe remote installer command. <br>
Mitigation: Review installer commands before use and prefer an already installed Node.js runtime or a verified package-manager installation path. <br>
Risk: Browser-based Google searches may leave the user's machine and depend on local network, proxy, and regional settings. <br>
Mitigation: Install only in environments where browser-based Google search is acceptable, and adjust language, country, and proxy settings for the deployment context. <br>


## Reference(s): <br>
- [Detailed usage and code examples](references/detail.md) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/free-google-search-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Bun installer referenced by setup instructions](https://bun.sh/install) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with Python and shell command examples; exported search results may be JSON, CSV, Markdown, or plain text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-query free edition; uses browser automation and may require Node.js or Bun, Playwright, Chromium, and network access to Google.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
