## Description:

Johnny activates a persistent design-dialog persona that acts as a virtual second designer, challenging product and UX thinking in short conversational replies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fiodor-po](https://clawhub.ai/user/fiodor-po)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, product teams, and design-minded developers use this skill to turn an agent thread into an ongoing design critique and UX consultation dialog. It helps sharpen design arguments, surface weak spots, and answer pattern or industry-practice questions with cited sources when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoking the persona changes the style of the whole thread until the user exits the mode.

Mitigation: Invoke Johnny deliberately and use explicit wording to exit or switch away when the design-dialog posture is no longer wanted.

Risk: Saved notes may be placed in the wrong destination if the request is ambiguous.

Mitigation: Use explicit wording for note saves, including the intended destination when it matters; otherwise accept the skill's save prompt only after checking it.

## Reference(s):

- [Claude Code skills documentation](https://code.claude.com/docs/en/skills)
- [ClawHub skill page](https://clawhub.ai/fiodor-po/skills/johnny)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Short conversational text, with Markdown links or citations when factual sources are used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code is produced by the skill; note-saving is limited to explicit user approval or direct save commands.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
