## Description: <br>
BaseLinker helps an agent inspect connector schemas and run BaseLinker inventory and order-management actions through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to let an agent work with BaseLinker inventory catalogs, products, warehouses, orders, order statuses, and recent order events through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access business-sensitive BaseLinker order and inventory data through the user's connected account. <br>
Mitigation: Install only when agent access to the OOMOL-connected BaseLinker account is intended, and handle returned order and inventory data as business-sensitive. <br>
Risk: Actions tagged as write or destructive could change BaseLinker state if executed with an incorrect payload. <br>
Mitigation: Inspect the live action schema before constructing payloads and require explicit user confirmation for write or destructive actions. <br>
Risk: Account setup, expired credentials, missing scopes, or billing limits can prevent connector actions from running. <br>
Mitigation: Use the documented first-time setup and connection recovery steps only after an action fails with the matching authentication, connection, scope, or billing error. <br>


## Reference(s): <br>
- [BaseLinker skill page](https://clawhub.ai/oomol/skills/oo-baselinker) <br>
- [BaseLinker homepage](https://baselinker.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an installed, signed-in oo CLI and a connected BaseLinker account.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
