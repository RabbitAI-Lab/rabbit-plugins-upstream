## Description:

CCPA Audit helps agents preview CCPA/CPRA audit items, collect compliance responses, submit scored answers to compliancehub.cn, and generate local text, JSON, or HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External compliance teams and developers use this skill to run a bilingual CCPA/CPRA self-audit, preview audit items without sending answers, and generate a scored report when they choose cloud scoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored audit answers are sent to compliancehub.cn.

Mitigation: Use preview mode when answers should stay on-machine, and run scored reports only after confirming that cloud scoring is acceptable.

Risk: The skill can use an API key and an anonymous trial identifier stored under ~/.config/compliancehub.

Mitigation: On shared systems, prefer COMPLIANCEHUB_API_KEY over a saved key file and delete the key file or ccpa-audit.anon_id when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/ccpa-audit)
- [ComplianceHub account center](https://compliancehub.cn/account.html?skill=ccpa-audit)
- [ComplianceHub cloud endpoint](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [text, json, html, guidance]

**Output Format:** [Plain text, JSON, or HTML audit preview and report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are generated locally after preview or cloud scoring; scored runs send answers to compliancehub.cn.]

## Skill Version(s):

2.1.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
