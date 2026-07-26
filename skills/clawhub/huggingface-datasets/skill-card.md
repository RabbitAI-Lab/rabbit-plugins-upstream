## Description: <br>
Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search text, apply filters, download parquet URLs, and read size or statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huggingface](https://clawhub.ai/user/huggingface) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data practitioners use this skill to explore Hugging Face datasets through Dataset Viewer API calls, inspect rows and metadata, find parquet shards, and get guidance for dataset upload flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may expect only read-only dataset exploration while the skill also includes dataset creation and upload guidance. <br>
Mitigation: Use only the Dataset Viewer endpoints when read-only behavior is intended, and review any create or upload commands before execution. <br>
Risk: Uploading local folders or agent traces can expose secrets, PII, private prompts, tool outputs, or file paths. <br>
Mitigation: Inspect selected files before upload, narrow the upload scope, and prefer private Hugging Face dataset repositories. <br>


## Reference(s): <br>
- [Hugging Face Dataset Viewer API](https://datasets-server.huggingface.co) <br>
- [Create a Hugging Face dataset](https://huggingface.co/new-dataset) <br>
- [ClawHub skill page](https://clawhub.ai/huggingface/skills/huggingface-datasets) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API calls, configuration] <br>
**Output Format:** [Markdown with inline API paths and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include curl commands, Hugging Face Dataset Viewer endpoint paths, pagination parameters, and private-upload precautions.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
