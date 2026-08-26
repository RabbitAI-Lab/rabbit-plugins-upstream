## Description:

Hamsa helps agents search and read Hamsa project, voice agent, and text-to-speech voice data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to operate Hamsa through an OOMOL-connected account, including reading project details, voice agents, and available text-to-speech voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read data from the Hamsa account connected to OOMOL through the oo CLI.

Mitigation: Install and use it only with the intended OOMOL-connected Hamsa account, and review account access expectations before use.

Risk: Setup, authentication, or reconnection commands can change local CLI state or open account connection flows.

Mitigation: Run setup or login steps only after a command fails for the matching auth or connection reason.

Risk: Future connector actions may add write or destructive behavior beyond the current read-only action set.

Mitigation: Review action tags, live schemas, and the exact payload before approving any future write or destructive action.

## Reference(s):

- [ClawHub Hamsa Skill](https://clawhub.ai/oomol/skills/oo-hamsa)
- [Hamsa Homepage](https://tryhamsa.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
