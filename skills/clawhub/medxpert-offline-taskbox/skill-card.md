## Description:

MedXpert Offline Taskbox helps agents create, route, sync, and run local/offline LLM task queues across machines with Python scripts, Ollama workers, L1-L5 routing, retry handling, and sync-package import/export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and agent users use this skill to queue work on one machine, sync it to another, and process suitable batch, document, or sensitive tasks locally with Ollama. It is useful when users want offline execution, lower cloud-model spend, and explicit routing between local and cloud work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted sync packages can alter local task state during import.

Mitigation: Import sync packages only from trusted machines and inspect or back up JSON taskbox files before merging unfamiliar packages.

Risk: Task details may accidentally contain passwords, tokens, or other secrets.

Mitigation: Keep credentials out of task titles and details; treat optional cloud-document or DSH integrations as separate setups requiring credential review.

Risk: Exposing Ollama outside localhost or a trusted private network can allow unauthenticated local-model access.

Mitigation: Keep Ollama bound to localhost for local use, or expose it only through a trusted private network such as Tailscale or WireGuard.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/medxpert-offline-taskbox)
- [ClawHub publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [DeepSeek Harness documentation](https://deepseek-harness.github.io)
- [DeepSeek Harness product page](https://deepseek.com/harness)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON]

**Output Format:** [Markdown guidance with CLI examples and JSON task data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local task and result data is stored in JSON taskbox and sync-package files; worker responses are constrained to concise structured text.]

## Skill Version(s):

2.4.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
