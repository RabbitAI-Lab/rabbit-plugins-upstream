## Description:

Provides C systems-code guidance for module layout, function decomposition, status-enum errors, memory safety, undefined behavior, performance measurement, and native extension work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill when writing, reviewing, refactoring, or debugging C systems code, libraries, and native extensions. It is especially relevant for memory-safety, undefined-behavior, error-handling, build, sanitizer, Valgrind, and PHP extension work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may suggest local build, test, sanitizer, or Valgrind commands for C projects.

Mitigation: Review commands before running them and execute them only in the intended project and test environment.

Risk: C refactoring or memory-safety guidance can change behavior, ABI, or project-specific conventions if applied without local context.

Mitigation: Inspect local headers and adjacent C files, preserve established interfaces unless explicitly changing them, and verify with the repository's tests and sanitizer profile.

## Reference(s):

- [C memory safety and undefined behavior](references/memory-safety.md)
- [C correctness traps that pass review](references/correctness-traps.md)
- [C legibility: the deep rules and a worked refactor](references/legibility-standard.md)
- [PHP extension C](references/php-extension-c.md)
- [write-legible-c](https://github.com/7etsuo/write-legible-c)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-dependent C implementation, review, refactoring, debugging, build, and verification guidance.]

## Skill Version(s):

4.5.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
