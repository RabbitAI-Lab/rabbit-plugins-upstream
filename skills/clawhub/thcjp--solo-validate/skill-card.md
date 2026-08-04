## Description: <br>
Solo Validate helps users evaluate startup ideas with S.E.E.D. niche scoring, STREAM six-layer analysis, and Devil's Advocate pressure testing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and startup teams use this skill to turn short startup-idea descriptions into structured validation reports, scores, risk challenges, and recommended next actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution and local file-search tools that are broader than its startup-idea analysis purpose. <br>
Mitigation: Install only in environments where command execution and local file access are acceptable, review proposed commands before execution, and avoid granting access to secrets or sensitive business data. <br>
Risk: The skill describes generic file, API, and command-execution capabilities without clear limits. <br>
Mitigation: Use least-privilege agent permissions and prefer sandboxed runs until the publisher narrows and documents the behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/solo-validate) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured reports with optional inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include S.E.E.D. scores, STREAM analysis sections, Devil's Advocate findings, GO/PIVOT/KILL recommendations, and next-step guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 2.1.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
