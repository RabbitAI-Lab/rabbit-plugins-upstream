## Description: <br>
Writes, debugs, and reviews Python code across runtime errors, packaging, typing, async, testing, performance, subprocesses, logging, and version upgrades. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill for Python implementation, debugging, review, packaging, testing, typing, performance, CLI, subprocess, security, and upgrade guidance. It is intended for general Python work and excludes library-specific frameworks that have dedicated skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Python commands or package operations could change a project, install dependencies, publish artifacts, or delete files if accepted without review. <br>
Mitigation: Review proposed commands before execution, especially package installs, publishing, file deletion, and other project-changing actions. <br>
Risk: The skill may store stated Python preferences on the user's machine. <br>
Mitigation: Keep preference storage limited to the disclosed ~/Clawic/data/py/config.yaml path and avoid storing unrelated data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/py) <br>
- [Clawic Python skill homepage](https://clawic.com/skills/py) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May store stated Python preferences in ~/Clawic/data/py/config.yaml; requires python3 and supports linux, darwin, and win32.] <br>

## Skill Version(s): <br>
1.0.4 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
