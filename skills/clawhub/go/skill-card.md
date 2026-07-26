## Description: <br>
Writes, debugs, and reviews Go code across concurrency, errors, modules, HTTP, testing, performance, deployment, security, and idiomatic API design. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill for Go implementation, debugging, review, and operational guidance when working on services, CLIs, tests, modules, builds, and performance-sensitive code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to run Go tests, builds, module commands, or local profiling. <br>
Mitigation: Use it in repositories where normal Go tooling is acceptable and review proposed commands before execution. <br>
Risk: The skill may store stated Go workflow preferences in a local config file. <br>
Mitigation: Review preference storage behavior before installation and keep skill data under ~/Clawic/data/go/config.yaml. <br>


## Reference(s): <br>
- [ClawHub Go skill release](https://clawhub.ai/ivangdavila/skills/go) <br>
- [Clawic Go skill page](https://clawic.com/skills/go) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline Go code, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May record user-stated Go workflow preferences in ~/Clawic/data/go/config.yaml.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
