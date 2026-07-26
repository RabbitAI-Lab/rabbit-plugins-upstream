## Description: <br>
Turns raw changes, commits, or PRs into clean Keep a Changelog-style release notes grouped by change type, with breaking changes and upgrade notes surfaced first. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, maintainers, and release managers use this skill to turn raw commit logs, PR titles, or change lists into user-facing changelog entries and version announcements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated changelog entries may misstate version bumps, breaking changes, migration steps, or public issue and PR references. <br>
Mitigation: Review the generated changelog against the supplied release changes and the project's versioning policy before publication. <br>
Risk: Internal-only details from raw commits or change lists may be included in public-facing release notes. <br>
Mitigation: Remove implementation-only, CI, refactor, and private planning details unless they matter to the target audience. <br>


## Reference(s): <br>
- [Changelog Writer homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/changelog-writer.html) <br>
- [Keep a Changelog](https://keepachangelog.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown changelog or release notes text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include breaking changes, upgrade notes, issue or PR references, and a semver note when the version is inferred.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
