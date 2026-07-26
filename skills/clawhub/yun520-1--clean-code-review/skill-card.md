## Description: <br>
Pragmatic coding standards for writing clean, maintainable code covering naming, functions, structure, anti-patterns, and pre-edit safety checks for writing, refactoring, reviewing, or standardizing code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to guide new code, refactors, and code reviews toward clearer naming, smaller functions, simpler structure, and safer dependency-aware edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Clean-code guidance can lead an agent to remove comments, rename symbols, or restructure dependent files in ways that break callers or tests. <br>
Mitigation: Review proposed edits before applying them, check dependent files, and run relevant lint, type, and test checks. <br>
Risk: Broad installation may apply the style rules outside the intended codebase. <br>
Mitigation: Use project-level installation when the rules should only affect one repository. <br>


## Reference(s): <br>
- [Anti-Patterns Gallery](references/anti-patterns.md) <br>
- [Code Smells Catalog](references/code-smells.md) <br>
- [Refactoring Catalog](references/refactoring-catalog.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline code examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; no API keys, MCP integrations, hidden execution, or data access were identified by security evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and artifact _meta.json; artifact SKILL.md frontmatter lists 2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
