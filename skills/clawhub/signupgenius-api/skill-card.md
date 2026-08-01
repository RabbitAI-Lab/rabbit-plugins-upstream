## Description: <br>
Access SignUpGenius sign-ups, groups, and RSVPs from a shell with curl by logging in with email and password to obtain session credentials and calling the v3 API or legacy dispatcher directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect and manage SignUpGenius account data from scripts or terminals without running the signupgenius-mcp server. It is useful for profile, group, sign-up, public sign-up lookup, and RSVP workflows that can be performed through documented curl requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles SignUpGenius passwords, JWT cookies, and session cookies that can expose account access if left in shell history, environment scope, cookie jars, or temporary header files. <br>
Mitigation: Use the skill only on a trusted single-user machine, prefer a password manager or short-lived shell scope, treat generated cookie and header files as sensitive, and delete them after use. <br>
Risk: Some documented flows can modify account data, including adding group members and submitting RSVP responses. <br>
Mitigation: Confirm the intended write operation with the user and inspect the final curl payload before running commands that change SignUpGenius data. <br>


## Reference(s): <br>
- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell command examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes authenticated and unauthenticated curl patterns, endpoint notes, and session handling guidance.] <br>

## Skill Version(s): <br>
1.2.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
