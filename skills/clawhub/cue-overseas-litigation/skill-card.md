## Description:

境外诉讼案例库围绕主题检索主要法域的公开判例与监管公告，归纳诉因、判决倾向和对中国主体的合规启示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, compliance, and cross-border business users use this skill to request public-source overseas litigation and regulatory research across jurisdictions. It produces a Chinese report with case lists, claim analysis, outcome tendencies, penalties or damages, compliance implications, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends legal research prompts to Cue and may involve confidential or sensitive matters.

Mitigation: Avoid submitting confidential legal matters unless the user is comfortable sending them to Cue.

Risk: The skill relies on an external runner source and service availability.

Mitigation: Install only from trusted Cue sources, run the documented health checks before use, and review output source links.

Risk: The API key may be stored in plaintext configuration.

Mitigation: Protect the key with restrictive file permissions or a secret store and rotate it if exposed.

Risk: Raw user text interpolated through a shell command can create command-handling risk.

Mitigation: Pass user queries as arguments without unsafe shell interpolation.

Risk: The workflow consumes Cue credits and may steer users toward payment or referral links.

Mitigation: Tell users about credit use before running and distinguish operational errors from payment or referral guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-overseas-litigation)
- [Cue platform](https://cuecue.cn)
- [Cue playbook](https://cuecue.cn/playbook)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown report with source links, a Cue report URL when available, and a local report path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report should preserve original case names and legal provisions where relevant and should not be treated as legal advice.]

## Skill Version(s):

1.2.6 (source: server release metadata; artifact frontmatter says 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
