## Description: <br>
Hetzner Cloud CLI for managing servers, volumes, firewalls, networks, DNS, and snapshots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pasogott](https://clawhub.ai/user/pasogott) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and cloud operators use this skill to get Hetzner Cloud CLI setup guidance and command examples for managing infrastructure resources with explicit confirmation and credential-safety safeguards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help propose commands that create or modify billable Hetzner Cloud resources. <br>
Mitigation: Use a dedicated, least-privilege Hetzner API token and require explicit approval after reviewing the exact command. <br>
Risk: Cloud-management guidance may expose credentials if tokens are copied into prompts, logs, or command output. <br>
Mitigation: Do not share API tokens with the agent, and keep tokens stored through local hcloud context configuration. <br>
Risk: Infrastructure changes can disrupt existing resources if applied without recovery preparation. <br>
Mitigation: Create or confirm a current snapshot before approving modify operations. <br>


## Reference(s): <br>
- [Hetzner Cloud CLI repository](https://github.com/hetznercloud/cli) <br>
- [Hetzner Cloud Console](https://console.hetzner.cloud/) <br>
- [ClawHub skill page](https://clawhub.ai/pasogott/skills/hetzner-cloud) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hcloud command examples, JSON/YAML output-format suggestions, and confirmation prompts for create or modify operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
