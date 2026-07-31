## Description: <br>
Operate Eden AI through an OOMOL-connected account for reading, creating, and updating Eden AI data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate Eden AI through an OOMOL-connected account, including listing available models and creating non-streaming OpenAI-compatible chat completions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Eden AI access is mediated through an OOMOL-connected account. <br>
Mitigation: Install only if that intermediary access model is acceptable for the environment, and review the connected account before use. <br>
Risk: Write actions such as chat completions may consume Eden AI or OOMOL credits. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running write actions. <br>


## Reference(s): <br>
- [Eden AI homepage](https://www.edenai.co) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Guidance, Text] <br>
**Output Format:** [Markdown with inline bash and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the oo CLI to inspect action schemas and run Eden AI connector actions that return JSON data with execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
