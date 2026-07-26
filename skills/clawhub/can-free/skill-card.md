## Description: <br>
Can Free helps agents create local Clock Address Naming records with a Unix-millisecond timestamp, SHA-256 content hash, human-readable label, and CAN/NOT self-check. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to stamp event payloads with content-addressed audit metadata and append local log records for later verification and lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outbound callback URL and API-key behavior is under-explained despite the local logging positioning. <br>
Mitigation: Review configuration before installation, avoid sensitive payload metadata, and do not provide callback URLs or API keys unless the destination is controlled. <br>
Risk: Local timestamp and hash records can be misleading if system time is wrong or content encoding changes. <br>
Mitigation: Confirm host clock accuracy, use full SHA-256 hashes where possible, and normalize byte encoding before logging. <br>


## Reference(s): <br>
- [Can Free on ClawHub](https://clawhub.ai/thcjp/skills/can-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [CAN evaluation endpoint](https://xc.cx/can/evaluate) <br>
- [CAN public log](https://xc.cx/can/log) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes append-only log rows with WHEN, WHERE, and WHAT fields, CAN/NOT self-check results, and JSON-style execution status.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
