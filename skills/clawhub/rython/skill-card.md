## Description:

Compile Python to native Rust with the rython toolchain (rythonc/rypip): single files, packages, no_std embedded targets, PyO3 bindings, userspace drivers, and Linux kernel modules - output verified byte-identical to CPython.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rexlunae](https://clawhub.ai/user/rexlunae)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to convert Python source into native Rust artifacts with the rython toolchain, including single files, packages, no_std targets, PyO3 bindings, userspace drivers, and Linux kernel modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kernel-module and driver workflows can affect privileged system behavior when loaded or installed.

Mitigation: Treat kernel-module and driver commands as privileged operations, review generated artifacts, and load or install them only in environments intended for that work.

Risk: Generated Rust artifacts may be incorrect or unsuitable if the Python source crosses unsupported rython compatibility boundaries.

Mitigation: Refactor the Python source, regenerate artifacts, and compare compiled output against CPython before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rexlunae/skills/rython)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on editing Python source as the source of truth, regenerating Rust artifacts, and verifying compiled output against CPython.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
