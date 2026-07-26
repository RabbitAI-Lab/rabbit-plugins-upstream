## Description: <br>
Update Skill guides an agent through a gated refresh of one skill repository entry, including research, version and changelog updates, validation, and commit or PR follow-through. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and maintainers use this skill to refresh a single skill in a skills repository, review proposed edits at approval gates, update release metadata, run validation, and prepare repository changes for publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-assisted refreshes can introduce incorrect or misleading changes to skill files or release metadata. <br>
Mitigation: Review the Gate 1 proposed edits, validation output, and Gate 2 diff before approving changes. <br>
Risk: After approval, the workflow can commit and push repository changes that may publish through the repository pipeline. <br>
Mitigation: Approve Gate 2 only after confirming the target branch, privacy scan result, diff, and CI or publication expectations. <br>


## Reference(s): <br>
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/update-skill) <br>
- [Keep a Changelog 2.0.0](https://keepachangelog.com/en/2.0.0/) <br>
- [Semantic Versioning](https://semver.org/spec/v2.0.0.html) <br>
- [Pond MCP](https://pond.cascade.fyi/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands, proposed file edits, changelog entries, and git workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses two human approval gates before applying edits and before committing or pushing repository changes.] <br>

## Skill Version(s): <br>
0.8.1 (source: metadata.version, release.version, and CHANGELOG.md, released 2026-07-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
