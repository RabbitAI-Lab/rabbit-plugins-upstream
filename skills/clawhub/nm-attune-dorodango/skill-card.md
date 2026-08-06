## Description: <br>
Polishes working code through successive quality passes after tests pass, helping agents refine correctness, clarity, consistency, and release polish. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill after working code and tests are in place to run a structured refinement loop across correctness, clarity, consistency, and production polish before review or release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can modify code in the target area. <br>
Mitigation: Review diffs and rerun the relevant test suite before accepting changes. <br>
Risk: The workflow can run test or build commands in the workspace. <br>
Mitigation: Use it in a trusted repository and inspect proposed commands before execution. <br>
Risk: The workflow stores resume state in .attune/dorodango-state.json. <br>
Mitigation: Review the state file before sharing the workspace or committing generated files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-dorodango) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code edits, shell command recommendations, and a local JSON resume state file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update .attune/dorodango-state.json to track polishing progress.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
