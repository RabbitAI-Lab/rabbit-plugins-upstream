## Description: <br>
Leonardo.Ai (leonardo.ai). Use this skill for ANY Leonardo.Ai request: reading, creating, and updating data through the OOMOL Leonardo.Ai connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Leonardo.Ai through an OOMOL-connected account, including creating generation jobs, retrieving generation status and generated image URLs, and listing production API models with their parameter schemas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generation actions can spend credits or change Leonardo.Ai account state. <br>
Mitigation: Review and confirm the exact create_generation payload before approving execution. <br>
Risk: Setup and login commands can modify local authentication state or open account connection flows. <br>
Mitigation: Run setup, login, or connection steps only when the oo CLI or Leonardo.Ai connection is actually missing or expired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-leonardo-ai) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Leonardo.Ai homepage](https://leonardo.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the oo CLI to inspect connector schemas and run Leonardo.Ai connector actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
