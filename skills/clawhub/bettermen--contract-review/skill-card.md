## Description: <br>
AI合同智能审查助手 reviews contract text, extracts key information, scores risk across nine dimensions, suggests clause revisions, cites legal references, generates negotiation guidance, and produces an interactive HTML review report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, legal operations teams, and contract reviewers use this skill to analyze pasted or uploaded contracts, identify legal and business risks, extract structured contract details, and prepare review reports for human validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process sensitive contract text. <br>
Mitigation: Use explicit prompts, avoid submitting confidential contracts unless the environment is approved for that data, and review generated outputs before sharing. <br>
Risk: The skill creates local report files that may contain contract details. <br>
Mitigation: Store generated reports in an approved location and delete or protect files according to the user’s document-handling policy. <br>
Risk: The skill claims offline use while evidence notes possible network paths. <br>
Mitigation: Avoid URL-based inputs for confidential material and block or replace the report template’s CDN request with a local Chart.js copy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bettermen/contract-review) <br>
- [Publisher profile](https://clawhub.ai/user/bettermen) <br>
- [Project homepage](https://github.com/bettermen/contract-review) <br>
- [General contract review checklist](references/checklist_general.md) <br>
- [Risk scoring methodology](references/risk_scoring.md) <br>
- [Law reference library](references/law_reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON intermediate data, shell commands, and an HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local JSON and HTML report files while processing contract text.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
