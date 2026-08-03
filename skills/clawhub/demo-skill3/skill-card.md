## Description: <br>
Reviews a short product idea and returns structured feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jshiu0915](https://clawhub.ai/user/jshiu0915) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product managers, and founders use this skill to get a concise critique of a short product idea, including target user, core value, practical suggestions, and the highest-risk assumption to validate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A user could expose sensitive product information by pasting it into the prompt or pointing the agent at an unintended file. <br>
Mitigation: Provide only the product idea content intended for review, or point the agent at one specific intended file; avoid private files, network access, and shell commands. <br>
Risk: The critique may be incomplete or misleading if used as the sole basis for product decisions. <br>
Mitigation: Treat the output as lightweight feedback and validate the highest-risk assumption with users or market evidence before acting. <br>


## Reference(s): <br>
- [Demo Skill 3 ClawHub page](https://clawhub.ai/jshiu0915/skills/demo-skill3) <br>
- [Publisher profile](https://clawhub.ai/user/jshiu0915) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Product idea example](artifact/examples/product-idea.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Analysis] <br>
**Output Format:** [Markdown with structured sections for summary, suggestions, and validation risk] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Concise critique based only on the user's provided idea; no network access, private file access, or shell execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
