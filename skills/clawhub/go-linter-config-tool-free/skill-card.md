## Description: <br>
Helps individual Go developers create minimal or standard golangci-lint configurations, run local lint checks, and troubleshoot common CI import or type-checking failures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Go developers use this skill to bootstrap golangci-lint in a personal Go project, choose between minimal and standard lint configurations, and resolve basic local or CI lint failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to write golangci-lint configuration files and run local lint-related commands. <br>
Mitigation: Review proposed .golangci.yml changes and command invocations before applying them in a repository. <br>
Risk: The trigger wording is broader than ideal and may be invoked for coding, deployment, or troubleshooting outside lint setup. <br>
Mitigation: Use the skill only for Go lint configuration, local lint execution, and basic CI lint troubleshooting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/go-linter-config-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with YAML, JSON, text, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose edits to .golangci.yml and local golangci-lint commands for review before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
