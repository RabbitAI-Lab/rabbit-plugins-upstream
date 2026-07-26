## Description: <br>
Smart Router Publish helps Hermes agents route non-trivial prompts to local, flash, or pro model tiers using local classification and model-switch recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[raydatalab](https://clawhub.ai/user/raydatalab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to help Hermes agents choose a cost-appropriate model tier before answering non-trivial prompts. It is intended for model switching, token-cost reduction, and local routing recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate often because it uses broad model-switching and routing triggers. <br>
Mitigation: Review routing recommendations before changing tiers, and skip routing for trivial prompts as described in the skill documentation. <br>
Risk: The skill depends on external smart_router and Ollama setup for local classification. <br>
Mitigation: Review and test the local smart_router/Ollama configuration before deploying the skill. <br>
Risk: Model-tier recommendations can be advisory rather than authoritative for a specific task. <br>
Mitigation: Confirm the current tier and task complexity before applying a suggested model switch. <br>


## Reference(s): <br>
- [Smart Router Publish on ClawHub](https://clawhub.ai/raydatalab/skills/hermes-smart-router) <br>
- [Hermes Smart Router homepage](https://github.com/raydatalab/hermes-smart-router) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline code, YAML configuration, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces advisory model-tier recommendations for local, flash, and pro routing.] <br>

## Skill Version(s): <br>
0.2.2 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
