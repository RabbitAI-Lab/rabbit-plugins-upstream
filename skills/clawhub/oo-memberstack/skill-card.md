## Description: <br>
Operate Memberstack through an OOMOL-connected account for reading, creating, updating, deleting, and verifying member data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Memberstack member records through the OOMOL memberstack connector, including member lookup, listing, creation, update, plan changes, deletion, and JWT verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create, update, plan-change, and delete actions can change or permanently remove Memberstack member data. <br>
Mitigation: Review the exact action payload and intended effect with the user before approving state-changing or destructive operations. <br>
Risk: The skill operates through the user's OOMOL-connected Memberstack account. <br>
Mitigation: Install and use it only when the user wants Codex to manage Memberstack through that connected account. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-memberstack) <br>
- [Memberstack homepage](https://www.memberstack.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL Memberstack connection](https://console.oomol.com/app-connections?provider=memberstack) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses are JSON with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
