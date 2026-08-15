## Description: <br>
Domain/DNS ops across Cloudflare, DNSimple, and Namecheap for onboarding zones to Cloudflare, flipping nameservers, setting redirects, updating redirect-worker mappings, and verifying DNS/HTTP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage domain onboarding, DNS changes, nameserver delegation, redirects, Cloudflare bot settings, and verification for the publisher's manager repository workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Nameserver flips, DNS records, redirects, and bot-protection changes can affect live production domains. <br>
Mitigation: Confirm the domain, registrar, Cloudflare zone, redirect target, token permissions, and rollback plan before execution; verify DNS and HTTP behavior after each change. <br>
Risk: The skill depends on the publisher's local ~/Projects/manager workflow and repository contents. <br>
Mitigation: Use the manager repository as the source of truth and review any repository edits before committing or pushing. <br>


## Reference(s): <br>
- [manager-repo.md](artifact/references/manager-repo.md) <br>
- [ClawHub skill page](https://clawhub.ai/steipete/skills/domain-dns-ops) <br>
- [Publisher profile](https://clawhub.ai/user/steipete) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and operational checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose live DNS, registrar, Cloudflare, redirect, and repository changes that require user approval and verification.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
