## Description: <br>
Magneto Skill Master guides agents through safely locating, auditing, adapting, installing, and validating external WorkBuddy agent skills from GitHub, Gitee, or similar repositories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yehuzi2026](https://clawhub.ai/user/yehuzi2026) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and WorkBuddy users use this skill to install external agent skills while preserving an explicit review trail for repository source, security audit results, WorkBuddy format adaptation, dependency handling, and final validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can download and install third-party code into a local WorkBuddy skills directory. <br>
Mitigation: Require explicit user confirmation for the target repository and run the documented P0/P1/P2 audit before installation. <br>
Risk: Installing a skill can replace an existing ~/.workbuddy/skills/<name>/ directory. <br>
Mitigation: Back up any existing skill directory and confirm replacement before copying files. <br>
Risk: Dependency installation or validation commands can change the local environment, especially if sandboxing is disabled. <br>
Mitigation: Use the managed WorkBuddy virtual environment, avoid global package installation, and obtain explicit confirmation before disabling sandboxing or running validation commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yehuzi2026/skills/magneto-skill-master) <br>
- [README](README.md) <br>
- [Audit patterns](references/audit_patterns.md) <br>
- [Managed Python wrapper template](references/run_script_template.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes audit conclusions, installation status, dependency guidance, validation steps, and confirmation prompts for risky actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, target metadata, manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
