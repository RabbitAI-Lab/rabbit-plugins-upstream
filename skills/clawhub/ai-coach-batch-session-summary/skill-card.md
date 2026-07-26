## Description: <br>
Analyzes batches of recording transcripts to generate multi-dimensional customer-acquisition insight reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business teams use this skill to batch-analyze completed ASR recording transcripts, summarize sales outreach patterns, and receive a hosted HTML insight report with charts and excerpts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recording metadata and transcript-derived report content may contain sensitive business or personal information. <br>
Mitigation: Redact identifiers and transcript excerpts before use, and remove bundled live test outputs from release artifacts. <br>
Risk: Generated reports are uploaded to hosted HTML links that may be shared beyond the intended audience. <br>
Mitigation: Use fixed allowlisted upload hosts, require private or expiring links where available, and confirm report URLs are appropriate before sharing. <br>
Risk: Report rendering relies on third-party CDN JavaScript. <br>
Mitigation: Review and approve the CDN dependency, or pin and serve the charting script from a trusted internal source. <br>
Risk: Fetching recording data over non-HTTPS service endpoints can expose transcript data in transit. <br>
Mitigation: Require HTTPS endpoints or a trusted private network path for recording-service access. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/legionspace-hackathon/skills/ai-coach-batch-session-summary) <br>
- [Default Analysis Dimensions](artifact/DIMENSIONS.md) <br>
- [ASR Insight HTML Template](artifact/asr_insight_template.html) <br>
- [Chart.js 4.4.1](https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown response with a hosted HTML report link, plus generated HTML and JSON metadata files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses ASR records from the current request window and should avoid exposing local temporary paths or raw transcript JSON to the user.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
