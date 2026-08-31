## Description:

Skill Publisher helps agents publish completed SKILL.md-based skill folders to public marketplaces by validating metadata, preparing documentation and release notes, cleaning bundle files, running marketplace publish flows, and summarizing results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mebusw](https://clawhub.ai/user/mebusw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to prepare and publish completed Agent Skill folders to public marketplaces, especially ClawHub and skills.sh. It is not intended for local-only skill management, unfinished skill authoring, or standalone guidance for a single marketplace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill can delete local files while cleaning bundles.

Mitigation: Run with dry-run first and use a disposable staging copy of the skill folder before allowing destructive cleanup.

Risk: The security summary says the skill can change global developer settings and patch installed CLI files.

Mitigation: Review every proposed shell command, reject changes to global git config or installed CLI files, and run publishing in an isolated environment.

Risk: The security summary says the skill can publish broadly without enough user control.

Mitigation: Restrict the requested target markets explicitly and confirm each publish request before execution.

Risk: Publishing flows require marketplace tokens and API keys.

Mitigation: Avoid passing tokens visibly on the command line and prefer environment variables or secret stores scoped to the publishing session.

## Reference(s):

- [Server-resolved source repository](https://github.com/mebusw/skill-publisher)
- [ClawHub listing](https://clawhub.ai/mebusw/skills/skill-publisher)
- [ClawHub bundle specification](references/clawhub-bundle.md)
- [ClawHub publishing guide](references/clawhub.md)
- [skills.sh publish guide](references/skills-sh-publish.md)
- [Release notes template](references/release-notes-template.md)
- [SkillHub publishing guide](references/skillhub.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated or updated skill release files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May mutate the target skill folder during non-dry-run publishing by creating documentation, release notes, tags, cleaned bundles, and marketplace publish requests.]

## Skill Version(s):

0.1.1 (source: server release metadata; artifact frontmatter metadata lists 2.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
