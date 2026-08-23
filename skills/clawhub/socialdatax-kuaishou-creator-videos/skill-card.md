## Description:

用于快手达人数据、快手达人作品、作品列表、近期发布、内容调研和创作者内容分析。覆盖 Kuaishou / Kwai creator works，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve Kuaishou creator work lists for recent publishing review, creator benchmarking, content research, and account tracking through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SOCIALDATAX_API_KEY and runs the socialdatax-skills npm CLI package.

Mitigation: Install and run it only when SocialDataX access is intended, and provide the API key through the runtime environment rather than storing it in skill files.

Risk: Using --all or broad multi-page options can consume SocialDataX API credits.

Mitigation: Prefer bounded --pages or --max-items values for exploratory runs and monitor usage before expanding collection.

## Reference(s):

- [SocialDataX AI access and API key management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-creator-videos)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON API result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY plus node/npm; multi-page and --all usage can consume API credits.]

## Skill Version(s):

0.1.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
