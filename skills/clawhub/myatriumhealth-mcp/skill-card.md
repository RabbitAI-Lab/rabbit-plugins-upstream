## Description:

Reads a user's MyAtriumHealth patient-portal data from a shell by relaying fpx CLI requests through the user's signed-in Chrome tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically capable users use this skill to access their own MyAtriumHealth records, including test results, medications, allergies, immunizations, visits, goals, and messages, from shell workflows. It is intended for personal-account access through an already signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser-mediated access to a signed-in MyAtriumHealth session can expose highly sensitive health data if the fpx profile or browser extension is trusted too broadly.

Mitigation: Install only after reviewing the fpx package and Transporter extension, keep the profile scoped as narrowly as the tooling allows, and revoke the profile or pairing after use.

Risk: Full portal API responses may contain personal health information and could be accidentally written to logs or files.

Mitigation: Project responses with jq or equivalent filters before display, and avoid storing raw medical responses in shell history, logs, or shared workspaces.

Risk: The cached antiforgery token in MAH_TOKEN can remain available to the shell after a data retrieval task is complete.

Mitigation: Unset MAH_TOKEN when finished and rely on short-lived browser sessions plus fresh sign-in for later use.

## Reference(s):

- [MyAtriumHealth endpoint recipes](artifact/references/endpoints.md)
- [MyAtriumHealth shell helpers](artifact/references/mah.sh)
- [MyAtriumHealth portal](https://my.atriumhealth.org/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and helper function references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return portal API data to stdout; users should project sensitive responses before saving or logging them.]

## Skill Version(s):

0.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
