## Description: <br>
Parallel (parallel.ai) helps agents read, create, and update Parallel data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate Parallel through an OOMOL-connected account for web research, structured data enrichment, URL extraction, ranked web search, and task-run retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create Parallel task runs that change account state. <br>
Mitigation: Confirm the exact payload and expected effect with the user before approving create_task_run or any future write/destructive connector action. <br>
Risk: The skill depends on OOMOL account setup, the oo CLI, and a connected Parallel account. <br>
Mitigation: Run first-time setup only when a command fails with an authentication, missing CLI, missing scope, expired credential, or connection error. <br>


## Reference(s): <br>
- [Parallel homepage](https://parallel.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-parallel) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Parallel task-run status, ranked source excerpts, extracted content, or setup guidance depending on the requested action.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact metadata and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
