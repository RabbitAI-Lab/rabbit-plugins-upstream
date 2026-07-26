## Description: <br>
Analyzes one video or a directory of videos by extracting keyframes, searching the web for references, storing metadata and results in Supabase, and publishing category-grouped reports to Feishu Wiki. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to turn single-video or directory-based video collections into searchable Supabase records and Feishu Wiki reports. It is useful when extracted frames, search references, and batch status need to be organized into category-grouped documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes a broad Lark/Feishu automation workspace beyond the advertised video analyzer. <br>
Mitigation: Install only when those workspace capabilities are intended, review and remove unrelated nested skills, and limit Lark/Feishu scopes before deployment. <br>
Risk: The workflow writes video metadata, extracted frame paths, search results, and reports to Supabase and Feishu Wiki. <br>
Mitigation: Use least-privilege credentials, protect Supabase service-role keys, and confirm target Wiki visibility before processing sensitive videos. <br>
Risk: ffmpeg processes user-provided video files and saves extracted frames locally. <br>
Mitigation: Run the skill in a constrained workspace, process trusted inputs, and delete or secure extracted frames after use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/terrycarter1985/video-content-analyzer) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [ClawHub Package Metadata](artifact/clawhub.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration] <br>
**Output Format:** [Markdown reports, JSON-like CLI summaries, Supabase records, and extracted frame image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, ffmpeg, Supabase credentials, Google Custom Search credentials, and Feishu OpenAPI credentials.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata, created 2026-06-20T15:13:57Z) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
