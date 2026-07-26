## Description: <br>
Qlty helps agents search and read Qlty data through the OOMOL oo CLI connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to inspect Qlty users, workspaces, projects, project metrics, issues, and rate-limit status through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill brokers account-specific Qlty access through OOMOL's oo CLI. <br>
Mitigation: Install it only when that broker is acceptable for the workspace and keep use to the documented read-only Qlty actions. <br>
Risk: Future connector actions could change or delete Qlty data if write or destructive actions are added. <br>
Mitigation: Confirm the exact payload and effect with the user before write actions, and require explicit approval before destructive actions. <br>
Risk: First-time setup may require installing the oo CLI or connecting Qlty credentials. <br>
Mitigation: Run setup steps only after matching auth or connection failures, and review installer, login, connection, and billing commands before execution. <br>


## Reference(s): <br>
- [Qlty homepage](https://qlty.sh) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qlty) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, json] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the oo CLI to inspect live action schemas before sending connector payloads; submitted actions are read-only.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
