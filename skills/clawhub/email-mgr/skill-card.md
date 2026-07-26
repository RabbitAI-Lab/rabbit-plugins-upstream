## Description: <br>
Read, search, compose, and manage email with a local JSON-based store and zero external dependencies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use Email Manager to inspect local inbox data, search messages, compose drafts, review threads, and check mailbox status from terminal-driven workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email content is stored in plaintext JSON, including message bodies and metadata. <br>
Mitigation: Use restrictive filesystem permissions, avoid storing sensitive mailbox data unless local storage controls are acceptable, and do not treat the skill as encrypted email storage. <br>
Risk: The documentation contains confusing claims about SMTP, sending behavior, and security guarantees. <br>
Mitigation: Review recipient, subject, and body before using send-related workflows, and confirm the implementation path before relying on it for real outbound email or credentials. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/jlacroix82/skills/email-mgr) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, configuration, guidance] <br>
**Output Format:** [Terminal text, JavaScript API usage examples, and JSON-backed local email data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads and writes local JSON files under the configured email data directory.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
