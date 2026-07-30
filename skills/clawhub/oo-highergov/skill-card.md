## Description: <br>
HigherGov (highergov.com). Use this skill for ANY HigherGov request - searching and reading data. Whenever a task involves HigherGov, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to query HigherGov through an OOMOL-connected account for agency data, prime contract awards, NAICS codes, and federal, DIBBS, grant, state, or local opportunities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: HigherGov searches route through OOMOL's oo CLI and the user's connected HigherGov account. <br>
Mitigation: Confirm the user is comfortable using the OOMOL-connected HigherGov account before execution and rely on the connector's configured credential flow rather than handling raw tokens. <br>
Risk: First-time setup can require installing the oo CLI or connecting a HigherGov API key in OOMOL. <br>
Mitigation: Run setup steps only after a command fails with a matching installation, authentication, connection, scope, credential, or billing error. <br>


## Reference(s): <br>
- [HigherGov ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-highergov) <br>
- [HigherGov Homepage](https://www.highergov.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; command responses include data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
