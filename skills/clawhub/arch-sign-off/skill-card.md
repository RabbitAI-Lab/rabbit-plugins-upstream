## Description:

Append the Arch Linux sign-off line `btw, i use arch \uf303` to the very bottom of an article in ai-thoughts/docs/ (EN or ZH), unless the user explicitly says not to.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and writing agents use this skill to consistently append a specific Arch Linux sign-off to English and Chinese article files under ai-thoughts/docs/ while avoiding duplicates and respecting explicit opt-outs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The standing default can add the sign-off to every ai-thoughts/docs/ article, which may conflict with editorial approval or publication-policy requirements.

Mitigation: Install only where this default is desired, explicitly opt out when needed, and review article endings before publication.

Risk: The sign-off is always English and includes the Arch glyph, which may not match localized editorial standards or render correctly in all publication environments.

Mitigation: Preview final rendered articles and revise or remove the sign-off when localization or font compatibility requires it.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown file edits and concise status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Appends a single final sign-off line, preserves the Arch glyph, skips non-article files, and leaves files unchanged when the sign-off is already present or the user opts out.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
