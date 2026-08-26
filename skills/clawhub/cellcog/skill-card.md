## Description:

CellCog guides agents to use a third-party multimodal sub-agent for research, media generation, documents, dashboards, code, and other deliverables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to offload complex multimodal work to CellCog, including analysis, generated files, creative assets, code, and iterative follow-up tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tagged local files may be uploaded to the third-party CellCog service, including sensitive content if the wrong path is selected.

Mitigation: Only tag files intended for upload and exclude credentials, private keys, .env files, SSH keys, and other secrets.

Risk: Browser, co-work, and connected SaaS tool modes can grant broad access to local or account resources.

Mitigation: Enable browser or co-work modes only when needed and select narrow connected toolkits instead of enabling all tools.

Risk: Generated artifacts or task responses may be incomplete, costly, or require follow-up review.

Mitigation: Review the full CellCog response, generated file paths, credit usage, and follow-up instructions before relying on outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cellcog/skills/cellcog)
- [CellCog Homepage](https://cellcog.ai)
- [CellCog Python SDK](https://github.com/CellCog/cellcog_python)
- [CellCog PyPI Package](https://pypi.org/project/cellcog/)
- [DeepResearch Bench Leaderboard](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with Python and shell snippets; CellCog task results may include generated files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and CELLCOG_API_KEY; tagged local files may be uploaded to CellCog for processing.]

## Skill Version(s):

2.0.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
