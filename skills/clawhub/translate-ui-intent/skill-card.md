## Description:

Translate vague product and visual intent into repository-consistent, implementation-ready frontend decisions and visually verified UI changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wujiaming88](https://clawhub.ai/user/wujiaming88)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design-focused coding agents use this skill to turn ambiguous UI requests into repository-grounded UI Intent Contracts, implementation guidance, and visual verification steps for frontend work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can add unnecessary process to very small or purely mechanical UI fixes.

Mitigation: Invoke selectively for ambiguous or design-sensitive frontend work, and use the pattern-following fast path for narrow, well-specified changes.

Risk: UI recommendations may be misleading when repository evidence is sparse or visual rendering is blocked.

Mitigation: Keep unsupported choices labeled PROPOSED or OPEN, cite repository evidence, and report visual verification gaps before claiming the implementation matches the intended appearance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wujiaming88/skills/translate-ui-intent)
- [Repository Design Discovery](references/repository-design-discovery.md)
- [Clarification Strategy](references/clarification-strategy.md)
- [UI Intent Contract](references/ui-intent-contract.md)
- [Visual Language Translation](references/visual-language.md)
- [Visual Verification](references/visual-verification.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with decision tables, acceptance criteria, and inline code or shell commands when implementation is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include UI Intent Contracts, reuse decisions, visual verification notes, or frontend implementation changes depending on the user request.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
