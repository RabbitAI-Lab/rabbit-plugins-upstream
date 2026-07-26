## Description: <br>
Helps QA and engineering teams model complex business logic and system boundaries with state machines, data-flow views, and service-dependency views. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and requirements analysts use this skill to turn complex requirements or scenario-tree inputs into domain models that expose object states, data movement, service dependencies, and missing business rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may cause the agent to apply the skill to general modeling requests where a narrower skill would be enough. <br>
Mitigation: Use the skill when the request involves complex requirements, subsystem interaction, state transitions, data flow, or service dependencies. <br>
Risk: A domain model may omit subsystems, states, data paths, or failure impacts that are not explicit in the source requirements. <br>
Mitigation: Cross-check outputs against the scenario tree or requirements, use the included completion checklist, and retry modeling after filling any gaps. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown with text diagrams and structured tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces state-machine, data-flow, and service-dependency views with traceability IDs when source scenarios are available.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
