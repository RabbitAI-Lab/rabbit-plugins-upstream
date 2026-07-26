## Description: <br>
Enforces validation and evidence before claiming work complete. Use before declaring implementation done, creating a PR, or submitting deliverables for review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill before implementation completion, pull request submission, or review handoff to require reproducible tests, acceptance criteria, evidence logs, and known-issue checks before claiming work is done. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Evidence logs and command output can expose tokens, account IDs, internal hostnames, or sensitive environment values. <br>
Mitigation: Review and redact evidence logs before sharing them outside the intended audience. <br>
Risk: Stricter proof-of-work gates can make testing and validation tasks more process-heavy. <br>
Mitigation: Apply the skill when completion claims, reviews, or deliverables need reproducible evidence, and keep evidence snippets focused on the claim being proven. <br>
Risk: Validation examples include shell commands that inspect local state and may need adaptation to the user's environment. <br>
Mitigation: Run commands in the target environment, avoid destructive variants, and record pass, fail, partial, or blocked status honestly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-proof-of-work) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>
- [Atlassian definition of done](https://www.atlassian.com/agile/project-management/definition-of-done) <br>
- [Cargo cult programming](https://en.wikipedia.org/wiki/Cargo_cult_programming) <br>
- [Software Reuse in the Generative AI Era](https://dl.acm.org/doi/10.1145/3755881.3755981) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with checklists, command examples, evidence logs, acceptance criteria, and retry prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs emphasize reproducible evidence, pass/fail status, blockers, and user-verifiable completion claims.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
