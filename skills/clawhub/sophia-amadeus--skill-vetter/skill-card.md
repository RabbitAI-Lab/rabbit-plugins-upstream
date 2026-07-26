## Description: <br>
Audits AI skills for security risks before installation by checking credentials, permissions, network use, destructive operations, and ClawHub vetting status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sophia-amadeus](https://clawhub.ai/user/sophia-amadeus) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use Skill Vetter to pre-screen ClawHub, GitHub, or third-party skills before installation. It helps identify credential leaks, broad permissions, network access, destructive operations, and other patterns that call for manual review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill's score and Install verdict can be overconfident if treated as proof that another skill is safe. <br>
Mitigation: Use the result as an initial screen and manually review high-impact permissions, network destinations, credential handling, hooks, and install scripts before installing third-party skills. <br>
Risk: The shell helper depends on current ClawHub inspection output and local CLI availability. <br>
Mitigation: Confirm the inspected files directly when a result affects installation or production use. <br>


## Reference(s): <br>
- [Credential Patterns](artifact/references/credential-patterns.md) <br>
- [Safe Coding Patterns](artifact/references/safe-patterns.md) <br>
- [Flagged Skills](artifact/references/flagged-skills.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance and terminal-style security vetting output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses score and verdict labels such as Install, Caution, Reject, and Dangerous.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
