## Description:

Batch download WeChat articles as Markdown files with embedded images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lililly123789](https://clawhub.ai/user/lililly123789)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content archivists use this skill to save user-provided WeChat official account articles for offline reading, analysis, or archival workflows, including referenced content images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches user-provided article URLs and downloads referenced images from the network.

Mitigation: Use intended WeChat article URLs only, prefer short-format mp.weixin.qq.com/s URLs, and run in a managed environment.

Risk: The bundled script writes Markdown, images, and a manifest below the chosen output directory.

Mitigation: Choose an output directory that is safe for generated files and review the manifest and downloaded content before reuse.

Risk: Dependency hygiene depends on requests, beautifulsoup4, and lxml versions available at install time.

Mitigation: Pin or update dependencies according to the deployment environment before running the script.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lililly123789/skills/wechat-article-scraper)
- [Project homepage](https://github.com/lililly123789/wechat-article-scraper)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown files, downloaded image files, manifest JSON, and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes article Markdown files, image assets, and a manifest under the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
