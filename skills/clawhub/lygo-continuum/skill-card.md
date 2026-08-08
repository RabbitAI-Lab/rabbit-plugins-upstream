## Description:

LYGO Continuum creates falsifiable work capsules that seal checkable claims, re-verify them across sessions, detect drift, and produce portable handoff evidence for humans and agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Developers, engineers, and agent operators use this skill to record what work was completed as local claims, then verify those claims later and hand off a portable capsule to another human or agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Claims or capsules can direct verification at files outside the intended project boundary.

Mitigation: Review claim and capsule paths before use and pass an explicit --base for the intended project.

Risk: Handoff packs, task summaries, and claims can expose sensitive paths or secret-adjacent details if shared.

Mitigation: Avoid putting secrets in claims or handoff text, and strip private paths before publishing or sharing externally.

Risk: The browser portal is a remote site, so sensitive files require extra care even when hashing is described as client-side.

Mitigation: Avoid the portal for sensitive files unless the operator independently trusts the site; use local verification for sensitive work.

## Reference(s):

- [LYGO Continuum ClawHub page](https://clawhub.ai/deepseekoracle/skills/lygo-continuum)
- [Project homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-continuum)
- [Browser portal](https://chatagent.ca/lygo-continuum.html)
- [Security notes](references/SECURITY.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [JSON capsules and reports, Markdown handoff packs, HTML witness cards, and command-line text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local filesystem inputs are selected by the operator; the evidence states no network or subprocess use.]

## Skill Version(s):

1.0.0 (source: frontmatter, claw.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
