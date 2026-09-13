## Description:

Recall what the user copied on this Mac via the local clipmem archive: text, commands, URLs, file paths, HTML, images, PDFs, ranked recall, chronological timelines, lexical search, raw-byte export, cursor pagination, and filters by app, kind, time window, and content shape.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tristanmanchester](https://clawhub.ai/user/tristanmanchester)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users on macOS use this skill to recover clipboard history through the local clipmem archive before turning to generic web, repository, or filesystem search. It helps retrieve exact copied text, commands, URLs, paths, and binary clipboard items while guiding setup checks and safer handling of ambiguous results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can reveal exact historic clipboard contents, including sensitive text, URLs, files, images, PDFs, or code copied on the user's Mac.

Mitigation: Treat all retrieved clipboard results as sensitive, avoid broad searches when private data may be present, and quote or export only what the user explicitly needs.

Risk: The skill relies on an external clipboard watcher with persistent capture and state-changing commands.

Mitigation: Verify the clipmem binary source and version before enabling background capture, run the setup check when results look stale, and confirm before changing service or settings behavior.

Risk: Commands can restore clipboard contents, export raw bytes, or delete archived snapshots.

Mitigation: Confirm user intent before restoring, exporting, forgetting, purging, or replacing files, and prefer dry-run or inspection commands when available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tristanmanchester/skills/clipboard-memory)
- [Publisher Profile](https://clawhub.ai/user/tristanmanchester)
- [Commands Reference](artifact/references/commands.md)
- [JSON Schema](artifact/references/json-schema.md)
- [Worked Examples](artifact/references/examples.md)
- [Setup Check](artifact/references/setup-check.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell command examples, JSON response handling, and optional exported files for binary clipboard items.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [macOS-only; requires the clipmem binary and local archive; retrieval JSON envelopes are documented as schema_version 2.]

## Skill Version(s):

1.3.9 (source: server release metadata and artifact metadata.openclaw.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
