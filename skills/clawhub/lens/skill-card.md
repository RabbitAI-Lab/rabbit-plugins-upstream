## Description:

LENS helps an agent apply a user's facts, decision preferences, and voice to tasks the user explicitly asks it to handle through their LENS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[capachow](https://clawhub.ai/user/capachow)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals can explicitly ask an agent to use their saved facts, judgment preferences, and voice when drafting, evaluating, or deciding. They can also use LENS's interview and distillation workflows to update the profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring conversation collection can bring sensitive personal information into profile updates, and redaction cannot guarantee its removal.

Mitigation: Prefer a release that makes collection sources and integrations separately optional; review collected text and profile updates before sharing them.

Risk: Bootstrap migration can delete conflicting legacy files.

Mitigation: Back up both home and workspace .lens directories before bootstrap or migration.

Risk: Scheduled jobs may be recreated during later use even after they are removed.

Mitigation: Use a release with separately optional background jobs and integrations, and account for job recreation when disabling scheduled collection.

## Reference(s):

- [LENS release on ClawHub](https://clawhub.ai/capachow/skills/lens)
- [Alignment Scales](artifact/references/alignment-scales.md)
- [Resolve Protocol](artifact/references/resolve-protocol.md)
- [Trinity Definitions](artifact/references/trinity-definitions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, YAML configuration]

**Output Format:** [Personalized prose or updates to the LENS profile files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafting requests return finished first-person text; profile updates use the AXIOM, ETHOS, and MODUS files.]

## Skill Version(s):

2.0.1 (source: package.json, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
