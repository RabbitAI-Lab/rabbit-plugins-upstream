## Description: <br>
Runs multi-source research across GitHub, HN, Reddit, arXiv, and Semantic Scholar. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical researchers use this skill to classify a research topic, coordinate parallel code, discourse, academic, and TRIZ research agents, synthesize their findings, and produce a research report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may query external sources and run parallel research agents, which can expose sensitive topics or context outside the local workspace. <br>
Mitigation: Use it on sensitive topics only when external-source research is acceptable, and review the research prompts before agent dispatch. <br>
Risk: The skill may leave saved reports or session data in docs/research/ or related session storage. <br>
Mitigation: Review generated files before sharing and remove sensitive session data from the workspace when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-tome-research) <br>
- [Claude Night Market tome plugin](https://github.com/athola/claude-night-market/tree/master/plugins/tome) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, files] <br>
**Output Format:** [Markdown reports, briefs, transcripts, and JSON agent findings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save reports and session state under docs/research/ or related session storage.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
