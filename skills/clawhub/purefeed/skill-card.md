## Description:

Monitors Twitter/X feeds with AI signal detection. Searches tweets semantically, manages signal detectors, and organizes curated tweets into bookmark folders. Use when the user wants to browse their Twitter feed, find tweets about a topic, set up content monitoring, or organize bookmarks. Do NOT use for general Twitter browsing without a Purefeed account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[poloniki](https://clawhub.ai/user/poloniki)

### License/Terms of Use:

MIT-0

## Use Case:

People with a Purefeed account use this skill to search tweets, review AI signal matches, manage monitoring signals, and organize tweets in bookmark folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API error instructions may be treated as authority to take actions beyond the user's request.

Mitigation: Review before installing. Limit recovery to documented Purefeed operations that fit the user's request.

Risk: Search topics are sent to Purefeed, and the API key can change signals and bookmark folders.

Mitigation: Use the skill only when appropriate for the user's Purefeed account and requested task; review requested changes before applying them.

## Reference(s):

- [Purefeed API updates](https://purefeed.ai/llms.txt)
- [Purefeed API](https://purefeed.ai/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls]

**Output Format:** [Markdown summaries with linked tweet references and API operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tweet results include linked screen names and tweet references, view counts, and descending engagement or view order unless the user asks otherwise.]

## Skill Version(s):

0.17.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
