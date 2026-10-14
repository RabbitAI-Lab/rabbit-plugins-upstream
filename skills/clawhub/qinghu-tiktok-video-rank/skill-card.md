## Description:

Helps users retrieve and interpret TikTok popular-video and commerce-video rankings by region, category, and daily, weekly, or monthly period.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers, merchants, and analysts use the skill to find trending TikTok videos and compare video performance within a selected region, category, and reporting period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can install or upgrade Node/npm packages and change the host PATH.

Mitigation: Review installation steps before use; prefer an isolated environment with qhkit preinstalled.

Risk: Setup requires an API credential on the host.

Mitigation: Supply credentials through normal secret management rather than exposing a token in commands or chat.

Risk: Ranking queries may consume paid Qinghu credits.

Mitigation: Check the estimated cost before paid calls and report the credits consumed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-tiktok-video-rank)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise ranking summaries in Markdown; file export for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results identify the region, reporting period, and sample size; paid calls report Qinghu credit usage.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
