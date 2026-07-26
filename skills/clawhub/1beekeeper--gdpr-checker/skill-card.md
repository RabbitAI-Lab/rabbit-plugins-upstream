## Description: <br>
GDPR compliance audit for ZK-Bankir: data minimization verification, encryption audit, right-to-delete workflows, privacy policy validation, and data export procedures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1beekeeper](https://clawhub.ai/user/1beekeeper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to audit a local ZK-Bankir Rails deployment for GDPR-relevant privacy controls, including data minimization, encryption, deletion workflows, portability exports, retention, and privacy-by-design checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes mutation checks against live financial application data. <br>
Mitigation: Run mutation checks only on a disposable copy, staging database, or inside an explicit rollback transaction. <br>
Risk: The data portability workflow can produce plaintext GDPR export files containing sensitive financial data. <br>
Mitigation: Write exports to a protected location, keep permissions restrictive, avoid committing or syncing them, and delete or encrypt them after use. <br>
Risk: Audit commands are intended for a local ZK-Bankir environment and may be inappropriate for unrelated systems. <br>
Mitigation: Review each command before execution and confirm it applies to the target ZK-Bankir checkout and Rails server. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/1beekeeper/skills/gdpr-checker) <br>
- [ZK-Bankir Project](https://gitlab.com/1Beekeeper/zk-bankir) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and Ruby-on-Rails command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target a local ZK-Bankir checkout and may write GDPR export JSON files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
