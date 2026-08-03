## Description: <br>
Audit an LLM evaluation or benchmark repo for integrity and credibility practices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, benchmark maintainers, and reviewers use this skill to audit LLM evaluation repositories before publishing scores, submitting grants, or defending leaderboard methodology. It reports integrity gaps across pre-registration, contamination, holdout hygiene, judge validity, statistical honesty, reproducibility, and leaderboard exclusion practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The audit requires the agent to read the target benchmark repository and inspect open pull requests with the GitHub CLI. <br>
Mitigation: Run it only in environments where repository contents and open PR metadata may be reviewed by the agent. <br>
Risk: The artifact does not describe a local-only mode for private benchmark reviews. <br>
Mitigation: Confirm the workspace, agent, and GitHub CLI access are acceptable for private work before invoking the skill. <br>
Risk: The output is an advisory audit report and may affect benchmark methodology decisions if applied without review. <br>
Mitigation: Review the cited file:line evidence and approve any methodology changes separately before implementing fixes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/eval-integrity) <br>
- [Dimension Audit Briefs](artifact/patterns/dimension-prompts.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown audit report with file:line evidence, severity ratings, and concrete fixes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only audit output; does not edit benchmark repositories or rerun evaluations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
