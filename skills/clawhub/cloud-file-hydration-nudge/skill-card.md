## Description: <br>
Hydrate visible but unreadable cloud placeholder files with provider-aware read verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[talonpoint](https://clawhub.ai/user/talonpoint) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill to safely handle cloud-synced placeholder files by proving unreadability, selecting a provider-aware hydration path, and verifying readable bytes before downstream parsing or import. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud placeholder metadata can look available even when file bytes are unreadable. <br>
Mitigation: Require a bounded read probe before and after hydration, and continue downstream only after the same read succeeds. <br>
Risk: Provider UI automation or privacy permissions can broaden access beyond the target file. <br>
Mitigation: Use provider-native or narrowly approved helper workflows first, keep broad runtime permissions constrained, and leave files pending when approved helpers are unavailable. <br>
Risk: Changing paused, offline, or quit sync state can alter user-controlled provider behavior. <br>
Mitigation: Stop and ask for explicit consent before starting, resuming, or changing provider sync state. <br>


## Reference(s): <br>
- [Release Notes 1.1.0](references/release-notes-1.1.0.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/talonpoint/skills/cloud-file-hydration-nudge) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline bash and Swift code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes bounded read probes, provider-specific nudge guidance, permission boundaries, and compact verification notes.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
