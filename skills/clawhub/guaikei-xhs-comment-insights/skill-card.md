## Description:

Collects structured public Xiaohongshu note, author, post, and comment data so agents can support competitor monitoring, content research, KOL screening, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, content operators, and analysts use this skill to retrieve public Xiaohongshu search results, note details, creator posts, and comments for downstream analysis and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries send Xiaohongshu keywords, note or profile URLs, requested limits, and token-backed requests to guaikei.com.

Mitigation: Use only when the user is comfortable with that third-party data flow and has an authorized GUAIKEI_API_TOKEN.

Risk: The skill can save complete result data locally, including competitor research and public comments.

Mitigation: Review and delete generated logs when working on shared machines or with sensitive internal research.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-comment-insights)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance, files]

**Output Format:** [JSON from command-line scripts, with human-facing guidance for routing, parameters, and failure handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require Node.js 16.14.0+ and a GUAIKEI_API_TOKEN; complete results may be saved under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
