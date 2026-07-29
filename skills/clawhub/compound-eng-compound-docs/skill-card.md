## Description: <br>
Document solved problems for team reuse, including resolved issues, lessons learned, post-mortems, knowledge-base entries, and searchable debugging knowledge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill after resolving non-trivial issues to capture symptoms, investigation attempts, root cause, solution details, prevention guidance, and related references as reusable troubleshooting documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated troubleshooting documentation may include secrets, customer data, private URLs, or inaccurate technical claims. <br>
Mitigation: Review generated docs before committing, remove sensitive information, and verify technical claims against current source files. <br>
Risk: Optional follow-up actions can modify repository documentation or create/update learning skills. <br>
Mitigation: Treat menu actions that change skills or documentation as explicit repository changes and proceed only after user confirmation. <br>


## Reference(s): <br>
- [Documentation Capture Process](references/documentation-process.md) <br>
- [YAML Frontmatter Schema](references/yaml-schema.md) <br>
- [Quality Guidelines & Error Handling](references/quality-guidelines.md) <br>
- [Example Scenario](references/example-scenario.md) <br>
- [Resolution Template](assets/resolution-template.md) <br>
- [Critical Pattern Template](assets/critical-pattern-template.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-compound-docs) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown files with YAML frontmatter, inline shell commands, and a text decision menu] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes solution documentation under docs/solutions/ and may propose follow-up documentation or skill updates after user confirmation.] <br>

## Skill Version(s): <br>
4.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
