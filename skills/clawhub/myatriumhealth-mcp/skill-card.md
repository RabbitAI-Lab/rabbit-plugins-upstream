## Description:

Read MyAtriumHealth data, including test results, medications, allergies, immunizations, health issues, visits, and goals, from a shell through the fpx CLI by relaying requests through the user's signed-in Chrome tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically proficient users use this skill to script or inspect their own MyAtriumHealth patient-portal data from a shell while relying on an already signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser relay access can reach sensitive MyAtriumHealth session data.

Mitigation: Grant access only when needed, revoke the browser pairing after use, and avoid leaving a signed-in portal tab available to unreviewed commands.

Risk: Helper commands can print personal health information to stdout or downstream shell tools.

Mitigation: Project responses to the minimum fields needed, avoid storing full responses or tokens, and keep shell history and logs from capturing sensitive output.

Risk: Generic helper calls can target authenticated portal endpoints beyond the documented recipes.

Mitigation: Run only reviewed endpoint calls and prefer pinned dependency versions for the fpx CLI and browser relay tooling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [MyAtriumHealth portal](https://my.atriumhealth.org/myatriumhealth)
- [MyAtriumHealth endpoints](references/endpoints.md)
- [MyAtriumHealth shell helpers](references/mah.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, helper usage examples, and jq projections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce sensitive health data on stdout when the user runs the referenced helper commands.]

## Skill Version(s):

0.4.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
