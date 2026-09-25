## Description:

Looks up Zhejiang enterprise registration information by company name or unified social credit code, including operating status, category, industry, establishment date, registration authority, branch information, and coverage notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business review teams use this skill to check Zhejiang enterprise registration records for supplier onboarding, bid preparation, due diligence triage, and company identity verification. It should report both matches and non-matches with coverage boundaries instead of treating a missing result as proof that an entity does not exist.

### Deployment Geography for Use:

Global; registry lookup coverage is limited to Zhejiang Province records.

## Known Risks and Mitigations:

Risk: Company lookup terms and account or session identifiers are sent to the publisher's external service.

Mitigation: Install only when that data sharing is acceptable for the intended workflow, and avoid submitting sensitive queries unless approved.

Risk: Authentication and session data are stored locally in plaintext at ~/.odf/zj-enterprise-registry.json.

Mitigation: Use on protected machines, remove the credential file when no longer needed, and rotate or revoke any API key if the file may have been exposed.

Risk: The security review notes under-disclosed remote service use and recommends review before execution.

Mitigation: Review the script and network behavior before deployment, and communicate the external service dependency to users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/zj-enterprise-registry)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown summary derived from command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill fetches remote HTML, converts it to text, and reports data coverage and non-match boundaries.]

## Skill Version(s):

1.0.2 (source: server release evidence, SKILL.md frontmatter, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
