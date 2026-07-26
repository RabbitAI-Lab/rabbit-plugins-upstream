## Description: <br>
Writes, debugs, and hardens Bash shell scripts for quoting, arrays, strict mode, traps, argument parsing, and macOS/Linux portability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to write, review, debug, harden, and port Bash scripts for CI steps, deploy scripts, cron tasks, container entrypoints, API calls, and other shell automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can influence scripts that delete files, call APIs, use sudo, or run unattended jobs. <br>
Mitigation: Review generated shell changes before execution, prefer dry-runs for destructive operations, validate inputs, and require explicit confirmation for high-impact actions. <br>
Risk: User preferences stored under ~/Clawic/data/bash/config.yaml can affect future Bash guidance. <br>
Mitigation: Review or reset local preferences before shared, regulated, or high-assurance use. <br>


## Reference(s): <br>
- [ClawHub Bash skill page](https://clawhub.ai/ivangdavila/skills/bash) <br>
- [Clawic Bash skill homepage](https://clawic.com/skills/bash) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Bash code blocks, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local user preferences stored under ~/Clawic/data/bash/config.yaml; no other local state is disclosed.] <br>

## Skill Version(s): <br>
1.0.6 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
