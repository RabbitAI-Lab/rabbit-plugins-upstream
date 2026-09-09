## Description:

WorldLines scenario creation and revision with clear multi-agent dialogue, validation, and real-model playtesting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and narrative authors use this skill to create or revise WorldLines worlds, scene flows, Soul dialogue, and player-facing presentation while preserving clear speaker identification and NPC autonomy. It also guides validation, regression tests, and real-model playtesting before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A wrong target world-id could cause authored scenario changes to be written under the wrong WorldLines world root.

Mitigation: Confirm the intended world-id and writable root before editing, and keep writes scoped to ~/.worldlines/worlds/<world-id>/.

Risk: Validation, indexing, MCP health checks, and real-model playtests may use local project context and model or provider access.

Mitigation: Run those checks only in the intended project context and verify credentials, engine source, installed packages, and existing saves remain untouched unless separately authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/worldlines-scenario-authoring)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code, shell commands, configuration notes, and authored WorldLines content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scenario files, validation steps, testing evidence, and concise risk notes scoped to the selected WorldLines world.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
