## Description: <br>
Helps users run interactive topic research, maintain structured Markdown research folders, synthesize findings, and optionally export PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, students, and independent founders use this skill to research a topic through interactive agent sessions, record findings and sources in persistent Markdown documents, and review next steps over multiple rounds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research notes are saved locally and may contain sensitive topics or source material. <br>
Mitigation: Use non-confidential topics unless the local agent environment and storage location are approved for that data. <br>
Risk: Interactive research can send topic details to web search providers or other agent-integrated services. <br>
Mitigation: Avoid confidential, proprietary, or personal research prompts unless those providers are acceptable for the data. <br>
Risk: The skill may create files under ~/.research-workspace and optionally run PDF export tools. <br>
Mitigation: Review proposed file paths and commands before execution, and install optional export dependencies only from trusted package sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/parallel-research-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown research documents, text guidance, optional shell commands, and optional JSON-style status responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates persistent research folders under ~/.research-workspace and may export research documents to PDF when optional tools are installed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
