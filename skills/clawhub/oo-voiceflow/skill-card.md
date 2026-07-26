## Description: <br>
Voiceflow lets an agent read, create, and update Voiceflow data through an OOMOL-connected account instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workspace users use this skill to operate Voiceflow conversations, environments, and knowledge base queries through the OOMOL oo connector from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill lets Codex act through the user's OOMOL-connected Voiceflow account, including the write-tagged start_session action. <br>
Mitigation: Install only when that account access is intended, inspect the connector schema, and confirm the exact action payload before write operations. <br>
Risk: Credential handling and connector execution depend on OOMOL account setup and server-side credential injection. <br>
Mitigation: Use the documented setup flow only when an auth, connection, scope, credential, or billing error occurs; do not handle raw Voiceflow tokens in the agent session. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-voiceflow) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Voiceflow Homepage](https://www.voiceflow.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON connector payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses include data and an execution id.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
