## Description: <br>
Helps developers build, debug, preview, test, and publish WeChat Mini Program projects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill for WeChat Mini Program coding support, build and debug workflows, preview, testing, and publishing assistance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide file changes and command execution for build, test, preview, and publish workflows. <br>
Mitigation: Review proposed commands and file changes before execution, and require explicit user confirmation for deployment or release actions. <br>
Risk: Mini Program development workflows may involve API keys or publishing credentials. <br>
Mitigation: Keep credentials in protected environment variables or secret stores, avoid hardcoding them, and redact them from logs and shared output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/miniprogram-development) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code, shell commands, configuration notes, and structured status or report snippets when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file changes, commands, tests, previews, and publish steps for user review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
