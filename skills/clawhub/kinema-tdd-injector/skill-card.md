## Description: <br>
Generates or upgrades repository-level CLAUDE.md or AGENTS.md instructions that encode Kinema's TDD methodology for Python and TypeScript/JavaScript projects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeshunee](https://clawhub.ai/user/leeshunee) <br>

### License/Terms of Use: <br>
GNU General Public License v3.0 <br>


## Use Case: <br>
Developers use this skill to initialize or upgrade repository testing guidance before normal development. It collects project details, renders a TDD instruction file, and helps merge it with existing persistent agent instructions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make persistent repository-level agent instruction changes that affect future coding sessions. <br>
Mitigation: Confirm the target repository and review the generated CLAUDE.md or AGENTS.md diff before keeping or committing it. <br>
Risk: Optional migrations and configuration edits can rename test directories or alter project configuration. <br>
Mitigation: Decline git mv migrations or config.py generation unless those changes are intended and can be reviewed like normal code. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leeshunee/skills/kinema-tdd-injector) <br>
- [Onboarding guide](references/ONBOARDING.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instruction-file drafts with setup prompts and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces repository-level CLAUDE.md or AGENTS.md guidance from a questionnaire and requires user review before keeping changes.] <br>

## Skill Version(s): <br>
1.4.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
