## Description: <br>
Iterate automates multi-round code review and iteration by running configurable parallel review dimensions, applying atomic fixes, routing architectural fixes for approval, validating, merging, and pushing until no findings remain or a configured round limit is reached. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jingzhao-l](https://clawhub.ai/user/jingzhao-l) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use Iterate before release, during refactoring, or at iteration wrap-up to systematically review code across correctness, security, performance, architecture, tests, and related dimensions, then apply validated fixes under its workflow controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact code changes and git operations, including commits, merges, and pushes. <br>
Mitigation: Install only for explicitly invoked automation, verify the target branch, consider setting git.push_per_round to false, and review generated commits plus the decision log before allowing remote updates. <br>
Risk: Project-configured validation commands may run during the iteration workflow. <br>
Mitigation: Review validation.commands and command whitelists before use so only trusted project commands are executed. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/jingzhao-l/iterate-skill) <br>
- [ClawHub release page](https://clawhub.ai/jingzhao-l/skills/iterate-skill) <br>
- [Agent Skills](https://agentskills.io/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and structured text with code edits, shell commands, configuration guidance, and decision-log entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces an iterative workflow for review findings, fixes, validation results, commits, merges, pushes, and summaries.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
