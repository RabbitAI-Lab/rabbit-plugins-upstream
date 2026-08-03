## Description: <br>
Standardizes release approvals with GitHub-aware checklists and deployment gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, release managers, and operations teams use this skill before production releases to evaluate release gates, record waivers, and prepare PR or issue-ready rollout summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate during broad release- or GitHub-related conversations. <br>
Mitigation: Confirm the skill is appropriate for the workspace before installation and use it intentionally for release-readiness workflows. <br>
Risk: Release gates may affect PR comments, approvals, tracker fields, or other release records when paired with external tooling. <br>
Mitigation: Keep state-changing actions explicit, review generated release text before posting, and review any separate Claude Code plugin before installing it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-minister-release-health-gates) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/minister) <br>
- [Deployment Readiness Gate](modules/deployment-readiness.md) <br>
- [Quality Signals Gate](modules/quality-signals.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown checklists, summaries, and rollout scorecards] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable code is included in the artifact.] <br>

## Skill Version(s): <br>
1.9.17 (source: release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
