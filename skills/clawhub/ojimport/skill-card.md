## Description: <br>
Imports programming contest problems from online judges such as AtCoder and Codeforces, generates standardized problem packages, and can create test data from user-provided problem statements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fslong520](https://clawhub.ai/user/fslong520) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Competitive programming educators, contest maintainers, and developers use this skill to import OJ problems, translate or normalize problem statements, generate standard solutions, design test data, audit package completeness, and produce distributable problem archives. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, rename, delete, compile, and execute files in a Desktop work directory. <br>
Mitigation: Use it in a disposable or sandboxed workspace and review planned file operations before execution. <br>
Risk: Generated C++ solution and test-data files may be incorrect or unsafe to compile and run without review. <br>
Mitigation: Review generated std.cpp and mkin.h before compiling or executing them, and avoid invoking the skill on untrusted local problem packages. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fslong520/skills/ojimport) <br>
- [Test Data Design Reference](artifact/references/testdata-design.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with generated files, C++ code, YAML configuration, shell commands, and ZIP package paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces problem statements, std.cpp, mkin.h, testdata/config.yaml, .in/.out test files, and packaged ZIP archives when executed by an agent.] <br>

## Skill Version(s): <br>
2.5.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
