## Description:

Traverses a specified local directory and reviews C/C++ source files for production readiness, code quality, and potential vulnerabilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouzy-creator](https://clawhub.ai/user/zhouzy-creator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review local C and C++ projects for memory safety, resource management, concurrency, performance, and modernization issues before production use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects and may quote from local C/C++ source files, which can expose unrelated private code if the target directory is too broad.

Mitigation: Run it only on intended project directories and avoid directories containing credentials, unrelated private code, generated dependencies, or files that should not appear in review output.

Risk: Large files or broad projects may exceed practical review context and produce incomplete findings.

Mitigation: Review large projects by module or file group, and split files over the context limit at function boundaries before asking for final production-readiness guidance.

## Reference(s):

- [Server-resolved source repository](https://github.com/zhouzy-creator/local_code_review)
- [ClawHub skill page](https://clawhub.ai/zhouzy-creator/skills/local-code-review)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown review report with issue summaries, severity categories, and code comparison examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reviews user-selected local C/C++ files; large files may require module-level or function-level chunking.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
