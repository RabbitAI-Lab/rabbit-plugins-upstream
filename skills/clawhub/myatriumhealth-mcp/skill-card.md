## Description:

Read MyAtriumHealth, Atrium Health's Epic MyChart patient portal, from a shell with the fpx CLI by relaying requests through the user's signed-in Chrome tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve their own MyAtriumHealth/MyChart records from a signed-in Chrome session for shell scripts or one-shot analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive health information from the user's signed-in MyAtriumHealth session.

Mitigation: Treat MAH_TOKEN and command output as sensitive health information, avoid saving raw responses or shell logs, and sign out when finished.

Risk: The fpx bridge relays requests through a trusted browser session.

Mitigation: Install only when this relay behavior is intended, review the declared profile scope before pairing, and remove the fpx profile or Transporter trust when no longer needed.

Risk: Expired sessions or missing browser tabs can produce login pages, empty responses, or empty JSON results.

Mitigation: Use mah_signed_in before relying on results and re-authenticate or reopen the MyAtriumHealth tab when the helper reports a missing or expired session.

## Reference(s):

- [MyAtriumHealth skill page](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [MyAtriumHealth portal](https://my.atriumhealth.org/myatriumhealth)
- [Endpoint recipes](references/endpoints.md)
- [Shell helpers](references/mah.sh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and shell helper functions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can output JSON API responses containing sensitive personal health information; project responses with jq and avoid storing raw output.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
