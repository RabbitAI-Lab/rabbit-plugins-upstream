## Description: <br>
Operate WebinarJam through an OOMOL-connected account to read webinar data and register users with the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and operators use this skill to list WebinarJam webinars, inspect webinar details, list registrants or attendees, and register users through an authenticated OOMOL connection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read WebinarJam account data and register users through a connected OOMOL account. <br>
Mitigation: Use only the intended authenticated account and confirm registration payloads before running write actions. <br>
Risk: First-time CLI install or login steps establish trust in OOMOL tooling and account access. <br>
Mitigation: Run setup steps only after an auth, connection, or missing-CLI error and only when the user trusts OOMOL for the task. <br>
Risk: Connector action contracts can change, making stale payloads incorrect. <br>
Mitigation: Inspect the live connector schema before constructing each action payload. <br>


## Reference(s): <br>
- [WebinarJam homepage](https://webinarjam.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub WebinarJam skill page](https://clawhub.ai/oomol/skills/oo-webinarjam) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are returned as JSON when commands are run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
