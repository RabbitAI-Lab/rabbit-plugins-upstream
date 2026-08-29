## Description:

Adscrawl Browser helps agents extract rendered webpages as Markdown, structured JSON, or HTML, capture PNG screenshots, and create remote CDP browser sessions for multi-step website interaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adscrawl](https://clawhub.ai/user/adscrawl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an agent needs browser-rendered website content, screenshots, or a remote browser session for interaction-heavy pages that ordinary HTTP fetches cannot handle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may send requested URLs, browser tasks, cookies, login flows, personal data, proxies, or website actions to AdsCrawl.

Mitigation: Install only when this service use is intended, and authorize sensitive data, login flows, proxies, and website actions only for specific tasks.

Risk: API keys, CDP token-bearing URLs, cookies, or proxy credentials could be exposed in logs, prompts, code, commits, or final responses.

Mitigation: Keep secrets in environment variables, avoid printing token-bearing URLs, and report only safe error details.

Risk: Remote browser sessions can persist state or consume capacity if left open.

Mitigation: Use CDP only for multi-step tasks, reuse sessions for related work, close sessions in cleanup paths, and observe timeout and capacity limits.

Risk: Rendered extraction or screenshots may capture challenge pages, overlays, missing assets, or incomplete lazy-loaded content.

Mitigation: Verify saved content or screenshots before relying on them, and retry at most once with a more appropriate navigation strategy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adscrawl/skills/adscrawl)
- [Server-resolved GitHub provenance](https://github.com/AdsCrawl/skills/tree/main/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell, JSON, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to produce Markdown, HTML, JSON, PNG screenshots, or CDP session configuration through the AdsCrawl service.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
