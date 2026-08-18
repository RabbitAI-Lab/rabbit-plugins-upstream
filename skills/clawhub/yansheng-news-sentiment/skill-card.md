## Description:

A classroom demonstration skill that fetches public finance-page text for stock codes and produces simplified, rule-based news sentiment output.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and learners use this skill to demonstrate how an agent can run a simple stock-news sentiment workflow over public finance-page data. It is intended for teaching and exploration, not investment analysis or real-world sentiment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake formulaic keyword scoring for robust NLP sentiment analysis or investment guidance.

Mitigation: Present outputs as classroom-demo estimates only and require human review before using them in financial or operational decisions.

Risk: Running the script with stock codes contacts Sina Finance and depends on public page availability.

Mitigation: Review network access expectations before execution and use the built-in fallback behavior when live page access is unavailable or unsuitable.

## Reference(s):

- [Sina Finance stock page data source](https://finance.sina.com.cn/realstock/company/{code}/nc.shtml)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON sentiment report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs article counts, positive/neutral/negative distribution, sentiment score, and sentiment label; values are formulaic teaching-demo estimates.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
