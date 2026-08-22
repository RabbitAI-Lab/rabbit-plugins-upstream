## Description:

This skill helps agents migrate Chinese short-video workflows from Jimeng or Dreamina-style prompts into reusable three-beat storyboards and AI Hive Seedance 2.5 video tasks for text-to-video, image-to-video, reference-video, editing, and extension workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and marketing teams use this skill to plan and run Chinese vertical short-video generation or editing tasks through AI Hive Seedance 2.5. It is especially suited for reusable storyboards, product-introduction clips, reference-guided scenes, cleanup edits, and shot extensions without claiming official Dreamina or Jimeng integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to AI Hive for video generation.

Mitigation: Use only media that is approved, licensed, and appropriate for third-party processing; review AI Hive data-handling terms before using sensitive material.

Risk: The helper stores an AI Hive API key locally when initialized.

Mitigation: Protect the local configuration file, prefer environment or command-line key injection when operationally appropriate, and rotate the key if it may have been exposed.

Risk: Completed outputs are downloaded locally by default.

Mitigation: Use --no-download when local storage of generated outputs is not desired, or set an approved output directory for retained files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/dreamina-video-generation-alternative)
- [AI Hive API endpoint used by the helper](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline bash commands; helper commands return JSON task data and may download generated video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper can upload selected local media to AI Hive, poll generation tasks, and save completed outputs locally unless --no-download is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
