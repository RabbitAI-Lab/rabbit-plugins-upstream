## Description:

Imports competitive-programming problems from OJ platforms such as AtCoder and Codeforces into standardized problem packages, and can also generate test data from user-provided problem statements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, contest maintainers, and competitive-programming educators use this skill to convert online judge problems or supplied statements into normalized packages with statements, C++ solutions, test data, configuration, and archives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cleanup steps may delete or alter unintended desktop work folders.

Mitigation: Use a disposable workspace and confirm the resolved base and work paths before cleanup, rename, compile, run, or zip operations.

Risk: Generated C++ source may be compiled and executed during test data creation.

Mitigation: Inspect generated C++ before execution and run compilation and test generation inside a sandbox or container.

Risk: Imported problem content may be incorrect or unsafe when taken from untrusted sources.

Mitigation: Use trusted problem sources and review the final statement, configuration, tests, and archive before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/ojimport)
- [Testdata design reference](artifact/references/testdata-design.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create C++ source files, YAML configuration, test data, and zip archives in a workspace.]

## Skill Version(s):

3.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
