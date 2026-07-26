## Description: <br>
Polishes working code through successive quality passes in fresh subagents. Use after tests pass when code needs multi-dimension refinement before release. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill after tests pass to iteratively refine working code across correctness, clarity, consistency, and polish before review or release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may edit files in the selected target during iterative polishing. <br>
Mitigation: Review the target scope before use and inspect resulting diffs before committing changes. <br>
Risk: The workflow may write local state under .attune/, which can create repository-cleanliness issues if committed unintentionally. <br>
Mitigation: Delete or ignore .attune/dorodango-state.json when the state should not be committed. <br>
Risk: Polishing suggestions or edits could introduce incorrect behavior despite passing earlier tests. <br>
Mitigation: Run the project test suite and review changes after each pass, especially after clarity, consistency, and polish edits. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-dorodango) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>
- [Pass definitions](artifact/modules/pass-definitions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with code-editing steps, shell command suggestions, and JSON state tracking] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local polishing state under .attune/dorodango-state.json] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
