## Description: <br>
Control Tesla vehicles for status checks, locking and unlocking, climate, charging, location, honk, flash, and wake actions through Tesla account access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mvanhorn](https://clawhub.ai/user/mvanhorn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect and operate Tesla vehicles tied to their Tesla account, including multi-vehicle status, lock, climate, charge, location, honk, flash, and wake workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can issue actions that affect a real vehicle. <br>
Mitigation: Review the intended command and verify the targeted vehicle before lock, unlock, climate, charge, honk, flash, or wake actions. <br>
Risk: Vehicle location output can expose private location data. <br>
Mitigation: Treat location responses as private and avoid sharing or retaining them outside the trusted agent session. <br>
Risk: Tesla access tokens are cached locally. <br>
Mitigation: Use the skill only on a trusted machine and remove or revoke the local Tesla token cache when access is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Tesla skill page](https://clawhub.ai/mvanhorn/skills/tesla) <br>
- [Tesla Fleet API documentation](https://developer.tesla.com/docs/fleet-api) <br>
- [Tesla Owner API documentation](https://tesla-api.timdorr.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; command output is plain text with optional JSON for status data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TESLA_EMAIL and stores a local Tesla token cache at ~/.tesla_cache.json.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
