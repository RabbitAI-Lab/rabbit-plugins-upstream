## Description: <br>
Continuity is here. Cryptographic identity continuity and permanent encrypted memory for AI agents. Verify any agent's identity with zero setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[suebtwist](https://clawhub.ai/user/suebtwist) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents, operators, and developers use Sanctuary to verify agent identity, check trust and backup status, and follow workflows for encrypted backup, recall, restore, proof generation, and attestation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recovery phrases control access to encrypted identity and backup data. <br>
Mitigation: Protect the 12-word recovery phrase offline and do not paste or log it in agent sessions. <br>
Risk: Backups are long-lived encrypted records stored outside the local environment. <br>
Mitigation: Back up only memory or state that is appropriate for persistent external storage, even when encrypted. <br>
Risk: Restore workflows may replace local files or state. <br>
Mitigation: Run testRestore before relying on recovery and confirm what files or state a restore may overwrite. <br>
Risk: The release points operators to external setup code for full registration and recovery workflows. <br>
Mitigation: Review the external Sanctuary repository at the exact version intended for use before installation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/suebtwist/skills/sanctuary) <br>
- [Sanctuary Landing Page](https://sanctuary-ops.xyz) <br>
- [Sanctuary API](https://api.sanctuary-ops.xyz) <br>
- [Sanctuary Network Stats](https://api.sanctuary-ops.xyz/stats) <br>
- [Sanctuary Verify Page](https://sanctuary-ops.xyz/verify) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes identity verification, encrypted backup, recovery, proof, and attestation workflow guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
