## Description: <br>
Analyze codebase architecture and generate visual HTML reports. Use when reviewing architecture, assessing technical debt, diagnosing project health, or planning refactoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to review a project architecture, assess technical debt, and produce a shareable HTML report with diagrams, findings, and prioritized recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated architecture reports may summarize private code structure, dependencies, and technical debt. <br>
Mitigation: Run the skill only on repositories intended for review, provide an explicit project path or scope, and review the HTML report before sharing it. <br>
Risk: Architecture findings and refactoring recommendations may be incomplete or misleading if the scanned scope is too narrow. <br>
Mitigation: Review findings against the source code and expand the scan scope when important modules, tests, or configuration are omitted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/architecture-review) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with Mermaid diagrams and generated HTML report instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a local architecture review HTML report in the workspace when used as directed.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
