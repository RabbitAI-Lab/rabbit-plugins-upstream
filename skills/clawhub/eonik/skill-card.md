## Description:

eonik companion guides agents using connected eonik tools to ground ad and brand work in saved brand context, competitor research, own-ad facts, ad breakdowns, memory, and receipt-bound briefs without launching ads or changing budget.

This skill is ready for commercial/non-commercial use.

## Publisher:

[techievena](https://clawhub.ai/user/techievena)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External marketers and their agents use this skill to orient on an eonik workspace, research competitors and existing ads, preserve brand memory, and draft receipt-bound creative briefs while keeping publishing and spend decisions with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambiguous ad or brand requests may cause the assistant to consult connected eonik workspace context.

Mitigation: Install and connect the skill only when the user intends agents to use eonik brand memory, competitor research, own-ad facts, and brief drafting context.

Risk: Saved notes, brand truths, plans, and remembered facts are durable in the eonik workspace.

Mitigation: Save user-provided words verbatim, read dates back for saved plans, and confirm corrections or durable preferences before recording them.

Risk: Ad research can be misread as predictive performance advice or autonomous media-buying direction.

Mitigation: Keep outputs tied to receipts, avoid performance predictions, and do not recommend pause, scale, kill, launch, or budget actions.

## Reference(s):

- [eonik tool reference](reference.md)
- [eonik setup](https://www.eonik.ai/mcp)
- [eonik MCP connector](https://github.com/eonik-ai/eonik-mcp)
- [ClawHub skill page](https://clawhub.ai/techievena/skills/eonik)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance with receipt-bound bullet insights, brief structures, references, and guardrails.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use receipts from the connected eonik account; does not launch ads, pause ads, scale ads, or move budget.]

## Skill Version(s):

2.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
