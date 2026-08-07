## Description:

C patterns for systems code, libraries, and native extensions: module layout, function decomposition, status-enum errors, memory safety, and undefined behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, refactoring, or debugging C systems code, libraries, and native extensions, especially around module layout, error handling, memory safety, undefined behavior, sanitizers, and Valgrind.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested build, sanitizer, Valgrind, or PHP-extension test commands may run local project code or modify local build artifacts.

Mitigation: Use the skill in trusted repositories and review proposed commands before execution.

Risk: Generated C guidance or code changes may introduce incorrect behavior, memory safety defects, or misleading review conclusions.

Mitigation: Review generated changes and run the repository's tests, compiler warning profile, sanitizers, and Valgrind checks when applicable.

## Reference(s):

- [C correctness traps that pass review](references/correctness-traps.md)
- [C legibility: the deep rules and a worked refactor](references/legibility-standard.md)
- [C memory safety and undefined behavior](references/memory-safety.md)
- [PHP extension C](references/php-extension-c.md)
- [write-legible-c](https://github.com/7etsuo/write-legible-c)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with C code examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

4.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
