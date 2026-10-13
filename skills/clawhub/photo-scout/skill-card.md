## Description:

Searches for images, uses visual review to select relevant results, downloads the selected originals, and helps verify their source pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sedey999](https://clawhub.ai/user/sedey999)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users find and download relevant, high-quality logos, portraits, event photos, scenery, and other images using visual review and source-page checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fetching untrusted image URLs may reach sensitive network locations.

Mitigation: Review before installation; block access to localhost, private networks, and cloud metadata endpoints, and avoid untrusted URL lists.

Risk: Some sources use stealth browser settings, and downloaded content may be untrusted.

Mitigation: Use a task-specific workdir and disable Weibo or automation-evasion paths when unnecessary.

Risk: Unpinned dependencies can change behavior between installations.

Mitigation: Pin dependencies before production use.

## Reference(s):

- [Photo Scout release on ClawHub](https://clawhub.ai/sedey999/skills/photo-scout)
- [Visual selection criteria](artifact/references/scoring.md)
- [Image source guidance](artifact/references/sources.md)

## Skill Output:

**Output Type(s):** [Image files, JSON metadata, Spreadsheet report]

**Output Format:** [Downloaded images, JSON selection and source records, and optional XLSX report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional source-page screenshots support visual verification; reports require openpyxl.]

## Skill Version(s):

4.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
