## Description:

Turns a dealer-provided used-car condition sheet into a listing still and walkaround script, then generates a short narrated walkaround clip after approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Used-car dealers use this skill to turn their condition sheets into listing-ready visuals and a spoken walkaround, then generate one short video for a named vehicle after approving paid generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Beatra grants broader shared account authority than this vehicle-listing task requires.

Mitigation: Review the full authorization scope and connect only if that broader access is acceptable.

Risk: A reusable Beatra credential is stored locally.

Mitigation: Protect access to the device and disconnect or remove the credential when no longer needed.

Risk: Automatic updates can silently replace the skill's executable package files.

Mitigation: Review updates before installing, or disable automatic updates using the documented `update --auto off` command.

Risk: Approved image, speech, and video generation spends Beatra credits.

Mitigation: Review the current price and each approval card before authorizing paid work; avoid resubmitting an uncertain request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/used-car-walkaround)
- [Beatra skill homepage](https://beatra.ai/skills/used-car-walkaround)
- [Used-car walkaround workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Images, Audio, Video]

**Output Format:** [Listing plan and spoken script in text, followed by a generated still, speech track, and short video clip]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One named car per clip; paid generation requires separate approval for the still and speech, then the video.]

## Skill Version(s):

0.1.7 (source: server-resolved release and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
