## Description: <br>
Manage Notes, Tasks, Calendar, Files, Contacts, and Deck Kanban boards in your Nextcloud instance via CalDAV, WebDAV, Notes, and Deck APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[keithvassallomt](https://clawhub.ai/user/keithvassallomt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent manage a configured Nextcloud account, including notes, tasks, calendar events, files, contacts, public shares, and Deck boards. It is best suited for account-scoped automation where the user can confirm writes, deletes, and public-share operations before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Nextcloud app password with full account-scope access. <br>
Mitigation: Use a dedicated app password, test with a throwaway account first, and revoke the app password when it is no longer needed. <br>
Risk: Delete, edit, upload, and public-share operations can change or expose account data. <br>
Mitigation: Confirm the exact target and operation with the user before every delete, share, edit, upload, or move command; use the CLI confirmation token where required. <br>
Risk: The package includes unrelated GitHub pull-request authority in local Claude settings. <br>
Mitigation: Remove the unrelated .claude GitHub PR permission before use in environments that honor Claude local settings. <br>
Risk: Server security evidence flags an XML dependency path for review. <br>
Mitigation: Review dependency handling and keep the bundled package current before installation in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/keithvassallomt/skills/openclaw-nextcloud) <br>
- [Project homepage from ClawHub metadata](https://github.com/keithvassallomt/openclaw-nextcloud) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [JSON responses from a Node.js CLI, with Markdown guidance for agent behavior and command usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 20+, NEXTCLOUD_URL, NEXTCLOUD_USER, and NEXTCLOUD_TOKEN; commands perform account-scoped Nextcloud reads and writes.] <br>

## Skill Version(s): <br>
0.3.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
