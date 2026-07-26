## Description: <br>
Checks Base tokens before trading with buy/sell honeypot simulation, liquidity checks, and ownership-risk checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[true402](https://clawhub.ai/user/true402) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, traders, and trading agents use this skill to check Base ERC-20 tokens before buying, approving, or adding them to an autonomous trading flow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid checks can require a private key in the CLI environment. <br>
Mitigation: Use the free mode when possible; for paid checks, use a dedicated low-balance Base wallet and never print, echo, or log the key. <br>
Risk: Token safety verdicts are point-in-time and cannot guarantee that liquidity or ownership risk will not change later. <br>
Mitigation: Recheck immediately before trading or approval, report the returned reasons, and treat OK as a risk signal rather than financial advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/true402/skills/true402-token-safety) <br>
- [true402 homepage](https://true402.dev) <br>
- [true402 API documentation](https://true402.dev/docs/api) <br>
- [true402 OpenAPI specification](https://true402.dev/openapi.json) <br>
- [Live token check](https://true402.dev/check) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and verdict summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Verdicts use AVOID, CAUTION, or OK with a score, reasons, and scriptable exit codes.] <br>

## Skill Version(s): <br>
1.1.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
