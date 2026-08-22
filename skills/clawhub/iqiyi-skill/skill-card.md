## Description:

Search, recommend, inspect, and play iQiyi video content through no-login iQIYI content operations, qips playback deeplinks, and H5 or client-install fallbacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robinkam](https://clawhub.ai/user/robinkam)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search iQiyi videos, request recommendations, inspect video or star details, generate playback deeplinks or commands, and fall back to H5 playback or install links without account login.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search and recommendation requests can be sent to iQiyi's mesh API.

Mitigation: Use the skill for intentional iQiyi content lookups and avoid entering sensitive query text.

Risk: qips deeplinks can open or control the iQiyi client when playback or navigation is requested.

Mitigation: Review the target content and action before launch, and use only deeplinks generated or validated by the skill.

Risk: A caller-supplied Authorization header may be sent to the iQiyi API for history or favorites behavior.

Mitigation: Do not provide Authorization unless that transfer is intended; the skill does not create, store, or refresh login state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/robinkam/skills/iqiyi-skill)
- [Operation semantics](references/operations.md)
- [SOP](references/sop.md)
- [qips API usage](references/qips/api-usage.md)
- [qips channel table](references/qips/channel-table.md)
- [qips launch checklist](references/qips/launch-checklist.md)
- [qips vtype recipes](references/qips/vtype-recipes.md)
- [qips capabilities](docs/qips-capabilities.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON snippets, qips deeplinks, shell commands, and JavaScript examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include network-backed iQiyi results, locally generated qips deeplinks, H5 playback URLs, or client install links.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence; artifact metadata/package.json: 0.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
