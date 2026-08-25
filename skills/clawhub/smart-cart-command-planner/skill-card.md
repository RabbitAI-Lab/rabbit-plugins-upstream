## Description:

Convert Chinese or English natural-language requests for an OpenClaw-powered omnidirectional smart cart into conservative, structured motion plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jason15336804](https://clawhub.ai/user/jason15336804)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and smart-cart operators use this skill to convert Chinese or English movement requests into cautious JSON plans for a downstream omnidirectional cart controller, including assumptions, sensing steps, stop behavior, and confirmation needs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated motion plans may be used as controller input without enough real-world safety checking.

Mitigation: Treat every plan as a proposal and require live obstacle sensing, controller safeguards, and human review for high-risk or ambiguous movement.

Risk: Validation can create a local plan JSON file containing sensitive route or location details.

Mitigation: Avoid sensitive location details in requests unless local plan files are acceptable, and delete temporary plan files when they are no longer needed.

## Reference(s):

- [Command plan schema](artifact/references/command-schema.md)
- [Sample smart-cart plan](artifact/examples/sample-plan.json)
- [ClawHub skill page](https://clawhub.ai/jason15336804/skills/smart-cart-command-planner)

## Skill Output:

**Output Type(s):** [text, code, shell commands, guidance]

**Output Format:** [JSON command plan followed by a concise Markdown explanation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save a local plan JSON file and run the bundled validator when file execution is available.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
