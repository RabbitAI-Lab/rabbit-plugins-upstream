## Description: <br>
Secrets Manager is an encrypted local secret store for OpenClaw agents that uses AES-256-GCM authenticated encryption, per-secret random IVs, a chmod 0600 master-key file, rotation and audit commands, and opt-in plaintext output controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to store, retrieve, rotate, audit, and inject local secrets for OpenClaw workflows without external dependencies. It is intended for local file-based secret management, not as a replacement for a production vault or OS keychain. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Default --inject can leave a plaintext resolved command in /tmp/secrets-inject-*.sh even though documentation and output imply automatic cleanup. <br>
Mitigation: Avoid default --inject for important credentials, or remove the generated /tmp/secrets-inject-*.sh file immediately after use. <br>
Risk: The skill is a local file-based secrets store with master-key material stored in .master-key. <br>
Mitigation: Protect and back up .master-key, restrict access to the secrets directory, and use a real vault or OS keychain for production credentials. <br>
Risk: Raw retrieval and explicit inject-to-stdout modes can expose plaintext secrets to logs, terminal history, CI output, or agent transcripts. <br>
Mitigation: Use masked output by default and reserve --get --raw or --inject-stdout --confirm-expose for tightly controlled private processes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/secrets-manager) <br>
- [Publisher profile](https://clawhub.ai/user/jlacroix82) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text output, chmod-0600 shell script files for command injection, and JavaScript module return values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores encrypted secret records and master-key material as local files; raw secret output and resolved injected commands can expose plaintext when explicitly requested.] <br>

## Skill Version(s): <br>
1.1.9 (source: server release metadata and artifact clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
