## Description: <br>
Laposta (laposta.nl). Use this skill for ANY Laposta request - reading, creating, and updating data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Laposta mailing lists and members through an OOMOL-connected account, including listing, retrieving, creating, and updating records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create or update Laposta mailing lists and members. <br>
Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write actions. <br>
Risk: The skill operates mailing-list data through an OOMOL-connected account. <br>
Mitigation: Use it only with an intended Laposta connection and inspect the live action schema before constructing payloads. <br>
Risk: CLI installation, authentication, or connection recovery can change the local or account setup. <br>
Mitigation: Run install, login, or connection steps only after a matching command failure and only when the OOMOL tooling is trusted. <br>


## Reference(s): <br>
- [Laposta homepage](https://laposta.nl/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-laposta) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
