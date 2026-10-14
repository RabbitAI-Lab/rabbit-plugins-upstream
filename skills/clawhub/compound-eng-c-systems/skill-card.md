## Description:

Provides C systems-programming guidance for structuring, reviewing, debugging, and verifying libraries and native extensions, with an emphasis on memory safety and correctness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill when writing, reviewing, refactoring, or debugging C systems code and native extensions, including memory ownership, undefined behavior, build checks, and performance measurement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested C changes may not fit a project's established conventions or safety requirements.

Mitigation: Review recommendations against repository conventions, then test the actual rebuilt code with appropriate warnings and safety checks.

Risk: Suggested verification commands may not suit the project's build environment.

Mitigation: Review commands before execution and adapt them to the repository's toolchain and test setup.

## Reference(s):

- [Implementation structure](references/implementation-structure.md)
- [Runtime safety](references/runtime-safety.md)
- [Build and measurement](references/build-and-measurement.md)
- [Memory safety and undefined behavior](references/memory-safety.md)
- [C correctness traps](references/correctness-traps.md)
- [PHP extension C](references/php-extension-c.md)
- [C legibility](references/legibility-standard.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with C snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on the target repository's conventions and build environment.]

## Skill Version(s):

5.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
