## Description: <br>
Evaluates and improves skills, agents, commands, and hooks after a workflow slice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill after a short workflow or command run to identify slow, confusing, repetitive, or fragile steps, then plan and validate improvements to related skills, agents, commands, and hooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can review workflow history and project context that may include sensitive operational details. <br>
Mitigation: Review the context and generated summaries before sharing them, and avoid including secrets, private project names, stack traces, architecture details, or internal operational notes. <br>
Risk: Automatic GitHub issue creation can publish deferred work, recommendations, or tooling lessons to an external repository. <br>
Mitigation: Disable automatic issue creation unless intended, check for duplicates, and review every proposed issue or discussion post before allowing publication. <br>
Risk: The skill may suggest changes to workflow assets that affect future agent behavior. <br>
Mitigation: Keep changes bounded, review diffs, run targeted validation, and compare before-and-after workflow metrics before relying on the updated assets. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/athola/skills/nm-sanctum-workflow-improvement) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with checklists, plans, metrics tables, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file edits, validation commands, GitHub issue content, and retrospective metrics for human review.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
