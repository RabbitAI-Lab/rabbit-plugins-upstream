## Description:

This skill automates a logged-in Xiaohongshu browser session to batch-export a creator's public notes as local Markdown and summary JSON while preserving note text, source URLs, media links, and engagement counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content researchers, and operators use this skill to archive or analyze public Xiaohongshu creator notes from an authenticated browser session. It is intended for batch export, backup, competitive research, and preparing local Markdown files for downstream AI analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill acts through the user's logged-in Xiaohongshu browser session and can export public note content at scale.

Mitigation: Use it only for intended accounts and exports, and confirm that the browser session and target profile are appropriate before running.

Risk: Generated Markdown and JSON may contain source URLs with xsec_token parameters and engagement metadata.

Mitigation: Review exported files before sharing them with AI tools, collaborators, or public locations, and store them in a deliberate output directory.

Risk: Some records may be partial when interaction counts or page content do not load before the timeout.

Mitigation: Check summary.json for partial and failed entries, then rerun with adjusted count, offset, or a fresh authenticated browser session when completeness matters.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/fatmind/skills/xhs-note-batch-export)
- [Publisher profile](https://clawhub.ai/user/fatmind)
- [webclaw3 browser automation prerequisite](https://clawhub.ai/fatmind/skills/webclaw3-browser-automation)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Local Markdown files for exported notes plus JSON summary/result files and a single-line JSON status response on stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes per-note Markdown files, summary.json, res.json, and data.md under the selected output directory; supports count, offset, and parallel export controls.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
