## Description:

AnySearch lets agents search AnySearch data sources, run batch searches, extract cleaned Markdown from HTML pages, and discover vertical search domains through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run AnySearch search, batch search, page extraction, and vertical-domain discovery tasks through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can execute downloaded oo CLI installer scripts with the user's account privileges.

Mitigation: Review the setup path before installation, trust the OOMOL installer endpoint before use, and prefer a verified, version-pinned, or package-manager-based oo CLI installation when available.

Risk: AnySearch actions depend on an OOMOL-connected account and may fail when authentication, connection scopes, credentials, app readiness, or billing are not current.

Mitigation: Run setup or account remediation only after an action fails with the matching error, then reconnect, refresh credentials, or resolve billing before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-anysearch)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [AnySearch homepage](https://anysearch.com/home)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON responses, and oo CLI shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [batch_search supports up to five parallel AnySearch queries; extract returns cleaned Markdown from HTML pages.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
