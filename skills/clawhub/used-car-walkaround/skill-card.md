## Description:

Turn one used-car condition sheet into a listing hero still and a speakable walkaround script, then turn that still into one used car walkaround clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Used-car dealers use this skill to turn a condition sheet for one named vehicle into a listing hero image, a speakable walkaround script and speech track, and one walkaround video clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious, with incomplete scan evidence and a do-not-install recommendation.

Mitigation: Avoid installation unless the skill is needed; first review its permissions, telemetry, shared-account behavior, and update process as the security guidance recommends.

Risk: The skill uses a Beatra device credential shared across Beatra skills, so its account access may extend beyond this skill.

Mitigation: Review the documented shared-account behavior and authorize only if that access is acceptable; the connection can be revoked from the Beatra Console.

Risk: Installation registration reports installation and coarse runtime details to Beatra.

Mitigation: Review the documented registration fields and decide whether that reporting is acceptable before connecting the skill.

Risk: Uninstall cleanup acts on shared Beatra connection state and could affect other installed Beatra skills.

Mitigation: Run the bundled uninstall script in dry-run mode and inspect its decision; then follow the script's shared-connection decision.

## Reference(s):

- [Beatra skill page](https://beatra.ai/skills/used-car-walkaround)
- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/used-car-walkaround)
- [Workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Updates and security](artifact/references/updates-and-security.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Images, Audio, Video]

**Output Format:** [Labeled listing still, speakable walkaround script and speech track, and one walkaround clip]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One named vehicle per clip; mileage, accident, and maintenance claims are copied from the supplied condition sheet.]

## Skill Version(s):

0.2.5 (source: server-resolved release and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
