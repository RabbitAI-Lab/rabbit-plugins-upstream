## Description: <br>
Security toolkit for AI workflows that scans code and repositories, audits third-party agent extensions, classifies shell command risk, and supports secure design review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rafter](https://clawhub.ai/user/rafter) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to run Rafter CLI scans, classify shell commands, audit skills, MCPs, and agent configs, and ask secure design questions during AI-assisted development. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary reports that command-validation instructions could cause real commands to run when users may expect only a safety check. <br>
Mitigation: Use non-executing dry-run command checks for review and classification, and separately approve destructive or privileged commands before routing them through /rafter-bash. <br>
Risk: API-backed Rafter scans can send code to Rafter services when RAFTER_API_KEY-enabled features are used. <br>
Mitigation: Use offline rafter secrets scans when code should remain local, and enable API-backed scanning only when sharing code with Rafter is acceptable. <br>
Risk: Rafter initialization can add agent command-validation hooks that affect shell command handling. <br>
Mitigation: Initialize only the intended integrations with opt-in --with-* flags, review Rafter configuration after setup, and inspect audit logs for command interception events. <br>


## Reference(s): <br>
- [Rafter Homepage](https://rafter.so) <br>
- [ClawHub Skill Page](https://clawhub.ai/rafter/skills/rafter-security) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call the local Rafter CLI; API-backed scans require the optional RAFTER_API_KEY environment variable.] <br>

## Skill Version(s): <br>
0.10.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
