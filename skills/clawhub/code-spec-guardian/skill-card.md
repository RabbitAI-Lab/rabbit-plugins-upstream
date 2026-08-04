## Description: <br>
Code Spec Guardian helps agents analyze project conventions across common frontend and backend stacks, store them as modular `.code-spec/` guidance, and apply them during code generation, bug fixes, refactors, reviews, and SQL/API work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gmmg55](https://clawhub.ai/user/gmmg55) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to extract code style, UI, architecture, API, SQL, Git, and language-specific conventions from a project, then have an agent apply those conventions when writing, modifying, reviewing, or refactoring code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist future assistant behavior by adding a `code-spec-guardian` rule to `AGENTS.md` after initial analysis. <br>
Mitigation: Require an explicit diff and approval before any `AGENTS.md` change is applied. <br>
Risk: Generated `.code-spec/` guidance can influence later code generation and reviews. <br>
Mitigation: Review generated spec files before committing them or treating them as project authority. <br>
Risk: Project analysis may read files that include sensitive configuration values. <br>
Mitigation: Avoid allowing raw `.env` or credential-bearing files to be read unless redaction has been confirmed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gmmg55/skills/code-spec-guardian) <br>
- [Publisher profile](https://clawhub.ai/user/gmmg55) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Code Spec Index](artifact/references/index.md) <br>
- [Self-Evolution](artifact/references/evolution.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code and shell command snippets; may create or update project convention files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create and update `.code-spec/` files and may propose or apply an `AGENTS.md` trigger rule during first analysis.] <br>

## Skill Version(s): <br>
1.3.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
