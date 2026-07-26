## Description: <br>
为个人 Go 项目提供最小和标准两套 golangci-lint 配置模板，支持本地运行和基础 CI 错误排查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual Go project maintainers use this skill to bootstrap golangci-lint configuration, run local lint checks, and troubleshoot common import, type-checking, and basic CI failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated golangci-lint configuration may change local lint results or CI behavior. <br>
Mitigation: Review proposed .golangci.yml changes and run lint in the intended Go project before committing or deploying them. <br>
Risk: The skill may suggest or run local Go and golangci-lint commands in a workspace. <br>
Mitigation: Use it only in Go project workspaces where those command effects are expected, and review command intent before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/go-linter-config-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with YAML configuration and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces proposed .golangci.yml content and troubleshooting steps for review before use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
