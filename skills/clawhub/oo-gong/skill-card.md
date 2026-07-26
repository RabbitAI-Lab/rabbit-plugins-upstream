## Description: <br>
Gong support for searching and reading Gong data through OOMOL's oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and teams with OOMOL-connected Gong accounts use this skill to inspect live connector schemas and read Gong calls, transcripts, users, and call outcomes via the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Gong queries and returned call or transcript data are routed through OOMOL's CLI-backed connector service. <br>
Mitigation: Install and use the skill only if OOMOL is trusted as a connector provider for the Gong account and the user is comfortable with that routing. <br>
Risk: The fallback CLI installation path downloads and runs a remote installer. <br>
Mitigation: Review the remote oo CLI installer source before using the fallback install command. <br>
Risk: Future or schema-discovered actions tagged write or destructive could change, remove, or overwrite Gong data. <br>
Mitigation: Fetch the authoritative action schema before constructing payloads and get explicit user confirmation for any write or destructive action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gong) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Gong homepage](https://www.gong.io/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-oriented Gong connector actions; live schemas are fetched before payload construction.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
