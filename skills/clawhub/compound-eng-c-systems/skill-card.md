## Description:

C patterns for systems code, libraries, and native extensions: module layout, function decomposition, status-enum errors, memory safety, undefined behavior, and performance measurement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, refactoring, or debugging C systems code, libraries, and native extensions, especially work involving ownership, buffers, undefined behavior, sanitizer or Valgrind checks, and project-specific C conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recommended build, sanitizer, Valgrind, or lint commands may be expensive or unsuitable for large or sensitive repositories.

Mitigation: Review commands before execution and scope them to the target repository, test suite, or file set.

Risk: Generic C guidance can conflict with established project idioms such as PHP extension allocation, macros, formatting, or cleanup style.

Mitigation: Apply the skill's repo-convention gate and load the relevant reference material before changing code.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-c-systems)
- [C memory safety and undefined behavior](references/memory-safety.md)
- [C correctness traps that pass review](references/correctness-traps.md)
- [C legibility: the deep rules and a worked refactor](references/legibility-standard.md)
- [PHP extension C](references/php-extension-c.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend local build, sanitizer, Valgrind, lint, formatting, debugging, or project-convention checks for the agent to review before execution.]

## Skill Version(s):

4.5.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
