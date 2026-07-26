## Description: <br>
Classifies and enforces constraints via soft vows, hard vows, and Nen Court layers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to classify project rules, audit enforcement gaps, and decide whether constraints belong in skill guidance, hooks, or external validation gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger words may make the skill appear in more governance or compliance conversations than intended. <br>
Mitigation: Treat its recommendations as advisory unless the user intentionally implements separate hooks or validators. <br>
Risk: Guidance about enforcement layers could be mistaken for active enforcement. <br>
Mitigation: Confirm that any required hooks, permissions, or validator agents are implemented and tested outside this documentation-only skill. <br>
Risk: Soft rules can fail when model goals conflict with project constraints. <br>
Mitigation: Promote high-risk binary constraints to hard hooks and route judgment-heavy checks through external validation gates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-vow-enforcement) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with tables, examples, and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only release artifact with no executable code included.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
