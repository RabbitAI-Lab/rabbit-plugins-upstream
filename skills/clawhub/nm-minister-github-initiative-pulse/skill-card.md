## Description: <br>
Generates markdown digests and CSV exports for GitHub initiative health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and project maintainers use this skill to turn tracker data and GitHub project metadata into initiative-level status digests, scorecards, blocker summaries, and CSV-style reporting content for issues, pull requests, and discussions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may trigger on broad GitHub, reporting, dashboard, project, or status requests. <br>
Mitigation: Review generated GitHub comments, labels, issue follow-ups, CSV exports, and reports before posting or applying them. <br>
Risk: The artifact assumes external tracker.py and GitHub workflows that are not included in this package. <br>
Mitigation: Confirm the required tracker data source and GitHub workflow are present and current before relying on generated initiative metrics. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-minister-github-initiative-pulse) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/minister) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown digests, GitHub comment snippets, and CSV export guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Review generated GitHub comments, labels, issue follow-ups, and report content before posting or applying them.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
