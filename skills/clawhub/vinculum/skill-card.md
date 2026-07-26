## Description: <br>
Shared consciousness between Clawdbot instances. Links multiple bots into a collective, sharing memories, activities, and decisions in real-time over local network using Gun.js P2P sync. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koba42corp](https://clawhub.ai/user/koba42corp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and teams use this skill to link multiple Clawdbot instances on a trusted local network so they can share memory, activity, decisions, status, and manual notes in near real time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill shares bot memory, activity, decisions, status, and manual notes with other linked Clawdbot instances. <br>
Mitigation: Install it only for trusted instances that intentionally need shared state, and review what categories are enabled before joining a collective. <br>
Risk: Network protections are weaker than the artifact descriptions suggest. <br>
Mitigation: Use only private, trusted networks; avoid public or untrusted networks; and stop the relay when it is not needed. <br>
Risk: Pairing codes and local configuration can grant access to shared collective data. <br>
Mitigation: Treat pairing codes and the local config as sensitive material, share codes through a secure channel, and rotate or recreate the collective if a code is exposed. <br>
Risk: The advertised encryption should not be relied on until fixed or independently verified. <br>
Mitigation: Do not share sensitive credentials or high-risk content through the collective, and independently verify encryption before using it for confidential data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/koba42corp/skills/vinculum) <br>
- [Gun.js](https://gun.eco) <br>
- [Clawdbot](https://clawd.bot) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown responses with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces /link command guidance, status summaries, shared-note confirmations, relay instructions, and local configuration updates.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
