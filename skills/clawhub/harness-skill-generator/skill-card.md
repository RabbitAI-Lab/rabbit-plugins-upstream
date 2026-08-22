## Description:

Guides developers through creating Harness-based skills for complex, multi-stage, branching workflows that need quality checks and persistent state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iichaner](https://clawhub.ai/user/iichaner)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to design and scaffold complex agent skills from problem definition through architecture, reference writing, test runs, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide creation and installation of other skills into a shared agent environment.

Mitigation: Review generated skill files before installation and confirm install paths, AGENTS.md changes, MEMORY.md entries, and rollback steps.

Risk: The artifact includes guidance around automation on restricted platforms.

Mitigation: Remove or rewrite that guidance so generated skills prefer authorized APIs and stop when automation is prohibited.

Risk: The skill is primarily Chinese-language guidance, which may be missed or misunderstood by reviewers who do not read Chinese.

Mitigation: Have a qualified reviewer inspect the source guidance before deployment and confirm the generated workflow matches the intended use case.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/iichaner/harness-skill-generator)
- [ClawHub skill page](https://clawhub.ai/iichaner/skills/harness-skill-generator)
- [Architecture Guide](references/architecture-guide.md)
- [Branch Routing](references/branch-routing.md)
- [Problem Scan Guide](references/problem-scan-guide.md)
- [Quality Checklist](references/quality-checklist.md)
- [Quality Matrix](references/quality-matrix.md)
- [Reference Writing Guide](references/reference-writing-guide.md)
- [Scaffold Template](references/scaffold-template.md)
- [Style Contract](references/style-contract.md)
- [Test Run Guide](references/test-run-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with file scaffolds, checklists, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces skill structures such as SKILL.md, references/, templates/, and review or test artifacts when used by an agent.]

## Skill Version(s):

0.1.0 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
