## Description:

Meme Digger helps an agent investigate Chinese internet meme origins, usage, spread, source evidence, related images, and unresolved claims using Bilibili and Tieba research workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sgtbaixiao](https://clawhub.ai/user/sgtbaixiao)

### License/Terms of Use:

MIT

## Use Case:

External users and researchers use this skill to investigate what a meme means, where it may have originated, how it spread, and which claims remain unverified. The skill guides an agent through collecting platform evidence, building a timeline, reviewing meme images, and producing a sourced Markdown report and single-file HTML encyclopedia page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to store full Bilibili and Tieba login cookies in plaintext and reuses them automatically.

Mitigation: Use cookies only when authenticated access is needed, treat them like passwords, keep config/cookies.json out of synced folders and source control, and rotate or revoke sessions after use.

Risk: The skill scrapes public web sources and writes local reports and image files, which can include copyrighted or misleading material.

Mitigation: Review collected sources and images before relying on or publishing the report, keep fact and rumor labels intact, and preserve source attribution.

Risk: Generated HTML reports may contact Google Fonts when opened.

Mitigation: Open generated reports in an environment where outbound font requests are acceptable, or review and remove external font references before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sgtbaixiao/skills/meme-digger)
- [Server-resolved GitHub source](https://github.com/SgtBaixiao/meme-digger)
- [Agent Skills standard](https://agentskills.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, local Markdown research files, image manifests, and a generated HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes per-meme research workspaces, downloaded image candidates, evidence notes, and a single-file HTML encyclopedia report when the agent runs the bundled scripts.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
