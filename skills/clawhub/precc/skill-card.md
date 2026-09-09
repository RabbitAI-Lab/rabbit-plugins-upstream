## Description:

Predictive Error Correction for Claude Code that corrects bash commands before execution, predicts token costs via a trained ML oracle, and captures opt-in counterfactual telemetry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yijunyu](https://clawhub.ai/user/yijunyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use PRECC with Claude Code to reduce failed Bash tool calls, estimate task token costs, compress selected context files, and configure command hooks that can improve repeated development workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation uses a pipe-to-shell flow and downloads local binaries.

Mitigation: Download and inspect the installer before execution, verify the source and checksum behavior, and install only from a trusted release channel.

Risk: The installed hook can persistently intercept Claude Code Bash tool use and modify Claude settings.

Mitigation: Review the generated ~/.claude/settings.json entries, confirm the hook commands are expected, and remove or disable them if they are not required.

Risk: Optional telemetry and local history databases may record command-related workflow data.

Mitigation: Keep counterfactual telemetry disabled unless explicitly needed, review local PRECC data paths, and avoid enabling upload or companion integrations without approval.

## Reference(s):

- [PRECC ClawHub page](https://clawhub.ai/yijunyu/skills/precc)
- [PRECC repository](https://github.com/peri-a-i/precc-cc)
- [PRECC releases](https://github.com/peri-a-i/precc-cc/releases)
- [cocoindex-code](https://github.com/cocoindex-io/cocoindex-code)
- [RTK](https://github.com/rtk-ai/rtk)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent through installing and using local PRECC binaries and Claude Code hook configuration.]

## Skill Version(s):

0.3.111 (source: server release metadata); artifact frontmatter declares 1.1.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
