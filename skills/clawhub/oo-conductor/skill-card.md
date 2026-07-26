## Description: <br>
Provides agent guidance for reading Conductor Monitoring websites, pages, segments, issues, affected pages, and statistics through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators with connected Conductor accounts use this skill to let an agent inspect live action schemas and retrieve Conductor Monitoring data through OOMOL-managed credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read data from a connected Conductor account through OOMOL. <br>
Mitigation: Install it only when that account access is intended, and review the Conductor connection scopes before use. <br>
Risk: Fallback setup includes remote CLI installer commands if the oo CLI is missing. <br>
Mitigation: Prefer an already installed oo CLI when available, and review installer commands before running them. <br>


## Reference(s): <br>
- [ClawHub Conductor skill page](https://clawhub.ai/oomol/skills/oo-conductor) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Conductor homepage](https://www.conductor.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Conductor Monitoring data access; live connector schema inspection is expected before action payloads are built.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
