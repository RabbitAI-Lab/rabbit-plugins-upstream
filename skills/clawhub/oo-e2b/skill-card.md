## Description: <br>
E2B (e2b.dev). Use this skill for ANY E2B request: reading, creating, updating, and deleting data through an OOMOL-connected E2B account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect E2B connector schemas, create sandboxes from templates, list or retrieve sandboxes, and delete sandboxes through the OOMOL `oo` CLI. It is intended for E2B account operations where credentials are managed through OOMOL rather than exposed directly to the agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create E2B sandboxes with unintended templates or parameters. <br>
Mitigation: Inspect the live connector schema and confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: Destructive actions can delete an E2B sandbox by sandbox identifier. <br>
Mitigation: Confirm the target sandbox ID and obtain explicit user approval before running destructive actions. <br>
Risk: Connector operations run through OOMOL rather than directly with a raw E2B API token. <br>
Mitigation: Ensure the user understands that OOMOL manages the credentialed connection and resolve auth, scope, credential, or billing errors through OOMOL setup paths. <br>


## Reference(s): <br>
- [E2B homepage](https://e2b.dev) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-e2b) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
