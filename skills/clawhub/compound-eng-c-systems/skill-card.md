## Description:

Guides developers writing, reviewing, and debugging C systems code, libraries, and native extensions with attention to memory safety, correctness, structure, and build verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, refactor, and review C systems code and native extensions, including memory ownership, input bounds, error handling, and safety testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested C changes may introduce memory-safety or correctness defects.

Mitigation: Review changes against the repository's conventions and run relevant sanitizer-enabled tests before deployment.

Risk: Suggested build or test commands may affect the local working tree.

Mitigation: Inspect commands and the repository's build instructions before running them.

## Reference(s):

- [Implementation structure](artifact/references/implementation-structure.md)
- [Runtime safety and interfaces](artifact/references/runtime-safety.md)
- [Build and measurement](artifact/references/build-and-measurement.md)
- [C memory safety and undefined behavior](artifact/references/memory-safety.md)
- [C correctness traps](artifact/references/correctness-traps.md)
- [PHP extension C](artifact/references/php-extension-c.md)
- [Legibility standard](artifact/references/legibility-standard.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on the target repository's conventions and available build and test tools.]

## Skill Version(s):

5.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
