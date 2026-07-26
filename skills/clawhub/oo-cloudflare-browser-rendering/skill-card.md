## Description: <br>
Cloudflare Browser Run helps agents render URLs or raw HTML through Cloudflare Browser Run and return rendered HTML, Markdown, links, selected elements, or structured JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when an agent needs browser-rendered page content from Cloudflare Browser Run, including HTML, Markdown, links, extracted JSON, selected element scraping, or account listing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: URLs, raw HTML, rendered page content, and scrape targets may be processed through the OOMOL and Cloudflare connector. <br>
Mitigation: Avoid submitting sensitive or regulated content unless the connected services and account configuration are approved for that data. <br>
Risk: One-time install, login, and connection commands can change the local setup or account connection state. <br>
Mitigation: Run setup commands only when an action fails because the CLI, authentication, or Cloudflare Browser Run connection is missing or expired. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cloudflare-browser-rendering) <br>
- [Cloudflare Browser Run Documentation](https://developers.cloudflare.com/browser-run/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on the selected Cloudflare Browser Run action and may include rendered HTML, Markdown, links, selected element data, structured JSON, or account information.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
