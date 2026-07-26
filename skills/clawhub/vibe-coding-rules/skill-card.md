## Description: <br>
Vibe Coding Rules gives coding agents a six-step development workflow for pre-change checks, safe command execution, post-change self-checks, automated web testing, changelog creation, and self-growing project rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ron-dali](https://clawhub.ai/user/ron-dali) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers, solo builders, small teams, and heavy AI-agent users use this skill to apply a repeatable coding workflow that checks changes before and after implementation, runs safer terminal and web-test steps, records changelogs, and grows project-specific rules from repeated issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated project-file edits can change workspace structure, generated documentation, or quality-rule files. <br>
Mitigation: Install and run the skill in a development workspace, review target paths and generated file changes, and commit only after inspection. <br>
Risk: Optional screenshot and OCR testing can capture secrets or private user data displayed in a browser. <br>
Mitigation: Disable or avoid screenshot and OCR tests on sensitive pages, and review captures before sharing or storing them. <br>
Risk: Generated changelog sharing can expose a contact phone number if the optional shareContact field is populated. <br>
Mitigation: Keep shareContact.phone empty unless the value is intentionally public. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ron-dali/skills/vibe-coding-rules) <br>
- [Publisher Profile](https://clawhub.ai/user/ron-dali) <br>
- [README](README.md) <br>
- [Pipeline Initialization Dialog](pipeline-init/references/init-dialog.md) <br>
- [Technology Stack Checklist](pipeline-init/references/tech-stack-checklist.md) <br>
- [Self-Check Full Rules](self-check/references/self-check-full.md) <br>
- [Growth Rules](changelog/references/growth-rules.md) <br>
- [TangBuPing Website](https://tangbuping.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline checklists, code snippets, shell commands, and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update project pipeline files, changelog entries, test scripts, and breadcrumb comments when invoked by an agent.] <br>

## Skill Version(s): <br>
2.5.3 (source: server release evidence; artifact frontmatter reports 2.5.2 and openclaw.json reports 2.5.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
