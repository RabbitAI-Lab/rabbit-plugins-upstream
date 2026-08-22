## Description:

Turn a script, scene, or ad brief into a structured AI storyboard plan with a practical shot list and one to four storyboard key-frame images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative teams, marketers, filmmakers, animators, and agent users use this skill to turn scripts, scenes, and ad briefs into reviewable shot plans. After user approval, it can help create one to four storyboard key frames through Beatra image-generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the skill uses a broad reusable Beatra device credential.

Mitigation: Use the bundled authorization flow, keep the token only in the private credential file, never expose it in chat, logs, arguments, or environment variables, and revoke the device from the Beatra Console or uninstall flow when access is no longer needed.

Risk: The release security summary says the bundled client silently self-updates local package code by default.

Mitigation: Review the automatic update behavior before install, use the provided update command to disable automatic checks when appropriate, and rely on the documented verification of discovery data, archives, manifests, and packaged files.

Risk: Storyboard key-frame generation can create paid Beatra tasks and duplicate charges if recovery is handled incorrectly.

Mitigation: Freeze the approved payload before submission, use one stable client request ID per paid key frame, do not resubmit queued or running tasks, and retry uncertain submissions only with the identical request identity and arguments.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/ai-storyboard-generator)
- [Beatra skill homepage](https://beatra.ai/skills/ai-storyboard-generator)
- [Storyboard planning and key frames](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured shot lists, prompts, command examples, and returned artifact summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task IDs, resolved model details, dimensions, format, usage, and billed credits when returned by the task API.]

## Skill Version(s):

0.1.4 (source: server release evidence and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
