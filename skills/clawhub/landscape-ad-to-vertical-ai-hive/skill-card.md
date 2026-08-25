## Description:

This skill helps brands, merchants, and production teams convert authorized 16:9 advertising, TVC, and launch footage into 9:16 social video plans, commands, AI-HIVE generation tasks, and delivery checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, brand teams, and developers use this skill to plan, process, and generate vertical commercial videos from authorized horizontal source material. It produces reviewable briefs, editing commands, AI-HIVE task records, and acceptance checks before any potentially paid generation step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads user-selected media to AI-HIVE and may submit paid generation tasks.

Mitigation: Use only media the user is allowed to upload, review the prompt, selected model, routing mode, and pricing snapshot before generation, and run a small sample before batch work.

Risk: Local API key configuration can expose credentials if mishandled.

Mitigation: Prefer environment variables or the script's protected config file, keep the key out of logs and repositories, and remove local credentials when no longer needed.

Risk: Generated or reframed advertisements can remove important disclosures or create unsupported product claims.

Mitigation: Preserve required statements, marks, and safety regions; mark unverified claims for review; and have a human approve facts, rights, and platform compliance before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/landscape-ad-to-vertical-ai-hive)
- [AI-HIVE entry point](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with inline shell commands, optional JSON task records, and generated or edited media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local blueprint JSON, ffmpeg-derived video outputs, AI-HIVE media uploads, task IDs, status records, and downloaded generation results.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
