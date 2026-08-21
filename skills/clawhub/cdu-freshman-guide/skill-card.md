## Description:

为成都大学新生提供选课、走读、住宿、医保、租房、就业等高频问题的一站式问答，并通过来源、时效提示和官方渠道核实建议降低误导风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[century0327](https://clawhub.ai/user/century0327)

### License/Terms of Use:

MIT-0

## Use Case:

External users, especially Chengdu University freshmen and student supporters, use this skill to ask campus-life and administrative questions and receive practical answers with source, timeliness, and verification prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The knowledge base includes unofficial campus experience and time-sensitive school information that may become outdated or conflict with current policy.

Mitigation: Treat important dates, fees, policies, account procedures, and student-status matters as leads to verify through official Chengdu University channels before acting.

Risk: The package republishes predictable default-password patterns, which can be sensitive if repeated without context.

Mitigation: Use password guidance only to help students reach official systems, and remind users not to share credentials, identifiers, verification codes, or passwords.

Risk: Maintenance scripts can expose names if used with raw chat exports.

Mitigation: Do not run maintenance scripts on private chat data unless name-list logging and reporting behavior has been removed and the input has been appropriately desensitized.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/century0327/skills/cdu-freshman-guide)
- [README](artifact/README.md)
- [Design Notes](artifact/DESIGN.md)
- [Example Q&A](artifact/examples/example-qa.md)
- [成都大学官网](https://www.cdu.edu.cn)
- [成都大学招生网](https://zhaosheng.cdu.edu.cn)
- [成都大学教务处](https://jw.cdu.edu.cn)
- [成都大学学生处](https://xsc.cdu.edu.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational Markdown with source, timeliness, cross-check, and user self-review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers are scoped to Chengdu University topics and should avoid personal data, gray-market services, and unsupported certainty.]

## Skill Version(s):

1.4.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
