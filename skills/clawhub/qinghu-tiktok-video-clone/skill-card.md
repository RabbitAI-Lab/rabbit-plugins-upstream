## Description:

Uses Qinghu TikTok ranking, search, video detail, and comment data to identify proven videos, break down hooks, content structure, selling points, and comment insights, and produce reusable shooting script templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce marketers, content teams, and social commerce operators use this skill to find TikTok video examples, analyze why they worked, and turn the structure into practical scripts for new product videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a Qinghu API token from user input or the QINGHU_TOKEN or QHKIT_TOKEN environment variables.

Mitigation: Install and run it only when Qinghu API access is intended, and keep the token scoped, private, and removable from the environment.

Risk: Some Qinghu tools may consume paid Qinghu points.

Mitigation: Require user consent before paid calls and report actual Qinghu point consumption using the returned pointCost value.

Risk: Large result sets may create local spreadsheet or cache files.

Mitigation: Review generated files before sharing and remove local exports or caches when they are no longer needed.

Risk: Video replication workflows can create copyright or platform-policy risk if users copy source footage directly.

Mitigation: Use the skill to learn structure and produce original scripts, scenes, and recordings rather than reusing another creator's video assets.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/autoagc/skills/qinghu-tiktok-video-clone)
- [Qinghu API Endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, script templates, JSON examples, and optional exported spreadsheet files for large result sets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Qinghu API tools, request or read a Qinghu token, report paid point consumption after authorized paid calls, and export local spreadsheet or cache files when result sets are large.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
