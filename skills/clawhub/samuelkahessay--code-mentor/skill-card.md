## Description: <br>
Code Mentor is an AI programming tutor for Python and JavaScript that supports interactive lessons, code review, debugging guidance, algorithm practice, project mentoring, and design pattern exploration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samuelkahessay](https://clawhub.ai/user/samuelkahessay) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, students, and interview candidates use Code Mentor to learn Python or JavaScript, review and debug code, practice algorithms and data structures, and plan projects with guided explanations and optional local analysis and test scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional test runner can execute local project tests and therefore may run untrusted repository code. <br>
Mitigation: Run tests only in repositories you trust or inside an isolated environment, and review the target before execution. <br>
Risk: The skill may read selected code files during tutoring, code review, debugging, and analysis workflows. <br>
Mitigation: Avoid sharing files that contain secrets, credentials, or sensitive data unless they have been sanitized. <br>
Risk: The skill can automatically retain learning history in references/user-progress/learning_log.md. <br>
Mitigation: Review or delete the learning log when session history should not be retained. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Common Algorithm Patterns](references/algorithms/common-patterns.md) <br>
- [Clean Code Principles](references/best-practices/clean-code.md) <br>
- [Arrays and Strings Reference](references/data-structures/arrays-strings.md) <br>
- [Trees and Graphs Reference](references/data-structures/trees-graphs.md) <br>
- [Creational Design Patterns](references/design-patterns/creational-patterns.md) <br>
- [JavaScript Quick Reference](references/languages/javascript-reference.md) <br>
- [Python Quick Reference](references/languages/python-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with code blocks, shell command examples, and optional JSON from utility scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional scripts can analyze code, estimate complexity, run local tests, and append session progress to references/user-progress/learning_log.md.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
