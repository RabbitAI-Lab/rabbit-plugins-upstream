## Description:

Design or audit self-describing ML run metadata attached at initialization, including intent, code and data identity, resume lineage, and evidence limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and ML engineers use this skill to design, audit, and locally validate ML run provenance metadata before training, tracker integration, resume handling, or authorized backfill work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented install command can introduce supply-chain risk if the package source changes after review.

Mitigation: Pin the installer and skill source to a reviewed release or commit when strong supply-chain control is required.

Risk: Provenance records may contain private paths, source references, dataset details, or tracker metadata that should not be disclosed broadly.

Mitigation: Redact records and keep repository URLs, data identifiers, secrets, and tracker writes within an explicitly authorized disclosure boundary.

Risk: Local validation confirms record shape and consistency, not that the metadata is true, persisted in a tracker, or sufficient to reproduce an experiment.

Mitigation: Verify timestamps, hashes, tracker readback, dataset permissions, and recorded commits against actual artifacts before relying on the record.

## Reference(s):

- [Local metadata contract](references/metadata-contract.md)
- [ClawHub skill page](https://clawhub.ai/antreasantoniou/skills/ml-run-provenance)
- [Publisher profile](https://clawhub.ai/user/antreasantoniou)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with optional JSON validation feedback and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled validator reads local JSON records and reports schema or consistency errors without contacting trackers.]

## Skill Version(s):

1.0.0 (source: server release metadata and changelog, released 2026-09-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
