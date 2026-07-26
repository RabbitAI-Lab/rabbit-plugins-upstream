## Description: <br>
Code Audit Pro reviews code for security, performance, logic, style, dependency, and AI-generated-code issues, with full, PR, security, and quick review modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g1776933879](https://clawhub.ai/user/g1776933879) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect source code, pull request changes, and snippets for security, correctness, performance, dependency, style, and AI-generated-code risks before merging or shipping changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local code files or git diffs selected for review. <br>
Mitigation: Run it only on code you are permitted to inspect, and avoid providing secrets unless they are necessary for the review. <br>
Risk: Review findings are heuristic and may be incomplete or include false positives. <br>
Mitigation: Treat results as lightweight review assistance, then validate important findings manually and with standard project security and quality checks. <br>
Risk: The install script adds Python lint and security tools to the local environment. <br>
Mitigation: Review the install script and install dependencies in a controlled environment before running it on sensitive systems. <br>


## Reference(s): <br>
- [Code Audit Pro on ClawHub](https://clawhub.ai/g1776933879/skills/code-audit-pro) <br>
- [g1776933879 ClawHub Profile](https://clawhub.ai/user/g1776933879) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown review reports and command-line scan output with issue severity, location, explanation, and suggested fixes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read user-selected source files, directories, or git diffs; findings are heuristic and require human review.] <br>

## Skill Version(s): <br>
2.2.2 (source: ClawHub release evidence and OpenClaw frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
