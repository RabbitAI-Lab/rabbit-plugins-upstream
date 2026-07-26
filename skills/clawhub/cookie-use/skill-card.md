## Description: <br>
Cookie Use helps agents manage logged-in website sessions by capturing, storing, listing, switching, and applying saved account sessions across Chrome profiles, isolated browsers, and connected sessions on macOS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeguooooo](https://clawhub.ai/user/leeguooooo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to save, inspect, switch, replay, and share authorized website login sessions across browser contexts. It is intended for workflows that need repeatable account selection or browser automation while preserving session metadata in an encrypted local vault. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give agents broad power to capture, store, share, and apply live website login sessions. <br>
Mitigation: Install and use it only for accounts the operator owns or is authorized to manage, and review planned session actions before execution. <br>
Risk: Bypassing the confirmation gate can allow non-interactive session injection. <br>
Mitigation: Do not use --no-confirm or COOKIE_USE_YES=1 except in tightly controlled automation with approved accounts and targets. <br>
Risk: Replaying production sessions to local or development origins can expose real account access or violate policy. <br>
Mitigation: Avoid replaying production sessions to local or development origins unless explicitly authorized, and prefer test accounts or isolated vaults. <br>
Risk: Shared session bundles can transfer active account access to another person. <br>
Mitigation: Share session bundles only when policy permits, protect the bundle password, and revoke or wipe sessions that should no longer be usable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/leeguooooo/skills/cookie-use) <br>
- [Server-Resolved Source Import](https://github.com/leeguooooo/cookie-use/tree/main/skills/cookie-use) <br>
- [Cookie Use Repository](https://github.com/leeguooooo/cookie-use) <br>
- [chrome-use Dependency](https://github.com/leeguooooo/chrome-use) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces macOS-oriented CLI workflows for capturing, storing, applying, replaying, and sharing browser sessions.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
