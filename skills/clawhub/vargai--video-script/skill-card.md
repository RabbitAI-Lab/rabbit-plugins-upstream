## Description:

Turns a video brief and fact file into a timed script table with spoken lines, on-screen text, visuals, sound, three hooks, and checks for pacing and unsupported claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and video producers use this skill to draft ads, UGC, Shorts, YouTube videos, demos, reviews, explainers, and short drama before production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Model-based judging may share drafts and supplied facts with the chosen provider.

Mitigation: Choose a provider whose data terms suit the project, omit confidential material, and keep project logs private.

Risk: Unsupported claims or invented facts in a script could mislead viewers.

Mitigation: Use facts.md as the source for claims, cite facts in the script’s Sources section, and run the provided checker.

Risk: Installing unreviewed plugin content or changed skill files may add unexpected behavior.

Mitigation: Install only the reviewed skill release, use a reviewed repository snapshot, and inspect changes to the installed skill and checker.

## Reference(s):

- [Skill instructions](artifact/SKILL.md)
- [Source bibliography](artifact/references/sources.md)
- [Video model duration reference](https://varg.ai/models/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown script with a timed table, three hooks, and source notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A script.md structure with brief metadata and one row per beat.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
