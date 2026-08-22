## Description:

Opens the AI PPT editing WebUI for an existing SenseNova HTML slide deck without regenerating slides.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and presentation authors use this skill to start or reuse a local WebUI for previewing and editing an already generated HTML slide deck while avoiding slide regeneration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill starts a local editing server that can modify deck files and use configured agent or gateway credentials.

Mitigation: Install only when that behavior is intended, run it on trusted machines, and disable bridge or export features that are not needed.

Risk: The local editing server may be exposed beyond localhost on some remote, Docker, WSL, or LAN setups.

Mitigation: Prefer localhost-only binding, avoid untrusted networks, and use an explicit forwarded or public URL only when the endpoint is protected and expected.

Risk: Shared or default bridge keys can allow unintended access to companion agent or gateway sessions.

Mitigation: Use explicit non-shared gateway keys, keep Workbench and Gateway keys matched, and avoid relying on default fallback keys in shared environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-ppt-workbench)
- [Hermes Gateway API Auth Setup for PPT Workbench](artifact/references/gateway-auth.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown/plain text with shell commands and JSON launcher status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns or reports editor, public, and progress URLs when the workbench starts successfully.]

## Skill Version(s):

2026.8.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
