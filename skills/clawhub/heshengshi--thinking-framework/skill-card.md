## Description: <br>
Thinking Framework loads a target person's, organization's, philosophy's, or system's cognitive and psychological framework so an agent can apply that clearly labeled analytical lens to a user's problem without impersonating the target. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heshengshi](https://clawhub.ai/user/heshengshi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to build an evidence-graded cognitive and psychological framework for a target person, organization, philosophy, or system and apply it to decisions, analysis, creation, debate, stress tests, forecasts, or problem solving. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce speculative psychological analysis of real people that readers may over-treat as fact or diagnosis. <br>
Mitigation: Treat outputs as uncertain inference, require evidence labels, avoid diagnosis or high-stakes judgments, and limit living-person analysis to publicly documented patterns. <br>
Risk: Framework mode can drift into impersonation, fabricated quotes, or misleading first-person presentation. <br>
Mitigation: Keep responses in the agent's own voice, clearly label framework use, and do not format generated content as real quotes from the target. <br>
Risk: The artifact includes step-by-step reasoning disclosure guidance that may conflict with deployments that hide private reasoning. <br>
Mitigation: Before deployment, replace requests for step-by-step reasoning disclosure with concise rationale summaries appropriate to the host agent's policy. <br>
Risk: Applying a loaded framework to harmful, deceptive, or manipulative goals could amplify unsafe advice. <br>
Mitigation: Review user intent before applying the framework and decline harmful, deceptive, manipulative, or otherwise unsafe requests. <br>


## Reference(s): <br>
- [Layer 1 - Cognitive Architecture](references/layer1-cognitive.md) <br>
- [Layer 2 - Deep Psychological Architecture](references/layer2-psychological.md) <br>
- [Layer 3 - Active Framework Operational Protocol](references/layer3-operational.md) <br>
- [Layer 4 - Synthesis, Integration & Composite Frameworks](references/layer4-synthesis.md) <br>
- [Model Guidance - Compensation for Weaker / Local Models](references/model-guidance.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, analysis] <br>
**Output Format:** [Markdown text with structured framework cards, evidence labels, and analytical guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on the target and user task; the skill instructs the agent to label uncertainty, avoid impersonation, and surface blind spots.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
