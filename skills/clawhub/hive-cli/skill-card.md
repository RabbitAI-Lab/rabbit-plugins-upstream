## Description: <br>
Operate Hive's folder-based coding-agent workflows from OpenClaw: guided CLI setup, reviewed workflow packages, task pipelines, patrols, web/TUI status, and consent-gated administration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivankuznetsov](https://clawhub.ai/user/ivankuznetsov) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to install, inspect, and operate Hive CLI workflows for repository task pipelines, reviewed workflow packages, status monitoring, patrols, and daemon-backed automation. The skill emphasizes read-only inspection first and consent before installation, project enrollment, workflow mutation, patrol starts, daemon repair, or other persistent host changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hive setup, project enrollment, workflow installation, daemon repair, patrols, and persistent admin commands can change local state or consume provider subscription capacity. <br>
Mitigation: Review dry-run or diagnostic output first, restate the exact effect, and obtain explicit approval before running mutating commands or autonomous patrols. <br>
Risk: Permission growth or high-risk workflow updates can expand what reviewed workflow actors may do. <br>
Mitigation: Treat permission growth separately from ordinary install or update consent and request separate approval before allowing escalation. <br>
Risk: Running installer or package-manager commands without review can install the wrong Hive binary or suppress normal transaction safeguards. <br>
Mitigation: Show the selected install command, keep package-manager confirmations intact, and verify the installed CLI with a strict version check before setup. <br>


## Reference(s): <br>
- [Hive CLI ClawHub page](https://clawhub.ai/ivankuznetsov/skills/hive-cli) <br>
- [Hive homepage](https://github.com/ivankuznetsov/hive) <br>
- [Homebrew formula ivankuznetsov/hive/hive](https://github.com/ivankuznetsov/hive) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown, text] <br>
**Output Format:** [Markdown guidance with shell commands and JSON-oriented CLI summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prefers read-only JSON inspection and summarizes status, setup, workflow, daemon, patrol, and recovery results.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
