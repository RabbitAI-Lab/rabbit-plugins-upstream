## Description: <br>
Use when the user asks to (re)cluster DIBP topic data into 需求簇/用户主动洞察, regenerate clusters.json, review the long-tail (未分类) topics, add a new theme to the taxonomy, or push cluster results to the dev/prod backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[christinelee3025](https://clawhub.ai/user/christinelee3025) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators working in the DIBP codebase use this skill to rerun the offline full-batch topic clustering pipeline, inspect quality signals, propose taxonomy updates, and, with explicit approval, ingest cluster results into backend environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Backend ingestion can overwrite shared DIBP cluster records for a selected cluster date. <br>
Mitigation: Require explicit user approval after restating the target environment, cluster date, and overwrite behavior before running ingestion commands. <br>
Risk: Production ingestion has high impact if run against the wrong environment or date. <br>
Mitigation: Treat prod ingestion as a separate confirmation step and only use production confirmation flags after the user explicitly authorizes prod. <br>
Risk: Reusing stale files from the pipeline scratch directory can produce misleading clustering results. <br>
Mitigation: Rerun the full pipeline from the first step and review reported long-tail and homogeneity quality signals before accepting output. <br>
Risk: Changing the manually maintained theme taxonomy affects global topic classification. <br>
Mitigation: Present proposed taxonomy changes for human review and wait for confirmation before editing the theme library. <br>


## Reference(s): <br>
- [DIBP Topic 聚类 ClawHub skill page](https://clawhub.ai/christinelee3025/skills/dibp-topic-clustering) <br>
- [hf-mirror.com model endpoint](https://hf-mirror.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, code references, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include review checkpoints, proposed taxonomy diffs, pipeline command sequences, and backend-ingestion confirmation text.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
