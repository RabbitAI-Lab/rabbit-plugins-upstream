## Description:

Converts locally downloaded video, audio, image, Markdown, and text-note materials into reusable text assets through an inbox, dry-run, processing, and manifest workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiyan521](https://clawhub.ai/user/shiyan521)

### License/Terms of Use:

MIT

## Use Case:

Creators, researchers, operations teams, content teams, developers, and external users can use this skill to batch intake local files they already possess and turn supported text files into reusable text assets while recording image and media items that need OCR or ASR backends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local files placed in the Inbox may be duplicated into outputs/items and manifest records.

Mitigation: Keep the Inbox limited to files intended for processing and review generated text.md, text.json, manifest.json, and summary.csv before sharing outputs.

Risk: Processing a full Inbox without preview can create more local output than expected.

Mitigation: Run the dry-run queue first and process a small batch with a limit before scaling up.

Risk: Image, audio, and video items are not extracted unless an OCR or ASR backend is configured.

Mitigation: Treat pending-backend entries as incomplete and configure and test the chosen OCR or ASR backend before relying on media results.

Risk: Using force overwrite can replace existing local outputs.

Mitigation: Use --force only when replacing prior outputs is intentional and previous artifacts have been reviewed or backed up.

## Reference(s):

- [Output Contract](references/output-contract.md)
- [ClawHub Skill Page](https://clawhub.ai/shiyan521/skills/local-material-batch-skill)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, CSV, shell commands, guidance]

**Output Format:** [Markdown guidance plus local files in Markdown, JSON, and CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes per-item text.md and text.json files under outputs/items plus batch manifest.json and summary.csv; image and media extraction requires user-configured OCR or ASR backends.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
