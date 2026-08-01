## Description: <br>
HTML helps agents write, review, and fix semantic HTML markup, forms, accessibility, document head metadata, media embeds, parsing issues, and safe handling of untrusted HTML. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent needs HTML-specific guidance for creating or repairing markup, diagnosing form and accessibility behavior, building metadata and media embeds, validating parsed DOM behavior, or producing safer patterns for user-supplied HTML. <br>

### Deployment Geography for Use: <br>
Global; runs locally in supported Linux, macOS, and Windows agent environments. <br>

## Known Risks and Mitigations: <br>
Risk: The skill may create or update local Clawic notes about HTML decisions, audits, templates, hostnames, and project context. <br>
Mitigation: Install only when local note storage under ~/Clawic/data/ is acceptable, and avoid storing secrets or sensitive values in those notes. <br>
Risk: Generated markup or guidance can still be incorrect for a specific application, browser target, accessibility requirement, or security posture. <br>
Mitigation: Review proposed changes before use, validate the resulting HTML, and apply project-specific accessibility and security checks before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/html) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Concise explanations, HTML snippets, checklists, review findings, and local configuration or memory-note guidance.] <br>
**Output Parameters:** [HTML context, target surface, accessibility target, browser support, markup flavor, security posture, and relevant project or domain notes when available.] <br>
**Other Properties Related to Output:** [Documentation-only helper with disclosed local note storage under ~/Clawic/data/ and no evidence of network transmission in the ClawHub security summary.] <br>

## Skill Version(s): <br>
1.0.2 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
