## Description: <br>
Plan the delivery route for an artifact. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[wxt-ai](https://clawhub.ai/user/wxt-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and evaluators use this skill to route artifact delivery or export requests into a concise route_mode for controlled validation scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is a controlled validation artifact and may be mistaken for a full operational delivery-planning tool. <br>
Mitigation: Use it only for narrow routing or validation scenarios and review outputs before applying them to real artifact handoffs. <br>
Risk: Restricted artifact handoff requests could involve sensitive material outside the skill's intended synthetic examples. <br>
Mitigation: Do not provide credentials, private files, or uncontrolled external endpoints when using this skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/artifact-export-route-identifier) <br>


## Skill Output: <br>
**Output Type(s):** [text] <br>
**Output Format:** [Concise plain text route mode] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns one route_mode value for the current export_request.] <br>

## Skill Version(s): <br>
1.0.4 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
