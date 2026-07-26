## Description: <br>
Generates commands for Tencent Cloud MPS to create an end-to-end translated and dubbed version of a video, including OCR or ASR extraction, translation, subtitle burn-in, and AI voice dubbing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-mpaas-skills](https://clawhub.ai/user/tencent-mpaas-skills) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and media localization operators use this skill to generate command lines and configuration checks for submitting, querying, and downloading Tencent Cloud MPS end-to-end video translation and dubbing jobs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can auto-install or upgrade Python packages before running its Tencent Cloud helper scripts. <br>
Mitigation: Review the dependency list first, run in a dedicated virtual environment, and manually control upgrades when operating in sensitive environments. <br>
Risk: The helper scripts read local environment and dotenv-style files that may contain Tencent Cloud credentials. <br>
Mitigation: Use least-privilege Tencent credentials, keep credential files outside untrusted directories, and avoid running from directories that may contain stray .env files. <br>
Risk: The skill handles video uploads, cloud storage objects, task outputs, and presigned download URLs. <br>
Mitigation: Limit COS bucket permissions, avoid sharing presigned URLs, and confirm storage locations before submitting jobs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tencent-mpaas-skills/skills/tencent-mps-video-dubbing) <br>
- [Video dubbing parameters and examples](references/mps_video_dubbing.md) <br>
- [ProcessMedia request examples](references/example.md) <br>
- [Tencent Cloud one-stop video dubbing documentation](https://cloud.tencent.com/document/product/862/124504) <br>
- [Tencent Cloud ProcessMedia API](https://cloud.tencent.com/document/product/862/37578) <br>
- [Tencent Cloud DescribeTaskDetail API](https://cloud.tencent.com/document/api/862/37614) <br>
- [Tencent Cloud MPS pricing](https://cloud.tencent.com/document/product/862/36180) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown text with command lines, task identifiers, and links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may include dry-run, query, polling, upload, download, and charge-confirmation options.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
