## Description:

Foodora-only CLI for checking past orders and active order status (Deliveroo WIP).

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent guide Foodora account setup, order lookup, active order tracking, history inspection, and confirmed reorder commands through the ordercli executable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install an unpinned third-party executable.

Mitigation: Review the package source and install a pinned, trusted ordercli version when possible.

Risk: ordercli may handle account passwords, browser cookies, browser profiles, and session tokens.

Mitigation: Avoid importing browser cookies or profiles unless session exposure is acceptable, and use password-stdin rather than placing passwords in command history.

Risk: The Deliveroo flow is documented as work in progress and requires bearer-token style credentials.

Mitigation: Do not provide Deliveroo tokens unless intentionally testing the unfinished Deliveroo flow.

Risk: Reorder commands can change cart state.

Mitigation: Use preview mode first and require explicit confirmation before cart-changing actions.

## Reference(s):

- [ordercli homepage](https://ordercli.sh)
- [Foodora Austria](https://www.foodora.at/)
- [ordercli Go module](https://github.com/steipete/ordercli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include commands that install and run a third-party executable.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
