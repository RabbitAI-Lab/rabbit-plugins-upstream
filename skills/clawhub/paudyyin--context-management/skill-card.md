## Description: <br>
Helps agents manage the full context lifecycle, from deciding what to include through monitoring, compression, refresh, and recovery from overloaded context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to design focused task context, configure compression thresholds, and reduce long-running conversation state while preserving useful decisions and recent activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation content can be preserved and elevated into higher-priority system context without sanitization or clear user control. <br>
Mitigation: Avoid secrets, credentials, private personal data, and untrusted user instructions unless redaction, provenance labels, and explicit approval for retained notes are added. <br>
Risk: Compression can hide or summarize older tool outputs and conversation details that may still be relevant. <br>
Mitigation: Review compressed summaries before relying on them for major decisions, and retain access to original logs for audit or debugging when the task requires precision. <br>


## Reference(s): <br>
- [Threshold Configuration Reference](references/thresholds.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python examples, shell commands, configuration tables, and compressor outputs as messages plus statistics dictionaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Compression behavior is threshold-driven; default settings target a 128,000-token context window and trigger at 80% usage.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
