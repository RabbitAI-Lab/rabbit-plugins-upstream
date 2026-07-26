## Description: <br>
External Audit Response helps users prepare for external audits by confirming audit type, industry, and standard before producing preparation advice, a checklist, and key cautions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External audit preparation teams, quality managers, and operations staff use this skill to plan for first-party internal audits, second-party customer audits, and third-party certification or surveillance audits. It produces preparation guidance, a tabular checklist, and practical cautions after collecting the required audit context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill generates local TXT and Markdown audit-preparation files that may contain sensitive audit or business information. <br>
Mitigation: Use the skill in a dedicated folder and apply the organization's handling rules for sensitive audit material. <br>
Risk: Same-date report filenames may already exist in the working directory. <br>
Mitigation: Check for existing same-date files before generating reports to avoid confusion or accidental overwrite. <br>
Risk: Audit preparation guidance does not replace official communications with certification bodies, customers, or internal accountable owners. <br>
Mitigation: Have responsible business, quality, or compliance personnel review and approve final audit positions and responses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-external-audit-response) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-external-audit-response) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [TXT and Markdown audit-preparation documents] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates dated local audit-preparation files for advice, checklist, and cautions; users should review content before external use.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
