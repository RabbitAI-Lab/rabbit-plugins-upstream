## Description:

Imports programming-contest problems from OJ platforms such as AtCoder and Codeforces into standardized problem packages, or generates test data from user-provided problem statements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, educators, and contest administrators use this skill to import OJ problems, format statements, generate standard solutions and test data, audit packages, and produce zip archives for judge systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and delete desktop work folders and produce zip archives.

Mitigation: Run it in a disposable workspace or sandbox and review resolved paths before execution.

Risk: The skill can compile and run generated C++ programs to produce outputs.

Mitigation: Review generated source code and run it in a sandbox before accepting generated test data.

Risk: The skill reads user-specified local files or attachments and browses OJ pages.

Mitigation: Use intended inputs only, verify source URLs, and avoid sensitive local files.

Risk: Vague contest-related prompts can lead to broad file or browsing activity.

Mitigation: Provide exact problem URLs, files, or contest scope before invoking the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/ojimport)
- [Test data design reference](artifact/references/testdata-design.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with C++ source, YAML configuration, generated test data files, and zip archives.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create problem_zh.md, problem.yaml, std.cpp, mkin.h, testdata .in/.out files, config.yaml, and packaged zip outputs.]

## Skill Version(s):

2.7.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
