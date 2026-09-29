## Description:

Creates a pre-deployment shutdown-planning card for an agent and checks that its stop conditions, access-revocation steps, owner, and recovery conditions are present.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); All rights reserved (documentation and theory)

## Use Case:

Developers and operators use this skill before deploying an agent to document when to stop it, how to revoke its access, who is responsible, and when it may restart. A local check flags missing card fields; it does not stop an agent automatically.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A complete planning card could be mistaken for an automatic emergency stop.

Mitigation: Treat the card and completeness check as planning aids; confirm shutdown actions and decision-makers separately before deployment.

Risk: Card fields or saved files could expose sensitive credentials or information.

Mitigation: Do not enter secrets in card fields, and select the output path deliberately.

Risk: Readers may overlook the Chinese-language instructions or differing license scopes.

Mitigation: Review the instructions and layered code/documentation terms before installing or redistributing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-kill-switch)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Human-readable card or JSON shutdown-planning card and validation result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional user-selected JSON output file; a missing required field produces a nonzero check result.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; bundled SKILL.md says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
