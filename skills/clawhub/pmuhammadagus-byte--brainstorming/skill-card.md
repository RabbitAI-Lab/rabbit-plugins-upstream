## Description:

Helps agents turn early ideas into approved designs and written specifications through staged collaborative dialogue before implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product builders, and agents use this skill to explore project context, clarify requirements, compare approaches, present design sections for approval, write a design specification, and transition to implementation planning only after user review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional visual companion opens a local browser server and includes a session key in the local URL.

Mitigation: Keep the default localhost binding unless network exposure is intentional, share only the complete keyed local URL with the user, and stop the companion when done.

Risk: Visual companion sessions can store mockups and click choices in a project session directory.

Mitigation: Add .superpowers/ to .gitignore when using project persistence and avoid placing secrets or unnecessary personal data in mockups.

Risk: Brainstorming outputs can preserve incorrect assumptions in a design specification before implementation starts.

Mitigation: Use the skill's clarification, approval, spec self-review, and user review gates before transitioning to implementation planning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/brainstorming)
- [Spec document reviewer prompt](artifact/spec-document-reviewer-prompt.md)
- [Visual companion guide](artifact/visual-companion.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Code]

**Output Format:** [Conversational text and Markdown documents, with optional HTML fragments and shell commands for the visual companion.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create design specs under docs/superpowers/specs/ and local visual companion session files when the user approves visual support.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
