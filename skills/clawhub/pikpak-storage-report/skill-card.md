## Description:

Read-only reports summarize authorized PikPak folders by size, file count, and largest known files while clearly identifying incomplete scans and unknown sizes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users can review storage usage in an explicitly authorized folder, including file counts, known sizes, and largest known files. The report is read-only and does not represent scanned data as account quota.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports can contain private file paths.

Mitigation: Keep reports in a controlled location and share them only with intended recipients.

Risk: Writing a report may overwrite the selected output file.

Mitigation: Choose an output path whose existing contents may safely be replaced.

Risk: Large scans can take substantial time, and display depth does not reduce scan work.

Mitigation: Authorize a specific folder and use it to limit scan scope; do not rely on display depth to reduce scanning.

## Reference(s):

- [upstream-design.md](references/upstream-design.md)
- [PikPak connected-app quota guidance](https://mypikpak.com/zh-CN/help-center/transfer_quota/connected_apps_quota)
- [PikPak connected-app speed limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON storage report, written to a file or standard output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include scan completeness and unknown-size indicators; file paths may be private.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
