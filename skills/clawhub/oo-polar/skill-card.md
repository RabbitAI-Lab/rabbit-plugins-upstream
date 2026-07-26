## Description: <br>
Polar (polar.sh). Use this skill for ANY Polar request - reading, creating, and updating data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect Polar schemas and operate Polar customer, order, organization, product, and subscription workflows through the OOMOL oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions may expose Polar customer, order, subscription, and organization information to the agent. <br>
Mitigation: Install only when agent access to Polar account data is intended, and review OOMOL connection scopes when narrower access is required. <br>
Risk: State-changing Polar actions can affect account data if run with an incorrect payload. <br>
Mitigation: Inspect the live connector schema before constructing payloads and confirm the exact payload and effect with the user before write or destructive actions. <br>


## Reference(s): <br>
- [Polar homepage](https://polar.sh) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live schema inspection steps and user confirmation guidance for state-changing Polar actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
