## Description: <br>
Use AssemblyAI through the OOMOL oo CLI to create, list, retrieve, and delete transcripts without calling the AssemblyAI API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate AssemblyAI transcript workflows from an OOMOL-connected account, including creating transcripts from media URLs and retrieving transcript details, paragraphs, or sentences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create transcripts and delete transcripts in the connected AssemblyAI account. <br>
Mitigation: Confirm write payloads and require explicit approval for destructive transcript deletion before running the action. <br>
Risk: The first-time setup path may run a remote oo CLI installer. <br>
Mitigation: Run the installer only when the oo command is missing and the user trusts OOMOL's installation path. <br>
Risk: Connector inputs may drift from documented examples. <br>
Mitigation: Fetch the live action schema with oo connector schema before constructing each payload. <br>


## Reference(s): <br>
- [AssemblyAI homepage](https://www.assemblyai.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub AssemblyAI skill page](https://clawhub.ai/oomol/skills/oo-assemblyai) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash, PowerShell, JSON, and text blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
