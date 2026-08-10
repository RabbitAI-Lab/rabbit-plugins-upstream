## Description:

AI Delivery Spec helps agents turn requirements, PRDs, prototypes, competitor material, and existing-system inputs into traceable, reviewable, testable delivery artifacts from framing through acceptance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

Apache License 2.0

## Use Case:

Product, engineering, design, QA, compliance, and delivery teams use this skill to clarify requirements, prepare PRDs or prototypes, review changes, produce traceable acceptance artifacts, and hand off validated product intent to coding agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated checkpoints, gate results, custom folders, and handoff files may contain sensitive product, customer, or internal process details.

Mitigation: Keep generated artifacts private by default, review them before sharing, and avoid committing sensitive local customizations unless they are approved for the target audience.

Risk: Automatic domain selection or domain guidance may be insufficient for sensitive regulated domains.

Mitigation: Require human confirmation of domain fit, applicable constraints, and review scope before relying on the skill for sensitive or regulated requirements work.

Risk: Static gates can confirm structure and traceability without proving business correctness, runtime behavior, or customer acceptance.

Mitigation: Treat gate results as review inputs, then complete human review, implementation validation, and acceptance evidence before declaring delivery complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/franklinxkk/skills/ai-delivery-spec)
- [Skill definition](SKILL.md)
- [Stage Workstations](references/stages.md)
- [Discover And Clarify](references/discover.md)
- [Requirement Lifecycle And Role Ownership](references/lifecycle.md)
- [Specify The Requirement Baseline](references/specify.md)
- [Page, Prototype And Testability Contract](references/prototype.md)
- [Change, Traceability And Acceptance](references/change-acceptance.md)
- [Context, Composition And Agent Handoff](references/context.md)
- [Tool Adapters](references/tool-adapters.md)
- [Troubleshooting, Recovery And Anti-Patterns](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON, YAML, code snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local requirement artifacts, validation reports, checkpoint files, and handoff files when a task requires saved outputs.]

## Skill Version(s):

5.4.4 (source: ClawHub release evidence and SKILL.md heading)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
