## Description:

Open GitHub in the user's Brave browser, reusing an existing GitHub tab or session when possible.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to open GitHub in Brave, reuse an existing session or matching tab, verify the destination, and stop safely at sign-in without handling credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may reuse the user's current GitHub login session in Brave.

Mitigation: Review the loaded browser page before taking account actions, and do not treat page access as authorization to modify account or repository content.

Risk: Authentication may be required before GitHub is usable.

Mitigation: Stop at the login page and let the user sign in; do not enter passwords, authentication codes, API keys, or other credentials.

## Reference(s):

- [GitHub](https://github.com/)
- [ClawHub skill page](https://clawhub.ai/ruchir17-cmd/skills/open-github)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Plain text or Markdown status with browser automation actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Opens or focuses one Brave tab and reports whether GitHub is visibly loaded.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
