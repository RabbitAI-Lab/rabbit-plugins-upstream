## Description: <br>
Converts raw git logs, commit lists, or release notes into polished, user-facing changelog entries following Keep a Changelog conventions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, release managers, and documentation writers use this skill to turn commit history, release notes, or a diff summary into a curated changelog section for a specific version and audience. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated changelog entries may misstate user-visible changes or omit important breaking-change details. <br>
Mitigation: Review the changelog against the supplied commits, release notes, and known migration requirements before publishing. <br>
Risk: User-supplied commit history may include internal identifiers or implementation details that are not appropriate for public release notes. <br>
Mitigation: Remove internal-only details and keep entries focused on externally observable behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mohitagw15856/skills/changelog-generator) <br>
- [Skill Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/changelog-generator.html) <br>
- [Keep a Changelog](https://keepachangelog.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown changelog section with version header, categorized changes, and migration notes when applicable] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Omit empty sections and review generated entries for accuracy before publishing.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
