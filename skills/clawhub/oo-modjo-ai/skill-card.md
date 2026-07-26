## Description: <br>
Provides agent guidance for searching and reading Modjo AI data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill when an agent needs to retrieve Modjo AI account, call, contact, deal, team, user, tag, topic, note, summary, transcript, or next-step data from a connected Modjo AI account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retrieve sensitive Modjo AI data, including call transcripts, contacts, users, and deal information. <br>
Mitigation: Review the Modjo AI permissions on the connected OOMOL account and use the skill only for prompts that actually require Modjo AI data. <br>
Risk: Retrieved CRM and conversation records may contain sensitive business or personal information. <br>
Mitigation: Limit requests to the minimum needed records and avoid exposing retrieved data outside the intended task context. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-modjo-ai) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Modjo AI Homepage](https://www.modjo.ai) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Modjo AI retrieval actions return JSON responses with data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
