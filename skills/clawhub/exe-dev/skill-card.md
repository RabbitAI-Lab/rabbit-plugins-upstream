## Description: <br>
Manage persistent VMs on exe.dev. Create VMs, configure HTTP proxies, share access, and set up custom domains. Use when working with exe.dev VMs for hosting, development, or running persistent services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bjesuiter](https://clawhub.ai/user/bjesuiter) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to manage exe.dev persistent VMs for hosting, development, and long-running services, including VM creation, proxy configuration, sharing, and custom domains. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can create VMs or change VM sharing, ports, users, links, and domains. <br>
Mitigation: Confirm the exact VM, intended audience, authentication state, exposed service, and cost or data exposure impact before running these commands. <br>
Risk: Public sharing actions can expose hosted services more broadly than intended. <br>
Mitigation: Review public access settings, invited users, generated links, and custom-domain routing before making a service public. <br>


## Reference(s): <br>
- [exe.dev documentation](https://exe.dev/docs/all.md) <br>
- [exe.dev VM service reference](artifact/references/exe-dev-vm-service.md) <br>
- [ClawHub skill page](https://clawhub.ai/bjesuiter/skills/exe-dev) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Command reference for exe.dev VM operations; users should confirm public exposure, user access, ports, domains, and cost-impacting VM changes before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
