## Description:

AI Life Coach uses Socratic, structured dialogue to support self-awareness, goal clarification, emotional support conversations, and action planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for reflective life-coaching conversations, including self-awareness, life direction, goal setting, emotional support, and practical next-step planning. The artifact describes a crisis-first assessment path for self-harm or suicide-related language before any coaching flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags that the skill asks to preserve sensitive coaching summaries across sessions despite declaring only Read tool access and without clear opt-in, review, or deletion controls.

Mitigation: Deploy only where local memory behavior is explicit, user-consented, reviewable, and deletable; disable any persistent memory write path unless the granted tool permissions and product policy allow it.

Risk: The security evidence flags broad automatic activation on emotional phrases in a sensitive life-coaching context.

Mitigation: Use scoped activation rules and human review for deployment contexts where emotional-support prompts could be misrouted or unexpectedly triggered.

Risk: The artifact handles crisis language, but the skill is not a substitute for professional mental health, medical, legal, financial, or crisis services.

Mitigation: Keep crisis-first routing prominent, pause coaching when self-harm risk is present, and direct users to qualified local emergency or professional resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [Publisher profile](https://clawhub.ai/user/luhayden-blip)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational text and Markdown action plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a long personal growth action blueprint when enough conversation history is available.]

## Skill Version(s):

2.0.8 (source: server release metadata; artifact frontmatter and manifest list 2.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
