## Description: <br>
Code Spec Guardian helps agents analyze, distill, enforce, and evolve project coding conventions across common frontend and backend stacks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gmmg55](https://clawhub.ai/user/gmmg55) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to analyze a repository, generate modular `.code-spec/` convention files, and apply those conventions during code generation, bug fixes, reviews, refactors, API work, SQL work, and UI changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can scan project files and create or update persistent `.code-spec/` files during broad coding requests. <br>
Mitigation: Require confirmation before repository writes, backups, overwrites, or `.env` reads, and review generated spec diffs before committing them. <br>
Risk: The security verdict is suspicious because automatic convention evolution can silently persist guidance that affects future code generation. <br>
Mitigation: Review the generated or modified conventions before relying on them for implementation, review, or refactoring work. <br>


## Reference(s): <br>
- [Code Spec Guardian ClawHub Page](https://clawhub.ai/gmmg55/skills/code-spec-guardian) <br>
- [README](artifact/README.md) <br>
- [Skill Instructions](artifact/SKILL.md) <br>
- [Specification Index](artifact/references/index.md) <br>
- [Self-Evolution Mechanism](artifact/references/evolution.md) <br>
- [Project Context Extractor](artifact/scripts/analyze_project.py) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, configuration, guidance, shell commands, code] <br>
**Output Format:** [Markdown guidance with generated `.code-spec/` Markdown and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill routes by project language and task type, with modular convention files intended to keep context usage low.] <br>

## Skill Version(s): <br>
1.2.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
