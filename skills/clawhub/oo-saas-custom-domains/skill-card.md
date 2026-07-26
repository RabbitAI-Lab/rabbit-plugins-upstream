## Description: <br>
SaaS Custom Domains helps agents manage accounts, upstreams, custom domains, DNS verification, and HTTP cache purging through OOMOL's oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect and administer SaaS Custom Domains resources through OOMOL, including listing accounts, managing upstreams and custom domains, verifying DNS records, and purging cache. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write or destructive connector actions can create, delete, or purge SaaS Custom Domains resources. <br>
Mitigation: Confirm the exact target, payload, and expected effect with the user before running those actions. <br>
Risk: First-time setup may require installing or authenticating the OOMOL CLI. <br>
Mitigation: Verify the OOMOL CLI installer and account connection before setup, and run setup only after an auth or connection failure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-saas-custom-domains) <br>
- [SaaS Custom Domains homepage](https://saascustomdomains.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
