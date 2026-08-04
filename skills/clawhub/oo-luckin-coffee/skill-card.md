## Description: <br>
Luckin Coffee (open.lkcoffee.com). Use this skill for ANY Luckin Coffee request - searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to operate a connected Luckin Coffee account through OOMOL, including store lookup, product search, product details, order previews, order status checks, order creation, and cancellation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create real Luckin Coffee orders that may require payment. <br>
Mitigation: Preview the order first and require explicit user confirmation of the exact payload and expected effect before calling createOrder. <br>
Risk: The skill can cancel real Luckin Coffee orders, which may be irreversible. <br>
Mitigation: Confirm the exact order with the user before calling cancelOrder and treat cancellation as a destructive action. <br>
Risk: The skill summary emphasizes searching and reading data even though security evidence identifies write capabilities. <br>
Mitigation: Treat createOrder and cancelOrder as state-changing capabilities regardless of the read-only wording in the summary. <br>


## Reference(s): <br>
- [Luckin Coffee MCP](https://open.lkcoffee.com/mcp) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-luckin-coffee) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a connected OOMOL Luckin Coffee account for live actions; write actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
