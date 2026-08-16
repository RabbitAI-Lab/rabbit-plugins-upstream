## Description:

China patents skill for mining patent points, drafting invention, utility-model, and design disclosures, producing plain-language patent readings, tracking policy signals, and assisting office-action responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomestwei](https://clawhub.ai/user/handsomestwei)

### License/Terms of Use:

MIT-0

## Use Case:

External patent practitioners, inventors, and developers use this skill to turn technical project material or patent documents into patent disclosure drafts, patent reading notes, prior-art search summaries, and office-action response drafts. The skill is oriented to China patent workflows and includes optional Obsidian-based knowledge organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles confidential patent materials, office-action documents, and local knowledge-base files.

Mitigation: Use an isolated workspace, back up the Obsidian vault before first use, and point the skill only at directories the user is comfortable letting the agent read or modify.

Risk: The security evidence warns that dependency and document-processing behavior should be reviewed before installing or processing untrusted documents.

Mitigation: Install in an isolated virtual environment and pin or upgrade flagged dependencies before handling untrusted files.

Risk: The skill may require API keys or embedding configuration for office-action retrieval workflows.

Mitigation: Avoid pasting API keys into chat or shell history; prefer environment variables or a local secret store, and keep vector embedding disabled or local for confidential patent material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomestwei/skills/patent-disclosure-skill)
- [Publisher profile](https://clawhub.ai/user/handsomestwei)
- [Installation guide](INSTALL.md)
- [Obsidian setup guide](docs/obsidian-setup-guide.md)
- [Office-action workflow documentation](docs/oa/README.md)
- [Formula paradigms reference](references/formulas/paradigms.yaml)
- [Patent type search reference](references/patent_type_search.yaml)
- [Patent Obsidian format reference](references/patent_obsidian_format.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, structured text, YAML/JSON configuration, shell commands, and generated document files such as DOCX when supporting tools are used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local project, output, and Obsidian vault files when the user directs the agent to run the workflow.]

## Skill Version(s):

3.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
