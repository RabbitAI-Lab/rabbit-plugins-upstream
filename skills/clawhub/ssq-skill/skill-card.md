## Description:

Generates responsible Shuangseqiu lottery analysis, randomness education, anti-fraud guidance, dan-tuo structure explanations, and draw checks while clearly stating that number-picking methods do not improve winning odds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to generate entertainment-only Shuangseqiu lottery reports, understand lottery randomness, check draw outcomes, compare claims from number-picking services, and receive responsible-play reminders. Reviewers and operators can also use its documented health checks and methodology notes to evaluate whether the release preserves its no-edge and anti-fraud posture.

### Deployment Geography for Use:

Global, with content focused on China's Shuangseqiu lottery.

## Known Risks and Mitigations:

Risk: The skill fetches public online lottery data and includes scraping/reporting behavior.

Mitigation: Review the data-fetching behavior before installation and use the documented offline mode when network access is not acceptable.

Risk: The skill writes local reports, caches, and supporting files.

Mitigation: Run it from a dedicated working directory and review generated files before relying on them.

Risk: The evidence notes Windows scheduling and local automation guidance, including possible unattended operation.

Mitigation: Avoid administrator or SYSTEM scheduled-task setup unless unattended local operation is intentional and reviewed.

Risk: Lottery-focused recommendations can be misunderstood as financial or predictive guidance.

Mitigation: Keep the no-guarantee, no-positive-edge, budget-limit, and responsible-play warnings visible in user-facing outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/ssq-skill)
- [README](artifact/README.md)
- [Responsible play guide](artifact/responsible_play_2026.md)
- [Methodology](artifact/methodology.md)
- [Operations](artifact/operations.md)
- [FAQ](artifact/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown-style guidance with inline shell commands; local runs may produce HTML reports and JSON data files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Python 3 standard-library workflow; may fetch public lottery data and write local reports or caches.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
