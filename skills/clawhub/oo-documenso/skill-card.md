## Description: <br>
Documenso helps agents search and read Documenso envelopes and templates through OOMOL's oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when an agent needs to retrieve individual Documenso envelopes or templates, or list envelopes and templates with filters. It is intended for connected OOMOL accounts with Documenso access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on an OOMOL-connected Documenso account and may expose account-scoped envelope or template data to agent workflows. <br>
Mitigation: Review OOMOL and Documenso connection scopes during setup, and require explicit confirmation before enabling any future action that writes, deletes, or overwrites data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-documenso) <br>
- [Documenso](https://documenso.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector responses as JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
