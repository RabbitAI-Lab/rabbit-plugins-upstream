## Description: <br>
Use this skill for Readwise requests that read, create, or update data through the OOMOL Readwise connector instead of calling the Readwise API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Readwise through an OOMOL-connected account, including exporting highlights, listing books or Reader documents, saving URLs, creating highlights, and updating Reader document metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OOMOL acts as the intermediary for account-scoped Readwise actions. <br>
Mitigation: Install and use this skill only when the user is comfortable authorizing OOMOL for the connected Readwise account. <br>
Risk: Write actions can create highlights, save Reader documents, or update Reader document metadata, tags, or location. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running any create, save, or update action. <br>
Risk: First-time setup commands can install the oo CLI or initiate account connection flows. <br>
Mitigation: Run installation, login, or connection steps only after an auth or connection failure and only when the user intentionally wants the integration configured. <br>


## Reference(s): <br>
- [ClawHub Readwise skill page](https://clawhub.ai/oomol/skills/oo-readwise) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Readwise homepage](https://readwise.io) <br>
- [OOMOL Readwise connection](https://console.oomol.com/app-connections?provider=readwise) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md metadata.version and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
