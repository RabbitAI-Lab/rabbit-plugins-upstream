## Description:

Provides assistant-driven commands for checking Fellow Aiden brewer status, viewing device details, listing schedules, and listing or looking up brew profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mogglemoss](https://clawhub.ai/user/mogglemoss)

### License/Terms of Use:

MIT

## Use Case:

External users with a Fellow Aiden brewer can ask an agent to inspect brewer status, retrieve device details, list schedules, and find brew profiles. The release evidence says the shipped code is mostly read-only despite documentation that advertises profile creation, deletion, sharing, import, and schedule creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Fellow account credentials and sends them to a hard-coded AWS API Gateway endpoint.

Mitigation: Install only after verifying who operates the endpoint and after accepting the credential exposure; consider using dedicated credentials and rotating them if the skill is removed.

Risk: The documentation advertises create, delete, share, import, and schedule creation features that the bundled code does not implement.

Mitigation: Treat this release as mostly read-only and rely only on implemented commands until the code and documentation are reconciled.

Risk: The security guidance flags an unpinned unused dependency before routine use.

Mitigation: Remove the unused dependency or pin and review it before deploying the skill in a regular workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mogglemoss/skills/fellow-aiden)
- [Publisher profile](https://clawhub.ai/user/mogglemoss)
- [Project homepage from metadata](https://github.com/9b/fellow-aiden)
- [Fellow Aiden product page](https://fellowproducts.com/products/aiden)
- [OpenClaw project](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require FELLOW_EMAIL, FELLOW_PASSWORD, python3, and network access to the configured Fellow API endpoint.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
