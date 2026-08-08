## Description: <br>
Auto-analyze URLs/info for OpenClaw strategic value, classify, create Obsidian notes, update memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2233admin](https://clawhub.ai/user/2233admin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to ingest shared URLs, articles, tweets, and pasted external information, classify its relevance to OpenClaw, and turn it into structured notes, memory updates, and next-step recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may fetch shared external content and save it into local notes or memory without a clear confirmation step. <br>
Mitigation: Require confirmation before filesystem writes, restrict or review URLs before fetching, and avoid using it on secrets, private messages, or proprietary content. <br>
Risk: Generated note paths and filenames are based on ingested content. <br>
Mitigation: Sanitize generated filenames and keep writes constrained to the intended Obsidian and OpenClaw memory locations. <br>


## Reference(s): <br>
- [ClawHub Skill Release](https://clawhub.ai/2233admin/openclaw-skill-intelligence-ingestion) <br>
- [Publisher Profile](https://clawhub.ai/user/2233admin) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown notes and concise text summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create Obsidian intelligence notes and append local memory logs when the host agent has filesystem access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
