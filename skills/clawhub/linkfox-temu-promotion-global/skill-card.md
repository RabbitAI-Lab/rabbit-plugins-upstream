## Description: <br>
Temu Global promotion skill for querying Partner Global promotion activities, candidate goods, enrolled goods, operation results, goods enrollment, goods updates, signed file downloads, and LinkFox/Temu token guidance through LinkFox gateway scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Temu sellers, commerce operators, and their agents use this skill to work with Temu Global promotion campaigns through LinkFox, including promotion discovery, candidate item review, enrollment, update, operation status checks, signed downloads, and token setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles LinkFox API keys and Temu seller access tokens, including optional local token storage. <br>
Mitigation: Use it only in trusted workspaces, avoid inline raw token output, restrict access to token files, and review where tokens are stored before use. <br>
Risk: Enrollment, update, deactivate, signed file download, and generic proxy calls can affect live promotion operations. <br>
Mitigation: Require explicit user confirmation for these operations and verify activity, goods, SKU, price, quantity, and operation type parameters before execution. <br>
Risk: Full API responses may be saved locally and can contain sensitive commerce or account data. <br>
Mitigation: Review saved response locations, limit sharing of generated JSON files, and prefer summarized output unless full response details are needed. <br>
Risk: The generic proxy can call broader Temu API types than the promotion-specific wrappers. <br>
Mitigation: Prefer the promotion-specific scripts when possible and use generic proxy calls only for a clearly identified Temu API type and purpose. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-promotion-global) <br>
- [API reference](references/api.md) <br>
- [Access token guidance](references/access-token.md) <br>
- [Authorization flow](references/authorization-flow.md) <br>
- [Partner Global catalog](references/partner-global-catalog.md) <br>
- [Promotion API index](references/apis/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance, shell command examples, and JSON API responses saved to local files or printed to stdout.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses may be persisted locally by the scripts; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
