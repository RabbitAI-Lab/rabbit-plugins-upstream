## Description: <br>
Secrets Manager is a local encrypted secret store for OpenClaw agents that stores, retrieves, lists, rotates, audits, and deletes secrets using AES-256-GCM with a local master key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to keep local agent secrets encrypted at rest, retrieve them in masked form by default, and manage rotation, deletion, and audit checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Server security evidence marks the release suspicious because README, changelog, tests, manifest, and code disagree about secret-injection and temp-file behavior. <br>
Mitigation: Review before installing, do not rely on README-documented injection or cleanup commands, and use a clearly separate high-privilege injection skill when command injection is needed. <br>
Risk: The --get --raw mode and the local .master-key are sensitive credential material that can expose stored secrets if captured or mishandled. <br>
Mitigation: Prefer masked retrieval, pipe raw output only to private processes or protected files, protect and back up .master-key, and avoid exposing SECRETS_MASTER_KEY in shared or logged environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/secrets-manager) <br>


## Skill Output: <br>
**Output Type(s):** [text, files, shell commands, configuration] <br>
**Output Format:** [CLI text output and encrypted local JSON data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates local encrypted secret data and a local master-key file; raw retrieval can print plaintext to stdout.] <br>

## Skill Version(s): <br>
1.1.14 (source: server release metadata and clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
