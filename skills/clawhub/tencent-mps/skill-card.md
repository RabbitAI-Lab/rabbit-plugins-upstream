## Description: <br>
Tencent MPS helps agents generate Tencent Cloud Media Processing commands for audio, video, image, AIGC, content understanding, COS, usage, and task-query workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ollielin](https://clawhub.ai/user/ollielin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and media operators use this skill to prepare script commands for Tencent Cloud MPS and COS workflows, including dry runs, task submission, status checks, and result retrieval. <br>

### Deployment Geography for Use: <br>
Global, subject to Tencent Cloud MPS regional endpoint availability. <br>

## Known Risks and Mitigations: <br>
Risk: The skill may discover Tencent Cloud credentials from user and project environment files. <br>
Mitigation: Run it in an isolated environment with least-privilege Tencent credentials and no unrelated secrets in dotenv files or shell profiles. <br>
Risk: Local media may be uploaded to Tencent COS and result links may be printed. <br>
Mitigation: Review local-file inputs before execution and avoid sensitive media unless storage, retention, callback, and logging behavior are acceptable. <br>
Risk: Some workflows support deduplication, face or voice replacement, and watermark or subtitle removal. <br>
Mitigation: Do not use these workflows for evasion, impersonation, or unauthorized content changes; require user authorization for sensitive transformations. <br>
Risk: The skill can update the Python package environment to newer SDK versions. <br>
Mitigation: Install and upgrade dependencies inside a dedicated virtual environment and review dependency changes before use. <br>


## Reference(s): <br>
- [Tencent MPS Skill Page](https://clawhub.ai/ollielin/skills/tencent-mps) <br>
- [Tencent MPS Best Practices](references/best_practices.md) <br>
- [Tencent Cloud MPS Request Regions](https://cloud.tencent.com/document/product/862/37572) <br>
- [Tencent Cloud ProcessMedia API](https://cloud.tencent.com/document/api/862/37578) <br>
- [Tencent Cloud ProcessImage API](https://cloud.tencent.com/document/api/862/112896) <br>
- [Tencent Cloud CreateAigcImageTask API](https://cloud.tencent.com/document/api/862/114562) <br>
- [Tencent Cloud CreateAigcVideoTask API](https://cloud.tencent.com/document/api/862/126965) <br>
- [Tencent Cloud DescribeTaskDetail API](https://cloud.tencent.com/document/api/862/37614) <br>
- [COS Operations Reference](references/mps_cos_ops.md) <br>
- [Task Query Reference](references/mps_query_task.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with shell commands, task IDs, and result links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run commands, confirmation prompts for billable operations, and Markdown links to generated media.] <br>

## Skill Version(s): <br>
1.3.0 (source: frontmatter, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
