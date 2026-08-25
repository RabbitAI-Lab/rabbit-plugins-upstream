## Description:

Use when a talking-head, interview, documentary, or explanatory video needs deliberate transcript-timed visual cutaways from local media or Pexels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-editing agents use this skill to add transcript-timed B-roll cutaways to talking-head, interview, documentary, or explanatory video projects. It supports local media and Pexels-sourced media with explicit review gates before project outputs are changed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow processes local video files and writes review, cache, and render-state artifacts.

Mitigation: Use it only in projects where that local media processing and artifact creation are acceptable, and review generated pages and receipts before final render or registration.

Risk: Pexels access requires a local API key.

Mitigation: Keep the key in the local .env file or environment and do not place it in chat, commands, URLs, logs, plans, review artifacts, or responses.

Risk: Incorrect B-roll choices could make a video misleading or visually inappropriate.

Mitigation: Require the skill's explicit candidate review, approval receipts, verification stills, contact sheet, boundary reel, and final visual review before project outputs are finalized.

## Reference(s):

- [B-Roll Rules](reference/broll-rules.md)
- [Example B-Roll Plan](examples/example-broll-plan.json)
- [Example Candidate Ranking](examples/example-candidate-ranking.json)
- [ClawHub Skill Page](https://clawhub.ai/whitetowerai/skills/video-add-b-roll)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown, Code]

**Output Format:** [Markdown instructions with PowerShell and Python command examples, JSON plan and receipt schemas, and generated review artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [During execution, the workflow can produce JSON plans and receipts, local review HTML, candidate analysis packets, normalized silent video overlays, verification stills, contact sheets, boundary reels, and summary Markdown.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
