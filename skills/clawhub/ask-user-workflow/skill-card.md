## Description: <br>
Ask User Workflow helps an agent ask bundled clarifying questions for ambiguous tasks, then summarize the answers into an actionable plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[9438190](https://clawhub.ai/user/9438190) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when a request is too ambiguous to act on directly. It guides the agent to gather a small set of clarifying answers and convert them into a concise task plan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may add clarification prompts when the user expected the agent to proceed immediately. <br>
Mitigation: Use it only for complex or ambiguous requests, and proceed directly when the user already provided complete requirements or explicitly asked not to be questioned. <br>
Risk: A task summary can misstate intent if the bundled questions are too broad or omit a key requirement. <br>
Mitigation: Keep questions specific to the decision needed, summarize the selected answers, and ask for confirmation before execution when uncertainty remains. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/9438190/skills/ask-user-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text] <br>
**Output Format:** [Markdown task summaries and concise clarifying-question prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May prompt the user for a small set of clarification choices before summarizing next steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
