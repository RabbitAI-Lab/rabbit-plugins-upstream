## Description: <br>
Glyphic (goairspeed.com). Use this skill for searching and reading Glyphic data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect Glyphic connector schemas and retrieve calls, transcripts, summaries, media metadata, snippets, tags, playbooks, and playbook versions through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retrieve sensitive Glyphic business data, including call transcripts, summaries, media metadata, insights, tags, and playbooks. <br>
Mitigation: Use it only with authorized Glyphic accounts and review retrieved content before sharing it outside the intended workflow. <br>
Risk: First-time setup can require installing the oo CLI, signing in, or reconnecting the Glyphic account. <br>
Mitigation: Run setup only when a command fails with an installation, authentication, connection, or billing error, and confirm account context before retrying. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-glyphic) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Glyphic homepage](https://www.goairspeed.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, json] <br>
**Output Format:** [Markdown guidance with shell command examples; connector actions return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
