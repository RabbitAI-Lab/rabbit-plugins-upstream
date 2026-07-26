## Description: <br>
Choose TokenLab models and fallback chains using public pricing, task fit, latency expectations, and native endpoint needs before writing production routing code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hedging8563](https://clawhub.ai/user/hedging8563) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to choose cost-aware TokenLab model routes, compare pricing-aware options, and design fallback chains that preserve required endpoint behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence is clean, but cost recommendations can become stale if public catalog or pricing data is unavailable or not refreshed. <br>
Mitigation: Use the current TokenLab catalog and pricing endpoints before recommending models, and state when a route cannot be price-verified. <br>
Risk: A cheaper fallback could change output quality, safety behavior, structured output support, media support, or endpoint semantics. <br>
Mitigation: Require explicit user approval before quality-reducing or paid media/video fallback changes, and document capability tradeoffs in the route table. <br>


## Reference(s): <br>
- [TokenLab model catalog](https://api.tokenlab.sh/v1/models) <br>
- [TokenLab recommended model catalog](https://api.tokenlab.sh/v1/models?recommended_for=<scene>) <br>
- [TokenLab model details](https://api.tokenlab.sh/v1/models/{model}) <br>
- [TokenLab model pricing](https://api.tokenlab.sh/v1/models/{model}/pricing) <br>
- [ClawHub skill page](https://clawhub.ai/hedging8563/skills/tokenlab-cost-routing) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with routing tables and inline catalog or pricing commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes workload assumptions, model route roles, endpoint notes, fallback conditions, and implementation guardrails.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
