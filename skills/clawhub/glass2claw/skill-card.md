## Description: <br>
Routes user-selected photos from Meta Ray-Ban glasses or another camera through a configured messaging ingress to an approved specialist and destination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathanjing](https://clawhub.ai/user/jonathanjing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users with a configured camera and messaging ingress use this skill to route explicitly selected photos to allowlisted specialist agents and destinations such as databases or channels. It is intended for visible, consent-based photo routing with confirmation before cross-session forwarding or persistent writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can post photos externally or write durable database entries. <br>
Mitigation: Keep automatic routing disabled unless a named destination is allowlisted, and require confirmation before any Discord post, cross-session forwarding, or database write. <br>
Risk: Photos may contain people, locations, business cards, bystanders, or other sensitive identifiers. <br>
Mitigation: Route only photos the user intentionally submitted, show the category and destination before acting, and avoid routing third-party or sensitive photos without appropriate consent. <br>
Risk: Incorrect or inferred destinations could send images to the wrong participant, session, channel, or database. <br>
Mitigation: Use only preconfigured destination session keys and exact allowlisted routes; ask for clarification when intent or category is ambiguous. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jonathanjing/skills/glass2claw) <br>
- [ClawHub package homepage](https://clawhub.ai/jonathanjing/glass2claw) <br>
- [README](artifact/README.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>
- [Vision Hub sample routing logic](artifact/SAMPLE_AGENT.md) <br>
- [Wine Specialist sample persona](artifact/SAMPLE_SOUL_WINE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and sample agent configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces routing instructions and sample specialist-agent behavior; it does not include credentials or destination keys.] <br>

## Skill Version(s): <br>
2.3.4 (source: server evidence, SKILL.md frontmatter, skill.json, CHANGELOG released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
