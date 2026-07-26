## Description: <br>
抖音无水印下载器支持无水印视频和原图图文下载，并自动识别单个或批量抖音链接。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[belingud](https://clawhub.ai/user/belingud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to download Douyin videos without watermarks and Douyin image posts as original JPEG files from shared Douyin links, including batch lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may auto-install Python dependencies and the security summary notes pinned HTTP libraries with current security advisories. <br>
Mitigation: Review and update the pinned requirements before use, and run the skill in a dedicated virtual environment. <br>
Risk: The downloader writes media files from user-provided Douyin links to local storage. <br>
Mitigation: Use a dedicated output directory and review downloaded files before moving them into trusted workspaces. <br>
Risk: Douyin API or WAF changes can cause failed, incomplete, or delayed downloads. <br>
Mitigation: Verify the resulting files after each run and retry later when the upstream service rate-limits requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/belingud/skills/douyin-downloader) <br>
- [Source repository listed in artifact metadata](https://github.com/belingud/douyin-downloader-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Text] <br>
**Output Format:** [Terminal text plus downloaded MP4 and JPEG files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-link mode writes one media result; batch mode processes one link per line and writes results to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
