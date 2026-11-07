## Description:

Runs a two-minute guided Cargo demo for new users: one question about who they sell to, then 25 real leads with a cost receipt, saved as a recurring play. Works on a fresh account (100 free credits, no card). Triggers: "show me what Cargo can do", "give me a demo", "take me on a tour", "quickstart", "getting started with Cargo", "I just installed Cargo", "my workspace is empty", "does this actually work". Skip when: the user has a real job to run (build a list, enrich a CSV, find emails), use cargo-gtm; when they want CLI reference or routing, use the cargo router skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

New Cargo users use this guided workflow to try a small lead search, review its cost and results, and optionally save the search as a weekly recurring play. It is intended for onboarding and a first look at Cargo; users with a concrete GTM task should use the dedicated GTM workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional weekly runs have unclear ongoing credit costs, storage changes, and cancellation controls.

Mitigation: Before enabling weekly runs, obtain the scheduling recipe, confirm recurring costs and storage changes, and establish spending and cancellation controls.

Risk: The external CLI version and scheduling implementation were not verified.

Mitigation: Use a reviewed CLI version and obtain and review the scheduling recipe before enabling automation.

Risk: Temporary lead exports may remain after the demo.

Mitigation: Remove temporary lead exports after use.

## Reference(s):

- [Cargo Quickstart on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-quickstart)
- [Cargo skills project homepage](https://github.com/getcargohq/cargo-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Conversational instructions with shell command examples, a lead summary table, and a cost receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user's buyer persona; the documented fast path searches up to 25 leads with an approximately 5-credit budget.]

## Skill Version(s):

1.1.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
