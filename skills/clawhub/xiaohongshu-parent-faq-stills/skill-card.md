## Description:

Turn Xiaohongshu parent FAQ notes into a 4 to 8 still answer set. This parent FAQ still studio reads public parent notes and questions, then lays out an answer still pack from confirmed teaching facts. Use it for parent FAQ graphics, answer stills, a Xiaohongshu parent FAQ still, and an answer card set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and school communication staff use this skill to turn public Xiaohongshu parent FAQ questions and confirmed teaching facts into a reviewed set of answer stills. It plans a free question-to-answer slot list first, then separates paid lookup, image generation, transform, and edit stages behind explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad Beatra device authorization and stores a reusable local bearer token.

Mitigation: Use a Beatra account with permissions and wallet exposure appropriate for the workflow, and protect ~/.beatra credentials as sensitive local state.

Risk: Default-on verified self-updates can replace package-owned files without a separate prompt.

Mitigation: Review the documented update controls and disable automatic checks with the bundled update command if this is not acceptable for the deployment.

Risk: Lookup and image generation can consume Beatra credits.

Mitigation: Keep the skill's separate approval cards for lookup, generate, transform, and edit stages, and verify live prices before each paid step.

Risk: Generated answer stills may contain small or inaccurate rendered text.

Mitigation: Review each generated still against the selected parent question and confirmed answer line before publishing or sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/xiaohongshu-parent-faq-stills)
- [Parent FAQ still workflow](references/workflow.md)
- [Parent FAQ lookup](references/parent-faq-lookup.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a visible slot plan and, after separate approvals, guidance for Beatra lookup and image tasks that can result in still-image files.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
