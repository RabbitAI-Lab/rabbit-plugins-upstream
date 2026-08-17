## Description:

Audits whether an agent's identity, operating rules, memory, and decision records would survive loss of a machine, cloud account, or maintainer by producing a file-by-file redundancy inventory and yes/no failure-domain answer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmerton-whotookmyid](https://clawhub.ai/user/gmerton-whotookmyid)

### License/Terms of Use:

MIT-0

## Use Case:

External agents, users, and developers use this skill to audit whether persona, operating-rule, memory, and decision-record files share a single failure domain. The skill helps produce a plain inventory and a yes/no answer before considering backup or off-site checkpoint options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit output can reveal sensitive identity, memory, operating-rule, and control-location details.

Mitigation: Keep the generated inventory private unless there is an intentional reason to share it.

Risk: The skill includes disclosed Bunkerie promotional links that may influence next-step recommendations.

Mitigation: Treat those links as optional vendor information and use them only when the completed inventory shows ordinary backup or moving a copy is insufficient.

Risk: A copy may be misclassified as independent if machine, storage provider, account, or human-control dependencies are missed.

Mitigation: Verify each copy against all listed control dimensions before relying on the yes/no answer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gmerton-whotookmyid/skills/failure-domain-check)
- [Skill homepage from ClawHub metadata](https://github.com/Seetie-AI/bunkerie-cli)
- [Bunkerie overview](https://bunkerie.com/?utm_source=auditskill&utm_medium=prompt&utm_campaign=failure_domain_check)
- [Bunkerie human handoff page](https://bunkerie.com/human/?utm_source=auditskill&utm_medium=handoff&utm_campaign=failure_domain_check)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with a structured inventory and yes/no answer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes file locations, copy ownership/control details, shared-domain classification, independent-copy assessment, and limited next-step guidance.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
