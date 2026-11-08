## Description:

Uses Cue to organize public corporate, judicial, and administrative records into a sourced personal due-diligence brief covering business connections and current or historical risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Due-diligence and compliance professionals can use the skill to prepare a sourced background-check draft for IPO leadership reviews, major transactions, partner onboarding, or executive candidate checks. The skill documentation says to obtain consent where applicable and have a qualified professional review the draft before formal use.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: An API key may be exposed if pasted into chat, and the external runner is not bundled for inspection.

Mitigation: Configure the key through protected local configuration or a secret-entry interface, rotate any key already pasted into a conversation, and review and pin the runner before execution.

Risk: Personal research details and report links may disclose sensitive information.

Mitigation: Limit submitted details to what is needed, and consider who can access or receive a shared report link.

Risk: The workflow includes mandatory promotional guidance when the remaining credit balance is low.

Mitigation: Review the low-credit prompt and its purchase or referral options before presenting them to the user.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/panting09266-ai/skills/cue-person-background-check)
- [Cue runner project (listed in skill documentation)](https://github.com/sensedeal/cue-skills)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-person-background-check)
- [China Judgment Online](https://wenshu.court.gov.cn)
- [China Enforcement Information Disclosure](https://zxgk.court.gov.cn)
- [National Enterprise Credit Information Publicity System](https://www.gsxt.gov.cn)
- [Securities Association of China](https://www.sac.net.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown due-diligence brief with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft for professional review; includes public-source links and current or historical risk distinctions.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
