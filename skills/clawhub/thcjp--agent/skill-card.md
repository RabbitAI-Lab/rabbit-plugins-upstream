## Description: <br>
Defines an agent's identity, personality, voice, and boundaries to help create consistent assistant behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to define persona, tone, behavioral boundaries, and basic operating expectations for conversational agents. It is not intended for high-certainty critical decisions without human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad filesystem write and shell execution permissions that are not clearly scoped to persona definition. <br>
Mitigation: Install with constrained filesystem and shell permissions, and review generated actions before execution. <br>
Risk: The artifact includes API-key setup guidance, which can expose credentials if handled carelessly. <br>
Mitigation: Use environment variables or platform secret storage, avoid committing secrets, and limit credentials to the minimum required scope. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Markdown, Shell commands] <br>
**Output Format:** [Markdown instructions with optional JSON response examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May request filesystem, shell, and API-key handling capabilities from the host agent.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
