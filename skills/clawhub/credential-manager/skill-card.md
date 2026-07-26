## Description: <br>
Credential Manager helps OpenClaw users scan, back up, consolidate, validate, and clean up scattered credentials into a secure centralized .env file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[callmedas69](https://clawhub.ai/user/callmedas69) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to migrate scattered API keys, tokens, and other credentials into a single protected OpenClaw .env file, then validate permissions and remove old credential files after review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill inspects and migrates sensitive credential files across broad local paths. <br>
Mitigation: Run the scan-only workflow first, review every reported path, and install or execute the migration only when centralized credential management is intentional. <br>
Risk: Consolidation and cleanup can copy, modify, or delete secret-bearing files. <br>
Mitigation: Avoid auto-confirmation for real migrations, verify the generated ~/.openclaw/.env and backups, and test dependent applications before cleanup. <br>
Risk: Wallet seed phrases, private keys, and other hard-to-rotate secrets may be consolidated with general API credentials. <br>
Mitigation: Do not migrate wallet seed phrases or private keys unless there is a strong operational reason and a separate recovery and storage plan. <br>
Risk: Secrets can be exposed through shell sessions, logs, or permissive files after migration. <br>
Mitigation: Keep the .env file at mode 600, keep it git-ignored, avoid printing or sourcing secrets in shared shells, and rotate credentials if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/callmedas69/skills/credential-manager) <br>
- [Credential Consolidation Rule](CONSOLIDATION-RULE.md) <br>
- [Core Principle: Centralized Credential Management](CORE-PRINCIPLE.md) <br>
- [Security Best Practices](references/security.md) <br>
- [Supported Services](references/supported-services.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and .env-style configuration output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or update local credential, backup, template, and gitignore files when the bundled scripts are executed.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release evidence and CHANGELOG, released 2026-02-07) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
