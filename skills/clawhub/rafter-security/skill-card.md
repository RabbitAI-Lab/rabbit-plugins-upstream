## Description: <br>
Security toolkit for AI workflows that supports scanning code or repositories for vulnerabilities, auditing third-party skills, MCPs, and agent configurations before installation, evaluating shell commands before running them, and generating secure design questions for new features. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rafter](https://clawhub.ai/user/rafter) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agent users use this skill to run Rafter security checks, scan for secrets, review third-party skills or agent configurations, and evaluate risky shell commands before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The command-validation workflow may be unclear about whether `rafter agent exec <command>` classifies a command or executes it. <br>
Mitigation: Confirm the Rafter CLI behavior before use and prefer a documented dry-run mode when the intent is only risk assessment. <br>
Risk: Initialization can add agent integrations or hooks through the Rafter CLI. <br>
Mitigation: Install only after deciding which integrations are trusted, and use the documented opt-in `--with-*` flags for targeted setup. <br>


## Reference(s): <br>
- [Rafter homepage](https://rafter.so) <br>
- [ClawHub skill page](https://clawhub.ai/rafter/skills/rafter-security) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON scan output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Secret scan JSON output redacts raw secret values when requested.] <br>

## Skill Version(s): <br>
0.9.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
