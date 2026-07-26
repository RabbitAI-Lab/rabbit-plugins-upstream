## Description: <br>
AI-powered academic paper reviewer. Uses a multi-agent system (Deconstructor, Devil's Advocate, Judge) to analyze papers for logical flaws, contradictions, and empirical validity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sschepis](https://clawhub.ai/user/sschepis) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to review academic papers or scientific claims for logical structure, contradictions, empirical weaknesses, and improvement suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Manuscript content and generated critique may be sent to external LLM, search, or literature services. <br>
Mitigation: Use only with provider data handling you trust, especially for confidential or unpublished papers. <br>
Risk: Google service credentials may be used for Vertex AI access. <br>
Mitigation: Keep credentials least-privilege and outside the repository. <br>
Risk: The serper-tool helper path uses shell-based execution. <br>
Mitigation: Avoid that adapter path until shell execution is replaced with argument-based execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sschepis/skills/peer-reviewer) <br>
- [Publisher profile](https://clawhub.ai/user/sschepis) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, json, guidance] <br>
**Output Format:** [JSON merit report with scores, defense strategy, and suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save the report as a local JSON file when run through the CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, package.json, server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
