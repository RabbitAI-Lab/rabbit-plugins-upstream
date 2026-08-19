## Description:

Seedance2.0 Lowest 20% Off Channel helps creators, marketing teams, ecommerce teams, and short-form production teams generate Seedance 2.0 videos through AI Hive from text and optional image, video, or audio references, then submit, track, and download results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, advertising teams, and production teams use this skill to create AI video assets for product demos, social ads, TVC-style clips, short drama, comic drama, and social commerce content. Developers and operators can configure an AI Hive API key, submit generation jobs, upload reference media, query task status, and download generated video files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an AI Hive API key locally and can submit paid generation jobs.

Mitigation: Review API key handling before installation, keep the config file permissions restricted, and confirm expected cost, routing mode, and job count before running generation commands.

Risk: The skill uploads user-provided media paths to AI Hive as part of generation workflows.

Mitigation: Use only media the user intends to upload, avoid sensitive or unauthorized assets, and verify reference files before submitting a job.

Risk: The security summary says the trigger scope is overbroad for a paid API workflow.

Mitigation: Invoke the skill only after the user has clearly chosen AI Hive Seedance generation, especially for comparison, pricing, or migration queries.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/seedance-2-0-lowest-20-percent-off-channel)
- [AI Hive API Key Page](https://ai-hive.iclip.cn/chat)
- [AI Hive API Base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json, files]

**Output Format:** [Markdown guidance with shell commands; helper script output includes JSON task status, media IDs, and downloaded video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key; generated media is saved locally by default under ~/Downloads/AiHive unless another output directory is provided.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata; artifact CHANGELOG top entry is 1.3.0 and should be reviewed)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
