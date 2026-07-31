## Description: <br>
Generates commands for Tencent Cloud MPS end-to-end video dubbing workflows that translate video language, optionally burn translated subtitles, create AI-cloned dubbing audio, and query task status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-mpaas-skills](https://clawhub.ai/user/tencent-mpaas-skills) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and operators use this skill to prepare correct Tencent Cloud MPS video dubbing commands for full-language-localization jobs, including local file upload, COS input handling, task polling, result download, and status queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local-file handling can upload input media even in dry-run or missing-confirmation paths. <br>
Mitigation: Use only non-sensitive test media for dry runs, inspect generated commands before execution, and rely on narrowly scoped Tencent Cloud CAM credentials and dedicated COS prefixes. <br>
Risk: The skill can automatically install or upgrade Python dependencies. <br>
Mitigation: Install dependencies manually in an isolated virtual environment before use, and review dependency versions as part of deployment approval. <br>
Risk: Presigned URLs and COS output links can grant temporary access to generated media. <br>
Mitigation: Treat generated links as sensitive, avoid posting them in public channels, and rotate or expire access according to the storage policy. <br>


## Reference(s): <br>
- [Video dubbing parameters and examples](references/mps_video_dubbing.md) <br>
- [ProcessMedia request examples](references/example.md) <br>
- [Tencent Cloud MPS one-stop dubbing guide](https://cloud.tencent.com/document/product/862/124504) <br>
- [Tencent Cloud ProcessMedia AiAnalysisTask](https://cloud.tencent.com/document/product/862/37578) <br>
- [Tencent Cloud DescribeTaskDetail](https://cloud.tencent.com/document/api/862/37614) <br>
- [Tencent Cloud MPS pricing](https://cloud.tencent.com/document/product/862/36180) <br>
- [Tencent Cloud MPS regions](https://cloud.tencent.com/document/product/862/37572) <br>
- [Tencent Cloud COS regions](https://cloud.tencent.com/document/product/436/6224) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text containing shell commands, task identifiers, and Markdown links for generated download URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [For processing jobs, the skill is expected to surface cost confirmation requirements and the Tencent MPS TaskId; dry-run and query paths avoid new processing charges.] <br>

## Skill Version(s): <br>
1.0.6 (source: evidence.json metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
