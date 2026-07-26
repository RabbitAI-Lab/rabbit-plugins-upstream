## Description: <br>
Detect image generation requests and route them to the artist agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to identify image-generation requests, collect the prompt and style context, route the request to an artist agent, and return the generated result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image prompts and feedback may contain private, client, personal, or regulated information and the skill asks the agent to store them persistently. <br>
Mitigation: Ask before storing prompts or feedback, store only minimal request metadata when possible, and define clear retention and deletion behavior. <br>
Risk: Problematic image requests could be routed to the artist agent if policy review is skipped. <br>
Mitigation: Review the request before handoff and decline ethically problematic requests before routing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/image-handoff) <br>
- [Publisher profile](https://clawhub.ai/user/space-cadet) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown] <br>
**Output Format:** [Markdown instructions with structured handoff text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include extracted prompts, style preferences, request IDs, routing results, and user feedback summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
