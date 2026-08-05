## Description: <br>
Query Google Search Console, Bing Webmaster Tools, Google Analytics 4 (GA4), and PageSpeed Insights through one self-hosted MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, site owners, and SEO operators use rankrat to let an agent inspect search, indexing, ranking, analytics, and PageSpeed data for sites they already control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Provider credentials and OAuth records are needed for operation. <br>
Mitigation: Run rankrat only where you control the configured provider accounts, keep credentials on the host, and mount only the required config, secrets, and OAuth directories. <br>
Risk: HTTP mode can expose the MCP and REST API beyond the local machine if bound or published too broadly. <br>
Mitigation: Bind HTTP to loopback or a private network and require a bearer token whenever anything else can reach the service. <br>
Risk: Writable or unbounded onboarding modes can modify provider resources or expand the configured boundary. <br>
Mitigation: Keep read-only mode enabled for normal use and enable writable or unbounded mode only for trusted, supervised onboarding sessions. <br>
Risk: The skill is intended for sites and accounts the operator controls, not arbitrary domains or competitor research. <br>
Mitigation: Configure boundaries only for owned properties and verify provider readiness before relying on reports. <br>


## Reference(s): <br>
- [rankrat setup reference](references/setup.md) <br>
- [rankrat ClawHub skill page](https://clawhub.ai/psyb0t/skills/rankrat) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide MCP or REST API calls against configured provider accounts and return provider-derived SEO, indexing, analytics, or performance observations.] <br>

## Skill Version(s): <br>
0.2.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
