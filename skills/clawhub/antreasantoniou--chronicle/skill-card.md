## Description:

Chronicle preserves operational history and intent across agent sessions for resuming work, recording decisions, preparing risky operations, verifying deployments, correcting claims, recovering captured file versions, and handing off unfinished work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and agents use Chronicle to reconstruct project history across sessions, preserve decisions and intent, and recover captured file versions when work is resumed or handed off.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chronicle can persistently capture commands, prompts, files, transcripts, remotes, and model-processing context.

Mitigation: Install only when persistent operational-history recording is intended, pin the install to a reviewed commit, preview hook installation with --dry-run, and avoid broad hooks on sensitive machines unless that capture is acceptable.

Risk: Captured history, content stores, spines, transcripts, and the optional canvas can expose private project history or secrets.

Mitigation: Keep ~/.chronicle, .chronicle, CHRONICLE.md, spines, transcripts, and the canvas private; review exclusions and do not rely on redaction to catch every secret.

Risk: Narration and remote sync can cause trace content to leave the local machine.

Mitigation: Review narration dry-run prompts and outbound data before enabling a model provider or remote synchronization.

Risk: Hook configuration, Codex trust, execution approval, and verified coverage are separate states.

Mitigation: Verify hook coverage with harmless tests, inspect captured events before relying on recovery, and continue using the host approval mechanism for commands.

## Reference(s):

- [Codex integration status](references/codex.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact pyproject.toml reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
