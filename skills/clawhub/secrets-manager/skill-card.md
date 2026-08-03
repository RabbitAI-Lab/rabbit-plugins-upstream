## Description: <br>
Encrypted local secret store for OpenClaw agents with AES-256-GCM storage, masked retrieval, rotation and audit commands, and opt-in plaintext output or command injection modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to store, retrieve, rotate, audit, and inject local secrets for OpenClaw workflows without relying on external dependencies. It is suited for single-user local secret convenience, not production-grade shared credential management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review identifies a high-risk feature that writes plaintext secrets into runnable temporary shell scripts. <br>
Mitigation: Avoid --inject for sensitive credentials unless this exposure is acceptable, run --cleanup-tmp immediately after use, and prefer a managed secret store for high-value or shared credentials. <br>
Risk: This is a local, single-user convenience vault rather than production-grade secret management. <br>
Mitigation: Use an OS keychain, HashiCorp Vault, AWS Secrets Manager, or another managed secret store for production, shared, or high-value secrets. <br>
Risk: Raw retrieval and stdout injection can expose plaintext credentials to logs, transcripts, shell history, or downstream tools. <br>
Mitigation: Use masked retrieval by default and reserve --get --raw or --inject-stdout --confirm-expose for tightly controlled private processes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/secrets-manager) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Changelog](artifact/CHANGELOG.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Files, Shell commands, Configuration] <br>
**Output Format:** [CLI text output, encrypted JSON data files, and chmod 0600 shell scripts for injected commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Secret values are masked by default; plaintext output and command exposure require explicit flags.] <br>

## Skill Version(s): <br>
1.1.13 (source: server release metadata and clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
