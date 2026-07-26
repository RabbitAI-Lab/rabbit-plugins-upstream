## Description: <br>
Fairing connector skill for searching and reading Fairing survey response data through the OOMOL oo CLI instead of direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect the live Fairing connector schema and retrieve paginated Fairing survey responses through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on OOMOL and the oo CLI setup path for connector execution and credential handling. <br>
Mitigation: Install and use it only when you trust OOMOL, the oo CLI, and the connected Fairing account. <br>
Risk: Future connector actions tagged write or destructive could change or remove Fairing data. <br>
Mitigation: Confirm the exact payload and effect with the user before write actions, and require explicit approval for destructive actions. <br>
Risk: A stale assumed payload can fail or request the wrong Fairing data. <br>
Mitigation: Inspect the live action schema with `oo connector schema` before constructing each `oo connector run` payload. <br>


## Reference(s): <br>
- [ClawHub Fairing skill page](https://clawhub.ai/oomol/skills/oo-fairing) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Fairing homepage](https://fairing.co) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON response guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before running actions; Fairing credentials are handled by OOMOL server-side.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
