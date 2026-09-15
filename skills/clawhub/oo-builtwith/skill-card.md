## Description:

BuiltWith helps agents query BuiltWith technology intelligence through OOMOL's oo CLI using a connected BuiltWith account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to retrieve BuiltWith domain technology profiles, summaries, recommendations, redirect history, and social-profile domain matches through an OOMOL-connected BuiltWith account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags direct execution of remote installer scripts in the setup path.

Mitigation: Review, pin, or integrity-verify the oo CLI installation path, and do not allow agents to automatically run curl|bash or irm|iex setup commands.

Risk: BuiltWith lookups depend on OOMOL authentication, a connected BuiltWith account, valid credentials, and available billing credit.

Mitigation: Run setup only after a matching failure, and have a human sign in, connect or refresh the account, or resolve billing before retrying.

## Reference(s):

- [ClawHub BuiltWith skill page](https://clawhub.ai/oomol/skills/oo-builtwith)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [BuiltWith connection setup](https://console.oomol.com/app-connections?provider=builtwith)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash and PowerShell examples, plus JSON CLI results from connector actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only BuiltWith connector actions are run through the oo CLI after inspecting the live action schema.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
