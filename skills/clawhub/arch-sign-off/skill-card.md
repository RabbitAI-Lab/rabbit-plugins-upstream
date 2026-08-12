## Description:

Append the Arch Linux sign-off line `btw, i use arch ` to the bottom of articles in `ai-thoughts/docs/` unless the user explicitly opts out.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and writers use this skill to keep articles in `ai-thoughts/docs/` consistently marked with a specific Arch Linux sign-off line. It applies to English and Chinese article versions while respecting explicit user opt-outs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill adds a visible branding-style sign-off to every scoped article by default, including Chinese `-chn.md` versions.

Mitigation: Install only when that exact sign-off is desired, and review generated article diffs when branding or language choice matters.

Risk: The sign-off could be applied when a user expects an article to remain unmarked.

Mitigation: Give an explicit opt-out instruction when the sign-off should be skipped for a specific article or workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/arch-sign-off)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [Markdown file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Appends one exact sign-off line at the end of scoped article files and avoids duplicate sign-offs.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
