## Description: <br>
Firecrawl (firecrawl.dev) lets an agent operate Firecrawl through OOMOL's oo CLI for scraping, crawling, search, URL mapping, structured extraction, usage visibility, and job management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate Firecrawl from Codex through an OOMOL-connected account, including web scraping, crawling, search, URL mapping, structured extraction, async job status checks, cancellations, and usage inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write, cancel, delete, crawl, agent, and deep-research actions can change Firecrawl state or consume account credits. <br>
Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running those actions. <br>
Risk: Connector actions depend on the user's OOMOL-connected Firecrawl account and may fail when authentication, connection scopes, credentials, or billing are unavailable. <br>
Mitigation: Use first-time setup or account remediation steps only after a command fails with the matching authentication, connection, scope, credential, or billing error. <br>


## Reference(s): <br>
- [Firecrawl homepage](https://www.firecrawl.dev) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub Firecrawl skill page](https://clawhub.ai/oomol/skills/oo-firecrawl) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return Firecrawl connector JSON responses containing data and meta.executionId values.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
