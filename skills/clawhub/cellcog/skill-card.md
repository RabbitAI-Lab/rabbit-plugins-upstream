## Description:

Any-to-any AI sub-agent — research, images, video, audio, music, podcasts, avatars, voice cloning, documents, spreadsheets, dashboards, 3D models, diagrams, and code in one request. Agent-to-agent protocol with multi-step iteration for high accuracy. #1 on DeepResearch Bench (Apr 2026) — deep reasoning meets all modalities, so all your work gets done, not just code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to delegate multimodal research, analysis, generation, coding, and document tasks to the CellCog remote AI sub-agent. It provides setup, authentication, file-sharing, task creation, and result-handling guidance for CellCog SDK workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly wrapped in SHOW_FILE tags are sent to CellCog.

Mitigation: Share only files intended for CellCog processing, and exclude secrets, private keys, .env files, credentials, and other sensitive material.

Risk: Full result messages may expose generated file paths, credit usage, or follow-up details in shared or logged environments.

Mitigation: Review full result messages in an appropriate environment and redact sensitive details before sharing logs or transcripts.

## Reference(s):

- [CellCog skill page](https://clawhub.ai/cellcog/skills/cellcog)
- [CellCog homepage](https://cellcog.ai)
- [CellCog Python SDK](https://github.com/CellCog/cellcog_python)
- [cellcog Python package](https://pypi.org/project/cellcog/)
- [DeepResearch Bench Leaderboard](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with Python and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe generated artifacts, downloaded file paths, credit usage, status, and follow-up instructions returned by CellCog.]

## Skill Version(s):

2.0.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
