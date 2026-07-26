## Description: <br>
Use a self-hosted SearXNG search engine to give agents free, self-hostable meta-search across general, code, academic, video, and image sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeshunee](https://clawhub.ai/user/leeshunee) <br>

### License/Terms of Use: <br>
GNU GPL v3.0 <br>


## Use Case: <br>
Developers, engineers, and agent operators use this skill to install or connect to a SearXNG service, manage the local search service, and retrieve search results for research or resource discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation can run shell commands, modify local service configuration, and enable autostart. <br>
Mitigation: Review the Python script and onboarding commands before installation, run them in a controlled Linux or WSL environment, and enable autostart only when a persistent local service is intended. <br>
Risk: Pipe-to-shell installation and service setup may execute code retrieved from external sources. <br>
Mitigation: Avoid running installer commands blindly; inspect downloaded install scripts and use trusted network paths before execution. <br>
Risk: Untrusted SEARXNG_HOST or SEARXNG_PORT values can redirect agent searches to an unintended service. <br>
Mitigation: Use trusted local or explicitly approved SearXNG endpoints and validate host and port settings before searching. <br>
Risk: Search queries may be processed by the local SearXNG service and upstream search engines. <br>
Mitigation: Do not submit secrets, credentials, or sensitive internal data as search queries. <br>


## Reference(s): <br>
- [SearXNG Search CLI Onboarding](references/ONBOARDING.md) <br>
- [SearXNG Official Docs](https://docs.searxng.org) <br>
- [SearXNG Project](https://github.com/searxng/searx) <br>
- [ClawHub Skill Page](https://clawhub.ai/leeshunee/skills/searxng-search-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with command examples and search-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search behavior depends on a reachable SearXNG service, selected engines, language, pagination, safe-search, time range, and result limit.] <br>

## Skill Version(s): <br>
1.3.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
