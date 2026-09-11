## Description:

Music Memory helps agents store and recall practice recordings, chord progressions, technique work, and lesson notes with BlueColumn-backed musical context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Musicians, instructors, and agents supporting music practice use this skill to log recordings and lesson notes with musical metadata, then recall progress, recurring technique issues, and drill plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Practice recording URLs, lesson notes, and musical metadata may include personal or student information sent to BlueColumn/Supabase.

Mitigation: Use only with consent for any recorded or coached person, and avoid sensitive personal details unless BlueColumn privacy and retention terms meet the deployment requirements.

## Reference(s):

- [Music Memory ClawHub Skill Page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/music-memory)
- [BlueColumn agent-remember endpoint](https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1/agent-remember)
- [BlueColumn agent-recall endpoint](https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1/agent-recall)
- [BlueColumn agent-note endpoint](https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1/agent-note)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline bash code blocks and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BLUECOLUMN_API_KEY; sends user-provided practice recording URLs, lesson notes, and musical metadata to the disclosed BlueColumn/Supabase service.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
