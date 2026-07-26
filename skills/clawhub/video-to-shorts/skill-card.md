## Description: <br>
Select complete short-form moments from a verified Open Recut main delivery, extract approved horizontal derivatives, and optionally render reviewed 9:16 versions using shared transcript/timeline evidence and hash-bound review decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video-production agents use this skill to convert a verified Open Recut main delivery into reviewed horizontal shorts and optional 9:16 vertical outputs while preserving transcript, timeline, and review traceability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes local video, transcript, and timeline files and can create or overwrite derivative shorts outputs in the project's final/shorts area. <br>
Mitigation: Install it only for projects where local media processing is acceptable, and review generated candidate and vertical pages before approving final outputs. <br>
Risk: Incorrect candidate or crop decisions can produce misleading or low-quality shorts. <br>
Mitigation: Inspect the bound candidate page, vertical preview, contact sheets, media probes, and warnings; revise or skip when the evidence does not support approval. <br>
Risk: Changed project inputs can invalidate prior decisions or approvals. <br>
Mitigation: Rely on the skill's hash-bound receipts and validation checks, and rerun review steps after regenerated source media, transcripts, candidates, pages, or plans. <br>


## Reference(s): <br>
- [Video To Shorts Skill Protocol](SKILL.md) <br>
- [Video To Shorts README](README.md) <br>
- [ClawHub skill page](https://clawhub.ai/whitetowerai/skills/video-to-shorts) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Markdown, HTML, Media files] <br>
**Output Format:** [Markdown protocol with PowerShell commands plus project-local JSON, Markdown summaries, HTML review pages, and derivative MP4 files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes work, review, cache, and final/shorts artifacts under the target project; review gates are hash-bound.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
