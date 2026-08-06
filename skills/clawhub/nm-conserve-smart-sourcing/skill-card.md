## Description: <br>
Selects optimal sources for tool calls, balancing accuracy with token cost. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill before research tasks or factual responses to decide when source verification is worth the cost, especially for version, security, API, pricing, release, and other time-sensitive claims. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may recommend skipping citations for claims that later prove time-sensitive or consequential. <br>
Mitigation: Apply the skill's stricter sourcing categories for security, pricing, API, release, version, and other high-impact claims, and use cited verification when uncertainty could cause harm. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-smart-sourcing) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, text] <br>
**Output Format:** [Markdown guidance with decision rules and citation examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Helps agents choose between no sourcing, uncertainty markers, and cited web searches based on claim risk and verification cost.] <br>

## Skill Version(s): <br>
1.9.17 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
