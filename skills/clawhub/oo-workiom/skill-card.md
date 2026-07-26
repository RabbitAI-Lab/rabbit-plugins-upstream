## Description: <br>
Workiom lets an agent operate a connected Workiom workspace to inspect apps, lists, metadata, fields, views, filters, and records, and to create records with schema-checked payloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent query Workiom apps, lists, metadata, and records through an OOMOL-connected account. For record creation, the agent should inspect the live connector schema and confirm the exact payload and effect before running the write action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A record-creation command could change Workiom workspace data if the payload is wrong or unintended. <br>
Mitigation: Fetch the live connector schema, show the exact create_record payload and expected effect, and get user confirmation before running the write action. <br>
Risk: First-time oo CLI installation or authentication expands local and account trust. <br>
Mitigation: Treat CLI installation and OOMOL sign-in as separate trust decisions, and only perform setup after a command fails for a matching install, auth, or connection reason. <br>


## Reference(s): <br>
- [ClawHub Workiom Skill](https://clawhub.ai/oomol/skills/oo-workiom) <br>
- [Workiom Homepage](https://workiom.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON payloads, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require confirmation of the exact payload and effect.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
