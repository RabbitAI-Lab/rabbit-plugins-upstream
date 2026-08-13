## Description:

Guided first-run demo for the Cargo CLI - from a fresh workspace to a real deliverable of 25 leads matching the user's buyer persona, with a cost receipt, in under two minutes and ending by saving the demo as a recurring play.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, sales operators, and go-to-market teams use this skill to run a guided first Cargo CLI demo that sources a small buyer-persona lead set, shows spending and hit-rate, and offers to convert the search into a recurring play.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend Cargo account credits during the demo.

Mitigation: Keep the normal demo path near the documented one-credit cap, require explicit confirmation before higher-cost fallback actions, and review the receipt after execution.

Risk: The buyer persona may be sent to external lead providers and resulting lead data may be temporarily stored on the local machine.

Mitigation: Avoid sensitive persona inputs, confirm before networked or paid actions when needed, and delete temporary output files after the demo.

Risk: A recurring play can continue running after the initial demo.

Mitigation: Confirm the schedule, destination, and cost expectations before enabling recurrence, and monitor or disable the play when it is no longer needed.

## Reference(s):

- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo Quickstart on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-quickstart)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise tabular lead summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create temporary local JSON files for run metadata and lead outputs during the demo.]

## Skill Version(s):

1.0.1 (source: frontmatter, skill-metadata.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
