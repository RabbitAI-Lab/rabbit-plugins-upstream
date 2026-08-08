## Description:

Helps agents analyze Xiaohongshu/XHS hot-list and related popular-note signals from SocialDataX into actionable content topic ideas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and marketing or content teams use this skill to inspect current Xiaohongshu/XHS hot-search topics, sample popular notes for selected keywords, and turn those signals into topic candidates, title hooks, content angles, and next-step recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocialDataX API key and sends XHS hot-list or search requests to SocialDataX.

Mitigation: Install and run it only when the user is comfortable providing SOCIALDATAX_API_KEY and using SocialDataX for public XHS data retrieval.

Risk: Returned full note URLs may include opaque query parameters.

Mitigation: Treat returned note URLs as shareable result data and preserve them exactly only where needed for references, display, storage, or forwarding.

Risk: Topic recommendations may be incomplete because they are based only on the current hot list and returned page range.

Mitigation: Present findings as directional selection guidance rather than full-platform coverage or guaranteed traffic outcomes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-hot-topic-selection)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown analysis with hot-list signals, topic candidates, note samples, title hooks, content angles, and next-step recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses current hot-list data and returned search pages only; preserves returned full note_url values including opaque query parameters.]

## Skill Version(s):

0.1.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
