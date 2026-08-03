## Description: <br>
Guides agents to write and update trustworthy software specification documents by recording only confirmed content, tracking coverage separately, and reporting cross-reference impacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jivecheng](https://clawhub.ai/user/jivecheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product managers, and agents use this skill to create or update software specs, PRDs, ADRs, requirements, acceptance criteria, API specs, and related project documentation without fabricating unconfirmed decisions. It is designed for projects that need persistent coverage tracking, explicit open questions, and impact reporting after documentation changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes and maintains project specification files, so unreviewed output could preserve incorrect assumptions as project documentation. <br>
Mitigation: Review generated or changed specifications, keep unconfirmed items marked as draft, tbd, or missing, and confirm affected sections before relying on them for implementation. <br>
Risk: The skill enforces a strict documentation workflow that may not fit projects using looser specification styles or non-Mermaid diagram standards. <br>
Mitigation: Use it only when the project accepts persistent coverage tracking, explicit status labels, Mermaid diagrams, and mandatory impact reporting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jivecheng/skills/software-spec-writing) <br>
- [Consideration Item List](references/chapters.md) <br>
- [Writing Conventions](references/conventions.md) <br>
- [Coverage File Guide](references/coverage.md) <br>
- [Glossary](references/glossary.md) <br>
- [Spec Coverage Template](assets/spec-coverage.template.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown documents and YAML coverage updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maintains spec-coverage.yaml and reports written items, affected sections, and remaining gaps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
