## Description: <br>
Datalust Seq helps agents operate a user's Datalust Seq account through OOMOL's datalust connector, including querying events, managing saved queries and signals, and ingesting structured logs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect and manage Datalust Seq data through an OOMOL-connected account. It supports event search and lookup, SQL-style query execution, saved query and signal management, and structured log ingestion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, ingest, or delete Datalust Seq resources. <br>
Mitigation: Confirm the exact payload and expected effect with the user before any write action, and require explicit approval before destructive actions. <br>
Risk: The connected Datalust Seq API key may expose more account capability than the current task requires. <br>
Mitigation: Use an API key with only the Seq permissions needed for the intended workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-datalust) <br>
- [Datalust Seq Homepage](https://datalust.co/seq) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent responses may include connector schemas, structured JSON results, command invocations, and proposed payloads for user approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
