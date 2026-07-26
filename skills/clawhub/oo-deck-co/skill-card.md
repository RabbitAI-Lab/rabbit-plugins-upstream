## Description: <br>
Deck.co lets agents read, create, and update Deck.co data through an OOMOL-connected account instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Deck.co through an OOMOL-connected account, including listing or retrieving agents and sources, testing API-key access, and creating website sources after confirming write payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions may expose Deck.co account data to the agent. <br>
Mitigation: Install and use this skill only when the agent is expected to access the connected Deck.co account. <br>
Risk: The create_source action can modify Deck.co state. <br>
Mitigation: Confirm the exact URL, display name, payload, and expected effect with the user before running write actions. <br>
Risk: First-time CLI setup or account connection can affect authentication state. <br>
Mitigation: Run setup or connection steps only after an auth or connection error indicates they are needed. <br>


## Reference(s): <br>
- [ClawHub Deck.co skill page](https://clawhub.ai/oomol/skills/oo-deck-co) <br>
- [Deck.co homepage](https://www.deck.co) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read actions can return Deck.co account data; write actions require user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
