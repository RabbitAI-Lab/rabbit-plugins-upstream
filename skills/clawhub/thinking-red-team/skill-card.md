## Description:

For authorized security review of code, auth, or APIs you control, model the attacker, map the attack surface, and report only findings with a reproducible exploit path and verified mitigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to conduct authorized adversarial reviews of code, authentication, APIs, data handling, and infrastructure. It keeps reports focused on reproducible exploit paths, realized impact, concrete mitigations, and re-test steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security testing can affect real systems if the user chooses an unsafe scope or lacks authorization.

Mitigation: Use only on systems the user owns or has written permission to test, and confirm target, allowed scope, out-of-scope assets, success conditions, and stop rules before probing.

Risk: Scanner output or speculative best-practice notes could be mistaken for validated findings.

Mitigation: Keep only findings with an entry point, ordered reproduction steps, realized impact, and a mitigation re-test.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tjboudreaux/skills/thinking-red-team)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown security review report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes target and scope, threat model, attack surface, exploit-backed findings, mitigations, re-test steps, and summary counts.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
