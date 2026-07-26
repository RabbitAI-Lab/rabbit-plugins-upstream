## Description: <br>
ConvertAPI helps agents operate the ConvertAPI PDF-to-DOCX conversion workflow through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect ConvertAPI connector schemas and run the supported PDF-to-DOCX conversion action through OOMOL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the OOMOL oo CLI, an OOMOL account connection to ConvertAPI, and available billing credits. <br>
Mitigation: Install and authenticate the CLI only when required, connect ConvertAPI once, and resolve billing errors before retrying conversion commands. <br>
Risk: Future expanded actions may write, overwrite, delete, or spend credits. <br>
Mitigation: Confirm the exact payload and effect with the user before running actions tagged write or destructive, and use the live schema before execution. <br>


## Reference(s): <br>
- [ConvertAPI homepage](https://www.convertapi.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution; conversion responses include temporary download URLs and an execution id.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
