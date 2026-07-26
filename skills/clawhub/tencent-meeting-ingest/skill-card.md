## Description: <br>
Ingest Tencent Meeting recordings, minutes, and transcripts into the Research KB by delegating platform fetching to tencent-meeting-skill, then letting OpenClaw generate structured meeting wiki pages and related KB updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[myd2002](https://clawhub.ai/user/myd2002) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and research operations teams use this skill to turn Tencent Meeting recordings, smart minutes, and transcripts into structured Research KB meeting pages and related wiki updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive meeting transcripts and minutes may be archived into the Research KB. <br>
Mitigation: Install only with trusted Tencent Meeting command paths and Gitea repositories, verify repository access controls, and use a narrowly scoped Gitea bot token. <br>
Risk: Broad meeting scans can increase exposure, quota use, or unwanted ingestion. <br>
Mitigation: Keep source configuration limits such as lookback days, window days, page size, and maxRecords tight for the intended source. <br>
Risk: Generated wiki drafts could target unintended paths or embed excessive content in manifests. <br>
Mitigation: Use the built-in validate-manifest step, task-scoped draft directory checks, allowed write roots, UTF-8 Markdown validation, and compact manifests without embedded page bodies. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/myd2002/skills/tencent-meeting-ingest) <br>
- [Publisher profile](https://clawhub.ai/user/myd2002) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON context and result envelopes with UTF-8 Markdown drafts and a compact JSON manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes or updates Research KB pages, catalog.json, index.md, archived source files, and a backend result file.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
