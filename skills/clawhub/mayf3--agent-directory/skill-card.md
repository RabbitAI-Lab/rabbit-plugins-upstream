## Description: <br>
Agent Directory helps maintain JSON-based agent profiles, including roles, pipeline ownership, status, and long-term planning details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayf3](https://clawhub.ai/user/mayf3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators maintaining an agent team directory use this skill to create, validate, and index JSON profiles that track agent roles, pipeline ownership, status, and planning details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The included scripts read local agent profile JSON files and can rewrite the generated profile index. <br>
Mitigation: Run the scripts only in the intended workspace and review generated index changes before committing or sharing them. <br>
Risk: Agent profile data may contain internal group identifiers, workspace names, or planning details. <br>
Mitigation: Review and redact profile data before sharing generated output outside the intended audience. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON examples and bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read local agent profile JSON files and rewrite docs/agent-profiles/index.json when scripts are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
