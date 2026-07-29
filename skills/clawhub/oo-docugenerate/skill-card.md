## Description: <br>
DocuGenerate helps agents read, create, update, and delete DocuGenerate data through the OOMOL-connected DocuGenerate connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to manage DocuGenerate templates and generated documents through an OOMOL-connected account, including listing, retrieval, generation, renaming, and deletion workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or rename DocuGenerate documents through a connected account. <br>
Mitigation: Confirm the exact action, target, and JSON payload with the user before running write actions. <br>
Risk: The skill can permanently delete generated DocuGenerate documents. <br>
Mitigation: Require explicit user approval for the document ID and deletion target before running destructive actions. <br>
Risk: Connector schemas may define required fields or response shapes that change over time. <br>
Mitigation: Fetch the live connector schema before constructing action payloads. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-docugenerate) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [DocuGenerate Homepage](https://www.docugenerate.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs DocuGenerate connector actions through the oo CLI and returns connector JSON responses, including generated document download URLs when available.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
