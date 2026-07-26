## Description: <br>
Analyzes pet face image or video inputs, identifies the pet, checks linked vaccination records against the current date, and returns due or overdue vaccination reminder results without providing medical advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet hospital staff, boarding center operators, and pet insurance reviewers use this skill to check whether a known pet's vaccination record is due or overdue from pet face media and linked records. The skill is intended for database comparison and reminder workflows, not veterinary medical advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet media, identity-linked request data, and vaccination or report history may be sent to the configured Life Emergence cloud services. <br>
Mitigation: Install only in environments where the publisher and cloud service are trusted, and confirm consent, tenant scoping, data retention, and access policies before use. <br>
Risk: The skill can silently create or reuse identities and store service tokens locally. <br>
Mitigation: Review local workspace database and token storage behavior, isolate deployments by tenant or account, and rotate or revoke tokens when access changes. <br>
Risk: Historical report lookup can expose prior vaccination analysis results and report links with weak user control. <br>
Mitigation: Restrict who can trigger history lookup, verify identity scoping before enabling the skill, and audit access to generated report links. <br>


## Reference(s): <br>
- [Pet vaccination reminder API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands] <br>
**Output Format:** [Markdown or JSON analysis results with report links for completed cloud analyses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write results to a user-specified output file and can return historical report lists from the configured cloud service.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
