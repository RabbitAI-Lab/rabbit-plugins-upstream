## Description:

Uses 550W to remove video subtitles, optionally remove audio before subtitle removal, remove short-video and image watermarks, and query task status or account credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinehu](https://clawhub.ai/user/sunshinehu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to route media cleanup requests to 550W actions for subtitle removal, optional audio removal, watermark removal, task tracking, and credit checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files, remote URLs, and account credentials are used with the 550W service.

Mitigation: Install only if the user trusts 550W with the provided media and credentials; avoid sensitive local file paths and private or internal URLs.

Risk: Successful operations can consume account credits, and duplicate submissions may be charged separately.

Mitigation: Confirm batch scope and costs before paid operations; after uncertain timeouts, query existing tasks instead of submitting duplicates.

## Reference(s):

- [API contract](artifact/references/api-contract.md)
- [ClawHub skill page](https://clawhub.ai/sunshinehu/skills/550w-ai-subtitle-remover)
- [550W service portal](https://qzm.550wai.cn)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON action responses and concise user-facing text with result URLs, task IDs, statuses, credit data, or actionable error messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one request at a time, avoids repeating full API keys, and may return processing states that require later task-detail queries.]

## Skill Version(s):

1.2.0 (source: server release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
