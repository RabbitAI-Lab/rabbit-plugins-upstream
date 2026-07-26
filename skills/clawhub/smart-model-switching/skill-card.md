## Description: <br>
Auto-route tasks to the cheapest Claude model that works correctly by classifying work into Haiku, Sonnet, or Opus tiers before responding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[millibus](https://clawhub.ai/user/millibus) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to choose an appropriate Claude model tier for each task, balancing cost with task complexity and quality needs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Routing heuristics may choose a lower-capability model for sensitive, production-critical, legal, medical, financial, or security tasks. <br>
Mitigation: Review and tighten the rules before high-stakes use so those tasks consistently route to an appropriate higher-capability model. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/millibus/skills/smart-model-switching) <br>
- [ClawHub homepage](https://clawhub.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown with inline JavaScript and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides model-selection heuristics and example model settings; it does not execute commands or request credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
