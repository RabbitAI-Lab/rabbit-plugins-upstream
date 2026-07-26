## Description: <br>
Retrieves Steam inventory data for a user from steamcommunity.com. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluesyparty-src](https://clawhub.ai/user/bluesyparty-src) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to retrieve and inspect Steam Community inventory JSON for a Steam account or common game inventories using curl and jq. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Steam session cookies can grant access to a browser session if exposed. <br>
Mitigation: Treat STEAM_COOKIES like a password: do not share it, log it, commit it, or leave it in persistent shell history, and sign out of Steam or invalidate the session if it may have been exposed. <br>
Risk: Repeated inventory requests can trigger Steam Community rate limits or temporary IP bans. <br>
Mitigation: Use the authenticated cookie only for appropriate inventory requests and wait at least 4 seconds between pages or inventory fetches. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bluesyparty-src/skills/steam-community-inventory) <br>
- [Steam Community developer site](https://steamcommunity.com/dev) <br>
- [steamid.io SteamID lookup](https://steamid.io) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and jq examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, STEAM_ID, and STEAM_COOKIES; command output is Steam inventory JSON.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
