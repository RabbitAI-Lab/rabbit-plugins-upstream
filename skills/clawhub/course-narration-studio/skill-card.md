## Description:

Turn lecture manuscripts and course slides into a lecture-by-lecture narration pack with one consistent teacher voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, training teams, and course producers use this skill to prepare lecture text, pronunciation guidance, voice selection or authorized cloning, and ordered lesson narration. It supports a pilot-first workflow before producing the remaining course audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan reports broad Beatra account powers that can spend credits and access multiple media-generation tools, not only narration.

Mitigation: Install only when the publisher and Beatra account access are trusted, keep credentials out of chat and command arguments, and confirm estimates before billable clone or synthesis calls.

Risk: The scan reports that the bundled client can silently replace installed package files through automatic updates.

Mitigation: Use the documented update controls to disable silent checks with `python3 scripts/mcp_client.py update --auto off` when change control is required.

Risk: Voice cloning can misuse a speaker sample without authorization.

Mitigation: Use cloning only after the user states that the voice is theirs or that the speaker authorized this cloning use.

Risk: First use sends package and platform registration metadata.

Mitigation: Expect package slug, version, platform, and installation reference registration metadata to be sent before using the skill.

## Reference(s):

- [Course narration workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/course-narration-studio)
- [Beatra skill homepage](https://beatra.ai/skills/course-narration-studio)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration, Audio artifacts]

**Output Format:** [Markdown guidance with JSON payload examples, shell command blocks, and Beatra task results that may include labeled lesson audio artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports task status, actual usage, billing.net_charged_credits, and ordered lesson delivery details when returned by Beatra.]

## Skill Version(s):

0.1.1 (source: manifest.json and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
