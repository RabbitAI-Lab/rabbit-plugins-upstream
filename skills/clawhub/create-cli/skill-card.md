## Description: <br>
Design command-line interface parameters and UX, including arguments, flags, subcommands, help text, output formats, error messages, exit codes, prompts, configuration precedence, and safe dry-run behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to design or refactor CLI interfaces before implementation, covering command structure, flags, output contracts, errors, safety behavior, and configuration precedence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated CLI specifications may include destructive-operation behavior, secret-handling choices, or configuration precedence that would be risky if implemented without review. <br>
Mitigation: Review any generated CLI specification before implementation, especially dry-run, force, confirmation, no-input, and secret-handling decisions. <br>
Risk: Generated output contracts can mislead users or automation when stdout, stderr, exit codes, or machine-readable modes are underspecified. <br>
Mitigation: Require explicit stdout and stderr behavior, JSON or plain-text modes, and exit-code definitions before treating a generated spec as implementation-ready. <br>


## Reference(s): <br>
- [Create CLI skill page](https://clawhub.ai/steipete/skills/create-cli) <br>
- [Command Line Interface Guidelines](https://clig.dev/) <br>
- [CLI Guidelines GitHub repository](https://github.com/cli-guidelines/cli-guidelines) <br>
- [CLI guidelines reference](references/cli-guidelines.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown CLI specification with usage synopsis, arguments and flags, output rules, exit-code map, safety rules, configuration precedence, and example invocations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Language-agnostic; may include optional shell examples and JSON or plain-text output contracts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
