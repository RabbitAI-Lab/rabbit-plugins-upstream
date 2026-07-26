## Description: <br>
Operates Bitly through the OOMOL oo CLI for reading Bitly data, creating shortened links, and updating existing Bitlinks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to handle Bitly requests through an OOMOL-connected account, including inspecting user or group data, creating short links, and updating editable Bitlink fields. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update Bitly resources through the user's connected OOMOL Bitly account. <br>
Mitigation: Confirm the exact payload and intended effect before running account-changing actions, including Bitlink updates and link creation. <br>
Risk: The artifact tags update_bitlink as a write action, while security guidance also treats shorten_link as a write because it creates a new link. <br>
Mitigation: Treat shorten_link and update_bitlink as account-changing actions that require user confirmation before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bitly) <br>
- [Bitly Homepage](https://bitly.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses OOMOL server-side injected credentials and requires schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
