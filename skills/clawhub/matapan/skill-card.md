## Description: <br>
Work inside a Matapan workspace: scoped file edits, hardened container runs, commits, and sealing an immutable proposal for human review and compare-and-swap apply. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mentholmike](https://clawhub.ai/user/mentholmike) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to make code changes inside a Matapan workspace, run verification in a hardened container, commit work, and seal an immutable proposal for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may attempt actions that are outside their Matapan scope, such as applying proposals, granting secrets or network access, or destroying workspaces. <br>
Mitigation: The skill instructs agents to stop and ask the human for grants, approval, teardown, or other operator-scoped actions. <br>
Risk: Code-change proposals could contain incorrect or misleading changes if verification is skipped or overstated. <br>
Mitigation: The skill requires build or test verification inside workspace_run before sealing, and asks agents to report exact commands and outcomes with the proposal ID. <br>
Risk: Secrets or external network access could be mishandled during workspace runs. <br>
Mitigation: The skill describes no network by default, human-controlled egress and secret grants, and redacted outputs; agents are told not to write secret values into files, command output, or proposal diffs. <br>


## Reference(s): <br>
- [Matapan on ClawHub](https://clawhub.ai/mentholmike/skills/matapan) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with tool names, command references, and handoff instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent workflow guidance for Matapan workspace operations; final proposals remain subject to human review and apply.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
