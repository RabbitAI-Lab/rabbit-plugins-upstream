## Description:

从 OJ 平台搬运题目（含AtCoder/Codeforces等），生成标准化题目文件包；也可根据用户提供的题目仅生成测试数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and contest maintainers use this skill to import OJ programming problems, translate and normalize problem statements, generate standard solutions, create 25-case test data sets, and package HydroOJ-compatible problem archives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create Desktop work folders and delete prior work_* or testdata outputs during setup and cleanup.

Mitigation: Run it in a disposable workspace or sandbox, confirm target paths before cleanup or packaging, and keep backups of any existing contest work.

Risk: The skill compiles and runs generated C++ locally to produce expected outputs.

Mitigation: Review std.cpp, mkin.h, and mkdata.cpp before execution, and compile/run them only in an isolated environment you are comfortable using.

Risk: Generated problem statements, scoring metadata, and test data can be wrong if the source problem is parsed incorrectly.

Mitigation: Verify imported statements, samples, problem.yaml, testdata/config.yaml, and the generated .in/.out pairs before publishing or uploading a package.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/ojimport)
- [Test Data Design Reference](references/testdata-design.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown problem statements, C++ source files, YAML configuration, generated .in/.out test data, and ZIP archives]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces standardized OJ problem packages and testdata.zip files after local generation, verification, and packaging steps.]

## Skill Version(s):

2.6.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
