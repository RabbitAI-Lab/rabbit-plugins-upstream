## Description:

Detect ad copy fatigue and auto-suggest micro-pivot refreshes by analyzing CTR/CPC degradation across Facebook, Google, and LinkedIn campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ncreighton](https://clawhub.ai/user/ncreighton)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, growth operators, and developers use this skill to monitor ad campaign performance across Facebook, Google Ads, and LinkedIn, identify copy fatigue, and generate refresh suggestions or alerting setup guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad ad-platform and OpenAI credentials may expose sensitive campaign data or allow more access than the user intends.

Mitigation: Use the narrowest possible scopes, prefer OAuth where available, and confirm where credentials, campaign metrics, generated copy, alerts, and model-bound data are stored or logged.

Risk: Automated A/B test setup or scheduled actions can create business-impacting campaign changes.

Mitigation: Avoid campaign-mutation permissions unless automated launch is intended, require human approval for campaign changes, and define rollback or disable steps before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ncreighton/skills/ad-copy-fatigue-detector-refresher)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ad-platform performance summaries, fatigue risk scores, copy refresh suggestions, alert setup, and A/B test setup guidance.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
