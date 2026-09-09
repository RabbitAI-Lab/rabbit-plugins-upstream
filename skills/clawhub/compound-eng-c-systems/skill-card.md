## Description:

C patterns for systems code, libraries, and native extensions: module layout, function decomposition, status-enum errors, memory safety, undefined behavior, and performance measurement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, refactoring, or debugging C systems code, libraries, and native extensions. It focuses the agent on repository conventions, memory safety, undefined behavior, build hygiene, and C-specific verification practices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to propose or run local compiler, test, sanitizer, Valgrind, or similar developer-tool commands during C tasks.

Mitigation: Review proposed commands, target paths, and tool effects before execution, and run them only in the intended local workspace.

## Reference(s):

- [Build and measurement](references/build-and-measurement.md)
- [C correctness traps that pass review](references/correctness-traps.md)
- [Implementation structure](references/implementation-structure.md)
- [C legibility: the deep rules and a worked refactor](references/legibility-standard.md)
- [C memory safety and undefined behavior](references/memory-safety.md)
- [PHP extension C](references/php-extension-c.md)
- [Runtime safety and interfaces](references/runtime-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local compiler, test, sanitizer, Valgrind, or related developer-tool commands during C tasks.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
