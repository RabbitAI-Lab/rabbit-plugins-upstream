## Description:

Helps creators extend one short video before or after its existing action while checking visual and audio continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video editors use this skill to add a lead-in or natural continuation to a single source clip, then review the join, motion, subject, lighting, audio, and final duration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent device authorization can spend credits and access broad Beatra media and task tools.

Mitigation: Install only if you trust Beatra, confirm the estimate before paid generation, and revoke the device authorization in the Beatra Console when finished.

Risk: The skill can update its local code automatically without separate confirmation.

Mitigation: Review the package before installation and disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if you need to approve changes manually.

## Reference(s):

- [ClawHub release](https://clawhub.ai/beatra-ai/skills/ai-video-continuation)
- [Beatra skill page](https://beatra.ai/skills/ai-video-continuation)
- [Video continuation workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Video artifact links, Guidance]

**Output Format:** [Markdown with video artifact links and task details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports available task status, final duration, model, usage, and net charged credits.]

## Skill Version(s):

0.2.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
