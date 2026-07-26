## Description: <br>
Sign and verify agent skill folders with ed25519 keys, detect tampering, manage trusted authors, and track provenance chains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[felmonon](https://clawhub.ai/user/felmonon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to generate signing keys, sign skill folders, verify file integrity, inspect signature metadata, manage local trusted keys, and review signing chains before running or publishing skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trusted-author labels can be misleading if editable metadata is treated as identity proof. <br>
Mitigation: Verify public keys independently before trusting them and do not rely on TRUSTED labels, inspect output, or provenance chains as sole proof of author identity. <br>
Risk: Private signing keys stored under ~/.skillsign can sign future artifacts if exposed. <br>
Mitigation: Protect private key files, keep their permissions restricted, and revoke or remove keys from trust stores if compromise is suspected. <br>
Risk: Verification confirms file integrity against the signature but does not prove the signed code is safe to execute. <br>
Mitigation: Review and scan skills before deployment, especially before running code from untrusted publishers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/felmonon/skills/skillsign) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/felmonon) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and CLI text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may create local key, trust, revocation, and .skillsig metadata files.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata; artifact frontmatter and setup.py report 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
