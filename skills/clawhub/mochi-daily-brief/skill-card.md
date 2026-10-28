## Description:

Create a cited Chinese or English personal news brief from public RSS/Atom feeds, filter by topic and calendar days, and save a local Markdown report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

External users can collect public AI and technology news for selected topics and calendar dates, then review a concise Chinese or English brief with dated source links saved in their workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feed servers receive request metadata, and the connected model processes collected evidence.

Mitigation: Use public feeds and avoid including private information in feed requests; check original links before relying on important claims.

Risk: Saved reports remain in the workspace until removed.

Mitigation: Review and delete local reports when they are no longer needed.

## Reference(s):

- [MochiLab](https://mochilab.bz)
- [Options and sources](references/options.md)
- [OpenAI News RSS feed](https://openai.com/news/rss.xml)
- [Google AI RSS feed](https://blog.google/technology/ai/rss/)
- [GitHub Changelog feed](https://github.blog/changelog/feed/)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Concise Markdown brief with dated, cited source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved as a local workspace report and shown to the user]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
