## Description: <br>
Edit Calibre metadata through verified dry-run and apply gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextaltair](https://clawhub.ai/user/nextaltair) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators maintaining Calibre libraries use this skill to apply confirmed book metadata updates and batch tags through lookup, dry-run, explicit apply, and verification gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change remote Calibre metadata and can probe alternate network hosts with Calibre credentials. <br>
Mitigation: Review dry-run output before apply, use a dedicated Calibre-only environment or configuration, and pass an explicit --with-library target when possible. <br>
Risk: Credential handling may be riskier if plaintext passwords or broad local credential sources are used. <br>
Mitigation: Prefer CALIBRE_PASSWORD through --password-env and avoid storing plaintext passwords. <br>
Risk: Heavy analysis or subagent flows may expose private book content to external processing. <br>
Mitigation: Do not use the heavy analysis or subagent flow for private books unless full-text processing is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/calibre-metadata-apply) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSONL input plans, and JSON execution summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node, calibredb, and CALIBRE_PASSWORD; pdffonts and CALIBRE_USERNAME are optional.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
