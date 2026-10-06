## Description:

Turns advisor-written product answers and public Xiaohongshu note questions into separate short spoken wealth FAQ videos, one per question.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Wealth advisors use the skill to turn public Xiaohongshu FAQ questions and their own approved product answers into a written clip plan and individual talking videos for posting themselves. It does not post to Xiaohongshu or provide personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared device credential grants broad Beatra access, including paid media generation.

Mitigation: Connect only when comfortable with that authority, and require explicit approval of each paid lookup or generation step and its live cost.

Risk: Package code silently updates by default.

Mitigation: Disable automatic updates before use with the documented update --auto off command if changes must be reviewed first.

Risk: Questions, images, or voice samples may be used without appropriate permission.

Mitigation: Use public questions and only stills, likenesses, and voices the advisor has rights to reuse.

Risk: Generated wealth content could imply unsupported returns or personalized advice.

Mitigation: Use only the advisor's supplied product answers; do not invent yields, promises, or buy-or-sell recommendations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/xiaohongshu-wealth-faq-talking)
- [Publisher skill page](https://beatra.ai/skills/xiaohongshu-wealth-faq-talking)
- [Wealth FAQ talking workflow](references/workflow.md)
- [Note lookup](references/note-lookup.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Video files, Audio files]

**Output Format:** [Markdown clip plan and separate media artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One video per approved question and still; reports available file details and actual credits charged.]

## Skill Version(s):

0.1.8 (source: server-resolved release and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
