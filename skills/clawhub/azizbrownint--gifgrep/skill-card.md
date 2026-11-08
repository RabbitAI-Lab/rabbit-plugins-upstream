## Description:

Search GIF providers with CLI/TUI, download results, and extract stills/sheets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-producing agents use this skill to search Tenor or Giphy with gifgrep, preview or download GIFs, and extract still images or frame sheets for review, documentation, pull requests, and chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on mutable third-party install sources for the gifgrep CLI.

Mitigation: Install only from trusted upstream sources and review or pin the Go module or Homebrew formula version where possible.

Risk: Provider API keys can be exposed if supplied unnecessarily or logged in agent workflows.

Mitigation: Provide GIPHY_API_KEY or TENOR_API_KEY only when those providers are intended, and handle the keys as secrets.

Risk: Downloaded or recommended GIF URLs may be unavailable, mislabeled, non-animated, or unsuitable for local project use.

Mitigation: Verify successful resolution, GIF content type, animation, attribution, license, and source URL before using an asset; copy assets locally when hotlinking is not appropriate.

## Reference(s):

- [gifgrep homepage](https://gifgrep.com)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/gifgrep)
- [Homebrew install source: steipete/tap/gifgrep](https://github.com/steipete/homebrew-tap)
- [Go module install source: github.com/steipete/gifgrep/cmd/gifgrep](https://pkg.go.dev/github.com/steipete/gifgrep/cmd/gifgrep)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON, URL, GIF, still image, or sprite sheet outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the gifgrep CLI; GIPHY_API_KEY or TENOR_API_KEY may be used for provider access.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
