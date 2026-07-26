## Description: <br>
Source-backed company context retrieval for OpenClaw agents via the fourok CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[simonvanlaak](https://clawhub.ai/user/simonvanlaak) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve permission-filtered company, project, customer, connector, and operational context from an existing fourok backend before answering. It helps agents inspect decisive sources and cite returned refs instead of relying on unsupported claims. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports under-disclosed OpenClaw chat-message ingestion that can retain full conversation content and identifiers. <br>
Mitigation: Enable the skill only after administrators confirm whether message-capture helpers are reachable, where records are stored, who can search them, and what retention and redaction controls apply. <br>
Risk: Retrieval queries or captured messages may include sensitive operational details. <br>
Mitigation: Avoid secrets, raw environment values, database URLs, tokens, and private keys in retrieval queries, and review retrieved records as evidence rather than final answers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/simonvanlaak/skills/fourok) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and source-reference citation instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Assumes the fourok CLI and backend already exist; normal use returns source-backed retrieval results and source refs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
