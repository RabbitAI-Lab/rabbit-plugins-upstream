## Description:

疗愈性影视推荐。根据用户描述的情绪困扰或现实困境，推荐能提供方法、理解或希望的电影或剧集。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangdaozhenren](https://clawhub.ai/user/wangdaozhenren)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this Chinese-language skill to receive movie or TV recommendations matched to emotional distress or life situations such as anxiety, loneliness, burnout, grief, work, school, family, relationship, health, or life-transition concerns. The skill is for supportive media discovery, not medical diagnosis, psychotherapy, crisis care, book recommendations, or pirated viewing sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake supportive film and TV recommendations for medical, psychiatric, or crisis care.

Mitigation: Present recommendations as auxiliary emotional support only; do not diagnose or provide treatment advice, and direct urgent or persistent distress to emergency, crisis, or professional support resources.

Risk: A user in acute self-harm, suicide, violence, or severe loss-of-control distress could receive ordinary recommendations instead of safety support.

Mitigation: Stop the recommendation flow when crisis signals appear, respond with care, and provide emergency, hotline, local support, and trusted-person help paths.

Risk: Real-time expansion beyond the seed library could produce inaccurate film titles, years, or availability assumptions.

Mitigation: Verify movie and series titles and years before recommending expanded items, and avoid providing pirated viewing resources.

## Reference(s):

- [Skill page](https://clawhub.ai/wangdaozhenren/skills/movie-therapy)
- [危机识别与处置](references/crisis.md)
- [种子影库（影愈）](references/library.md)
- [困扰分类学（书愈 / 影愈共用）](references/taxonomy.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown recommendation response in Chinese]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include matched concern categories, intensity-aware recommendations, brief rationale, and crisis or professional-support guidance when applicable.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
