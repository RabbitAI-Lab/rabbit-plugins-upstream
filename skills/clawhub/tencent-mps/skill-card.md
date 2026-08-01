## Description: <br>
Tencent MPS helps agents generate correct Python commands for Tencent Cloud Media Processing workflows across media transcoding, enhancement, AI generation, content understanding, COS operations, task lookup, and usage reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ollielin](https://clawhub.ai/user/ollielin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and media operations teams use this skill to select documented Tencent Cloud MPS helper scripts and produce shell commands for processing audio, video, images, documents, and COS assets. It is intended for users who already have permission to use the relevant Tencent Cloud services, credentials, and media inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scripts require Tencent Cloud credentials and access to COS storage. <br>
Mitigation: Use scoped credentials in a controlled local environment, avoid sharing secrets, rotate credentials when needed, and verify configuration with the environment-check script before running processing tasks. <br>
Risk: Local media or documents may be uploaded to Tencent Cloud services or COS as part of processing. <br>
Mitigation: Process only content you are authorized to upload, use dedicated buckets with appropriate retention controls, and remove temporary inputs and outputs when they are no longer needed. <br>
Risk: Processing workflows can generate Tencent Cloud charges, especially for AIGC video, long media, or batch image tasks. <br>
Mitigation: Use dry-run previews for uncertain or high-cost requests, require explicit confirmation before execution, avoid repeated submissions after incomplete results, and set budget alerts or spending limits in Tencent Cloud. <br>
Risk: Task results and generated outputs may be exposed through temporary links or downloaded files. <br>
Mitigation: Treat pre-signed links and downloaded media as sensitive, share them only with intended recipients, and prefer controlled storage locations for retained outputs. <br>
Risk: Voice cloning, deduplication, face replacement, and other media-alteration workflows can be misused for impersonation, evasion, or misleading content. <br>
Mitigation: Use these workflows only with consent and policy review, and do not use them for impersonation, platform evasion, or unauthorized content manipulation. <br>
Risk: The artifact includes runtime dependency installation or upgrade behavior for Python packages. <br>
Mitigation: Review the dependency list before installation, run the scripts in an isolated environment, and pin or preinstall approved package versions where change control is required. <br>


## Reference(s): <br>
- [Tencent MPS release page on ClawHub](https://clawhub.ai/ollielin/skills/tencent-mps) <br>
- [Tencent Cloud MPS pricing](https://cloud.tencent.com/document/product/862/36180) <br>
- [Tencent Cloud MPS region list](https://cloud.tencent.com/document/product/862/37572) <br>
- [ProcessMedia API](https://cloud.tencent.com/document/api/862/37578) <br>
- [ProcessImage API](https://cloud.tencent.com/document/api/862/112896) <br>
- [CreateAigcImageTask API](https://cloud.tencent.com/document/api/862/114562) <br>
- [CreateAigcVideoTask API](https://cloud.tencent.com/document/api/862/126965) <br>
- [COS operations reference](references/mps_cos_ops.md) <br>
- [Tencent MPS usage best practices](references/best_practices.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, markdown, configuration, guidance] <br>
**Output Format:** [Markdown text, usually command-only shell invocations with task IDs and links when applicable.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cost warnings, dry-run suggestions, confirmation prompts, and Markdown links for generated media outputs.] <br>

## Skill Version(s): <br>
1.2.9 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
