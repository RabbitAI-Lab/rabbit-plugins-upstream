## Description:

Helps coding agents recall reviewed fixes, record fixes learned from failures, and optionally measure their value in controlled experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to retain reviewed coding fixes across agent sessions, recall relevant fixes at the start of a task, and record when a fix helps. An optional experimental workflow compares performance before and after injecting fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored fixes can influence later agent sessions through prompt injection.

Mitigation: Keep manual review enabled, apply only relevant fixes, and prefer project-local hooks over global extensions.

Risk: Optional refinement or sharing can expose sensitive session content or fixes.

Mitigation: Avoid --llm-refine on sensitive sessions without reviewing provider exposure; review content before enabling optional sharing.

Risk: Experimental automation can admit unreviewed fixes, and --fresh clears the global experience store.

Mitigation: Avoid --auto-approve for normal use and verify the backup before running --fresh.

## Reference(s):

- [ClawHub release](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)
- [Pi coding agent](https://github.com/earendil-works/pi)
- [Evolver](https://github.com/EvoMap/evolver)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown and plain-text fix lists with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recall depends on reviewed, relevant fixes already in the local store.]

## Skill Version(s):

0.15.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
