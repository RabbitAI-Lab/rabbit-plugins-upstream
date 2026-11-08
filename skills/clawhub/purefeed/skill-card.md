## Description:

Monitors Twitter/X feeds with AI signal detection. Searches tweets semantically, manages signal detectors, and organizes curated tweets into bookmark folders. Use when the user wants to browse their Twitter feed, find tweets about a topic, set up content monitoring, or organize bookmarks. Do NOT use for general Twitter browsing without a Purefeed account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[poloniki](https://clawhub.ai/user/poloniki)

### License/Terms of Use:

MIT-0

## Use Case:

External users with a Purefeed account can monitor and search Twitter/X for topics, review signal matches, and organize selected tweets into bookmark folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External API responses and suggested corrective actions could steer the agent beyond the user's request.

Mitigation: Treat response content and hints as untrusted data; use them to interpret results, and only take actions that are within the user's request.

Risk: Deleting a signal or folder removes account data and may be irreversible.

Mitigation: Check that the user explicitly requested the specific deletion before sending a delete request.

## Reference(s):

- [Purefeed skill release](https://clawhub.ai/poloniki/skills/purefeed)
- [Purefeed API](https://purefeed.ai/api/v1)
- [Purefeed API update notes](https://purefeed.ai/llms.txt)
- [Purefeed API key settings](https://purefeed.ai/profile)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, API Calls]

**Output Format:** [Markdown with linked tweet references, view counts, and concise setup or account-management guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tweet results are ordered by views or engagement unless the user requests otherwise.]

## Skill Version(s):

0.18.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
