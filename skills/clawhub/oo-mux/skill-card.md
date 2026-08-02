## Description: <br>
Mux (mux.com). Use this skill for Mux requests that read, create, update, or delete video asset data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to manage Mux video assets through OOMOL, including listing assets, inspecting processing state, creating assets from public media URLs, creating playback IDs, and deleting assets after explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create Mux assets and playback IDs, which changes account state and may affect billing or availability. <br>
Mitigation: Confirm the exact action and payload before write actions and keep the OOMOL-Mux connection scoped to the permissions needed. <br>
Risk: The skill can permanently delete Mux video assets and associated data. <br>
Mitigation: Require explicit user approval for the target asset before running destructive actions. <br>
Risk: The skill operates a connected Mux account through OOMOL credentials. <br>
Mitigation: Install only for intended Mux account operation and review prompts before approving account-changing actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mux) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Mux Homepage](https://www.mux.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
