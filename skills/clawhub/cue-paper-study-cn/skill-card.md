## Description:

Turns supplied papers into a five-part, page-anchored study card with reproducibility gaps, source-grounded citation notes, a user-owned literature-review outline, and items for human verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, students, and other readers use the skill to turn supplied papers into a traceable study card, check what information is missing for reproduction, and organize source-grounded material for their own literature review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional online setup could send the API key to an unapproved server.

Mitigation: Keep credentials unset until destinations are validated and unsafe redirects are rejected; use the manual-card workflow and local checker meanwhile.

Risk: External parsing may send unpublished or otherwise sensitive papers to Cue.

Mitigation: Explicitly approve which documents may be sent before enabling external parsing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-paper-study-cn)
- [Cue service](https://cuecue.cn)
- [Cue API key guidance](https://cuecue.cn/hub/api-key)
- [Cue service catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, text, guidance]

**Output Format:** [Five-section Markdown study card]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses page or section anchors where available; marks missing information, limits citation claims to material actually found, and leaves the user's argument slots and academic judgments to the user.]

## Skill Version(s):

0.2.27 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
