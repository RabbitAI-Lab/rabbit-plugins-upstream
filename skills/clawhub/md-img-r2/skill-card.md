## Description: <br>
Prepare local Markdown image references for Cloudflare R2 or S3-compatible object storage by creating dry-run plans, requiring explicit confirmation for uploads or rewrites, and replacing approved local paths with public URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangchao228](https://clawhub.ai/user/yangchao228) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content publishers, and publishing workflow maintainers use this skill to inspect Markdown image links, create a dry-run image publishing plan, upload reviewed assets to R2 or another S3-compatible store, and rewrite approved local image paths to public URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Apply mode can publish unintended Markdown images or rewrite paths before the user has accepted the plan. <br>
Mitigation: Review the dry-run plan first, then use apply mode only with the explicit upload or write confirmation gate. <br>
Risk: Object storage credentials or private local paths could be exposed during publishing workflows. <br>
Mitigation: Keep R2 credentials in a secure environment, avoid command-line history for secrets, and only run uploads for Markdown and image paths intended to become public. <br>
Risk: Missing files, paths outside the reviewed project root, or incomplete URL maps can produce incorrect replacements. <br>
Mitigation: Resolve reported issues before applying changes, inspect the backup and replacement report after apply mode, and verify public URLs separately when required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yangchao228/skills/md-img-r2) <br>
- [Publisher profile](https://clawhub.ai/user/yangchao228) <br>
- [OpenClaw homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/publishing/md-img-r2) <br>
- [Source homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/publishing/md-img-r2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands plus JSON image-publish plan and replacement report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Plan mode leaves Markdown unchanged; apply mode can create backups, upload reviewed images, and rewrite only approved local-image references.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
