## Description:

Checks whether a known YouTube video is labeled Creative Commons in FlashData; it requires a FlashData API key and paid Credits and does not establish training or reuse permission.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and rights reviewers use it to inspect a known YouTube video's Creative Commons license label and record the result as one input to a separate rights review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Data queries use paid FlashData Credits.

Mitigation: Check pricing or request a free quote before a query, and run only the requests needed for the task.

Risk: A Creative Commons label match does not verify ownership or grant training, download, or republication rights.

Mitigation: Treat the classification as one input to a rights review; inspect the actual license and intended use before reuse.

Risk: The security review was partial and has medium confidence.

Mitigation: Review the skill and its unresolved local references before installation.

## Reference(s):

- [FlashData YouTube Trainability documentation](https://flashdata.dev/docs/sources/youtube_trainability?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_trainability-task)
- [FlashData pricing](https://flashdata.dev/pricing?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_trainability-task)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON license-label classification with interpretation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The classification is an observation of license metadata, not legal clearance or authorization to train, download, or republish.]

## Skill Version(s):

1.0.2 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
