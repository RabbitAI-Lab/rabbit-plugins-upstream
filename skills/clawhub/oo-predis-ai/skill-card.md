## Description: <br>
Predis.ai (predis.ai). Use this skill for ANY Predis.ai request - reading, creating, and updating data. Whenever a task involves Predis.ai, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a connected Predis.ai account through OOMOL for listing posts and templates, and for creating content generation requests after confirming write payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create content in a user's Predis.ai account through the create_content action. <br>
Mitigation: Review the exact create_content payload and expected effect with the user before running the write action. <br>
Risk: First-time CLI installation, login, or account connection steps grant Codex access to operate the user's Predis.ai account through OOMOL. <br>
Mitigation: Run setup steps only after an auth or connection failure and only when the user trusts OOMOL and wants the connector enabled. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-predis-ai) <br>
- [Predis.ai homepage](https://predis.ai) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo CLI connector actions and returns connector responses containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
