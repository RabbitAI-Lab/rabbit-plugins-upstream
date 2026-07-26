## Description: <br>
Generates markdown digests and CSV exports for GitHub initiative health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, project maintainers, and coordination teams use this skill to turn GitHub tracker and board data into initiative status digests, blocker summaries, and CSV-ready reporting outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated GitHub status text could be outdated, incomplete, or misleading if tracker data is stale. <br>
Mitigation: Review the generated markdown and confirm source tracker or GitHub board data before posting to issues, pull requests, or Discussions. <br>
Risk: The skill may activate on broad GitHub or status-reporting requests. <br>
Mitigation: Confirm the intended reporting context before using its snippets or summaries. <br>
Risk: Separate Claude Code plugin or tracker.py tooling referenced by the skill is outside this release's security evidence. <br>
Mitigation: Evaluate any external plugin or tracker tooling independently before installing or running it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-minister-github-initiative-pulse) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/athola) <br>
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/minister) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, guidance] <br>
**Output Format:** [Markdown digests, GitHub comment snippets, and CSV export guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Review generated markdown before posting it to GitHub issues, pull requests, or Discussions.] <br>

## Skill Version(s): <br>
1.9.16 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
