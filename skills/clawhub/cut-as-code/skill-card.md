## Description:

Routes Project Protocol V1 video editing requests to the appropriate leaf skill and recovers explicit project state before handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill as an entry-point router for Project Protocol V1 video editing projects. It helps an agent resume recorded project state and hand off to the correct video editing skill without taking over editorial, review, or rendering decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependent video skills may read or update project files and render outputs after this router hands off.

Mitigation: Review any separately installed dependent video skills and use explicit project roots with work/project.json before execution.

Risk: Ambiguous project state or unclear deliverables can cause the agent to choose the wrong workflow.

Mitigation: Require an explicit project root, source, or deliverable and ask one routing question when the requested route is genuinely ambiguous.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whitetowerai/skills/cut-as-code)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration]

**Output Format:** [Markdown guidance with routing tables and ordered workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes state recovery and handoff decisions; selected leaf skills own editing plans, review gates, render scripts, and final media outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
