## Description:

Reflective Tarot provides non-predictive, non-clinical tarot-style prompts for emotional reflection, self-awareness, grounding, and meaning-making.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to generate symbolic single-card or three-card tarot reflections that preserve user agency. It is intended for gentle reflection and grounding, not prediction, diagnosis, therapy, or medical, legal, or financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the skill requests broad read, write, and command-execution authority that does not fit its tarot reflection purpose.

Mitigation: Install only with narrowed permissions appropriate to text-only reflective guidance, and do not grant read, write, exec, API key, callback, file-processing, or command-execution authority unless separately justified.

Risk: Tarot-style guidance can be mistaken for prediction or professional advice.

Mitigation: Keep responses symbolic, non-clinical, non-predictive, and agency-preserving; refuse medical, legal, and financial advice.

Risk: Users expressing self-harm intent need safety-first support rather than tarot interpretation.

Mitigation: Pause tarot output when self-harm intent is detected and switch to crisis-support guidance and appropriate resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/tarot)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)
- [Source artifact](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text with card names, upright or reversed orientation, keywords, reflective prose, and an invitation question.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-card and three-card spreads use internally random Major Arcana selections, with about a 35% chance of reversed orientation.]

## Skill Version(s):

1.0.2 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
