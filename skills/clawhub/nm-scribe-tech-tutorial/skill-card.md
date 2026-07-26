## Description: <br>
Plans, drafts, and refines technical tutorials for developers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical writers use this skill to plan, draft, and verify hands-on tutorials for libraries, CLI tools, APIs, and developer workflows. It emphasizes scoped outcomes, tested code examples, progressive complexity, expected outputs, troubleshooting, and quality checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated tutorials may include code or shell commands that are unsuitable for the user's environment. <br>
Mitigation: Review generated commands and test runnable examples in an environment where execution is acceptable before publishing or sharing the tutorial. <br>
Risk: The skill can activate on broad documentation requests even when a hands-on tutorial is not the right format. <br>
Mitigation: Confirm the intended output is a step-by-step technical tutorial before applying the workflow. <br>
Risk: The artifact expects a companion slop-detector review for its quality gate. <br>
Mitigation: Run the referenced companion review when available, or apply an equivalent prose-quality review before final approval. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-tech-tutorial) <br>
- [Project homepage from skill metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>
- [Tutorial outline and structure module](artifact/modules/outline-structure.md) <br>
- [Code examples module](artifact/modules/code-examples.md) <br>
- [Progressive complexity module](artifact/modules/progressive-complexity.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown with fenced code blocks, expected output blocks, checklists, and troubleshooting sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tutorial outlines, tested code snippets, TODO items, quality gates, and review guidance.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
