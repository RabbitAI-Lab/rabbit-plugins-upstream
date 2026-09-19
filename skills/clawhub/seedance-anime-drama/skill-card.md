## Description:

Turns novel or script excerpts into anime-style storyboard clips by using Ofox image generation for character opening frames and Ofox video generation for each approved shot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn story excerpts, manga-drama scenes, or chapter passages into anime-style video shots with a consistent primary character. The skill guides the agent through brief questions, prompt construction, cost approvals, Ofox image generation for character frames, and Ofox video generation for the final shots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and images used for generation are sent to Ofox.

Mitigation: Use the skill only with content that is acceptable to share with Ofox, and avoid private or sensitive prompts and images unless the user has approved that exposure.

Risk: The fallback dependency path can lead to broad global installation of Ofox skills.

Mitigation: Install only the two required core skills for the active agent and review them explicitly before use.

Risk: The public image URL identity-reference route can expose private or sensitive images.

Mitigation: Use public image URLs only when access to the hosted image is controlled and the user understands the privacy tradeoff.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-anime-drama)
- [Skill homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-anime-drama)
- [Ofox application and API keys](https://app.ofox.ai)
- [Ofox model catalog](https://api.ofox.ai/v1/models/catalog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt text, approval tables, and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY plus curl and jq; generated images and videos are produced through the dependent Ofox core skills after explicit user approval.]

## Skill Version(s):

1.13.1 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
