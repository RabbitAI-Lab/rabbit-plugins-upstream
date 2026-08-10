## Description:

Verifies browser profile isolation by checking timezone and IP alignment, WebRTC exposure, stable canvas and WebGL fingerprints, and separation of personas, cookies, and addresses across authorized accounts or test identities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antibrow](https://clawhub.ai/user/antibrow)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA teams, and anti-fraud engineers use this skill to audit browser profile isolation for accounts or test identities they are authorized to operate, including choosing detection suites and identifying isolation failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use on accounts or identities without authorization could violate platform terms, law, or security boundaries.

Mitigation: Use only for accounts, client accounts, QA fixtures, or anti-fraud tests that the operator is authorized to run, and review applicable platform terms before use.

Risk: Browser tooling involved in the workflow may handle cookies, login state, proxy credentials, and an API key, and may contact a license service.

Mitigation: Review those data flows before using sensitive accounts, keep credentials in environment or approved secret storage, and audit network behavior where needed.

Risk: A clean browser isolation check does not rule out account linkage through payment instruments, contact details, activity patterns, identity verification, or platform policy decisions.

Mitigation: Treat passing results as evidence about the browser layer only and review non-browser correlation factors separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/antibrow/skills/multi-account-isolation)
- [Publisher profile](https://clawhub.ai/user/antibrow)
- [BrowserLeaks WebRTC](https://browserleaks.com/webrtc)
- [CreepJS](https://abrahamjuliot.github.io/creepjs/)
- [Whoer](https://whoer.net)
- [PixelScan](https://pixelscan.net)
- [LiarJS](https://liarjs.dev)
- [Antibrow](https://antibrow.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with TypeScript, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes checklists and risk notes; no automatic actions.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
