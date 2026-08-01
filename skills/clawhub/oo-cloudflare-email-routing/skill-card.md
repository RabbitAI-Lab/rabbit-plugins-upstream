## Description: <br>
Cloudflare Email Routing (cloudflare.com). Use this skill for Cloudflare Email Routing requests that read, create, update, or delete routing data through the OOMOL `oo` CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Cloudflare Email Routing through an OOMOL-connected account, including listing routing rules and destination addresses, creating or updating rules, and deleting rules with explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create, update, and delete actions can alter or remove Cloudflare Email Routing rules. <br>
Mitigation: Review the exact payload, target, and expected effect with the user before approving write or destructive actions. <br>
Risk: The skill operates through an OOMOL-connected Cloudflare account. <br>
Mitigation: Install and use it only when the publisher and connected account are trusted for managing Cloudflare Email Routing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cloudflare-email-routing) <br>
- [Cloudflare Email Routing](https://www.cloudflare.com/developer-platform/products/email-routing/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
