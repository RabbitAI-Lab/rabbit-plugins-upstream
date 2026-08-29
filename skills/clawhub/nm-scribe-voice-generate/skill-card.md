## Description:

Generates text in a learned writing voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, developers, and agent users use this skill to draft prose from local voice profiles, selected registers, and user-provided source material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice profiles and source material may contain sensitive writing samples or private draft content.

Mitigation: Keep voice profiles free of material that should not be sent into generation context, and review source material before use.

Risk: Silent cleanup can change generated wording before the user sees the draft.

Mitigation: Treat cleanup as draft editing, not an auditable final rewrite, and review the output before publishing or reuse.

Risk: The skill can produce prose that closely follows a learned writing voice.

Mitigation: Use only authorized voice profiles and review generated text for appropriate attribution, consent, and context.

Risk: Broad trigger terms can cause the skill to be selected for writing tasks where voice generation is not intended.

Mitigation: Review configured triggers and invoke the skill only when the user wants text drafted from a specific voice profile.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-voice-generate)
- [Project homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scribe)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with generated prose and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May apply draft cleanup for banned phrases and punctuation before optional review.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
