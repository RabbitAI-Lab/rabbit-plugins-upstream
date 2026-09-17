## Description:

Read MyAtriumHealth, Atrium Health's Epic MyChart patient portal, from a shell with the fpx CLI by relaying requests through a signed-in Chrome tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable users use this skill to query their own MyAtriumHealth data, including test results, medications, allergies, immunizations, health issues, visits, goals, and messages, from scripts or one-shot shell workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser-session access can expose sensitive health information to third-party tooling.

Mitigation: Install only if you are comfortable granting the CLI and Chrome extension access to the signed-in MyAtriumHealth session; pin or audit the tooling where possible and disable the pairing and extension when finished.

Risk: The profile setup uses broad scope for the Atrium Health domain.

Mitigation: Limit the browser profile and extension grant to the exact portal host where possible, and avoid exporting tokens or raw personal health responses beyond the local shell workflow.

Risk: Expired sessions, missing tabs, or disconnected extension pairing can produce empty or misleading responses.

Mitigation: Run the provided session check before data reads and reconnect the browser tab, sign in again, or re-pair the bridge when the helper reports a signed-out or empty relay condition.

## Reference(s):

- [MyAtriumHealth endpoints - verified recipes](references/endpoints.md)
- [MyAtriumHealth helper shell functions](references/mah.sh)
- [MyAtriumHealth portal](https://my.atriumhealth.org/myatriumhealth)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces shell-oriented guidance for fetching and projecting JSON responses from a signed-in MyAtriumHealth browser session.]

## Skill Version(s):

0.4.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
