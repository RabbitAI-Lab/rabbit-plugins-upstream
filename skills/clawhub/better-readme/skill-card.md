## Description: <br>
Use when the user asks to create, improve, fix, or audit a README.md file, score their README, document an open source project, or set up new project docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaszhou22](https://clawhub.ai/user/thomaszhou22) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill to audit, score, create, and improve project README files across common project types. It helps agents classify a project, run README quality checks, generate Markdown documentation, and apply a pre-publish checklist. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads README content and project metadata to classify projects and score documentation quality. <br>
Mitigation: Confirm the target project path and intended files before running scans or generating documentation. <br>
Risk: The onboarding workflow can optionally review public GitHub repository READMEs. <br>
Mitigation: Decline the onboarding repository audit for local-only use, or approve only the public repositories intended for review. <br>
Risk: README generation or multilingual output can replace or add documentation files. <br>
Mitigation: Review the preview or diff before allowing README.md or language-specific README files to be written. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thomaszhou22/skills/better-readme) <br>
- [Scoring Rubric](references/scoring-rubric.md) <br>
- [README Templates](references/templates.md) <br>
- [Pre-Publish Checklist](references/pre-publish-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, README drafts, audit scores, optional JSON audit output, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate or revise README.md and optional language-specific README files after user review.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata; artifact frontmatter says 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
