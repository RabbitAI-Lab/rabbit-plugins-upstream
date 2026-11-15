## Description:

Provides Xiaohongshu (XHS/RedNote) trend and note search, note details, comment analysis, creator profiles, and creator post lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

People researching Xiaohongshu content and creators can use the skill to find trending topics and notes, inspect note details and comments, and look up creator profiles and posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious because it repeatedly runs an unpinned, mutable CLI package; the scan also notes potential credential and privacy concerns.

Mitigation: Use a reviewed, fixed CLI version if available, and consider whether search terms or share text are sensitive before sending them to SocialDataX.

Risk: The security scan is partial and could not resolve three local references, so its evidence is incomplete.

Mitigation: Review the skill and its referenced components before installing or using it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Markdown]

**Output Format:** [Structured JSON data with agent-readable summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Xiaohongshu search and lookup results; the service may return partial results.]

## Skill Version(s):

0.1.27 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
