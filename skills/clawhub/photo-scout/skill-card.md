## Description:

Photo Scout helps an agent search image sources, visually gate candidate results, download selected original images, and verify source-page context for high-quality photo and logo collection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sedey999](https://clawhub.ai/user/sedey999)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users can use this skill through an agent to collect relevant, high-quality images or clean logo assets for documents, research, marketing analysis, product work, and reference packs while preserving source metadata for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches and renders arbitrary web content while searching, downloading, and verifying images.

Mitigation: Run it only in an isolated environment with no sensitive local files, no cloud metadata access, and no internal network reachability.

Risk: Supplemental URL inputs and verification pages may direct the browser or downloader to untrusted locations.

Mitigation: Review URLs before using --extra-file, --extra-urls, or verify, and avoid --weibo-album unless it is needed for the task.

Risk: Unpinned dependency installation can change behavior across environments.

Mitigation: Pin dependencies before broader use and keep browser sandboxing enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sedey999/skills/photo-scout)
- [Visual gating scoring rules](artifact/references/scoring.md)
- [Authority source list](artifact/references/sources.md)

## Skill Output:

**Output Type(s):** [files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands plus downloaded image files, JSON metadata, search screenshots, contact sheets, verification screenshots, and XLSX reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include candidate metadata, selected-image metadata, final ranked images, and optional source-page verification artifacts.]

## Skill Version(s):

4.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
