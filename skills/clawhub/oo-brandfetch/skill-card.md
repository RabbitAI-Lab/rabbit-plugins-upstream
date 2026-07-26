## Description: <br>
Brandfetch (brandfetch.com). Use this skill for ANY Brandfetch request: searching and reading brand data through an OOMOL-connected Brandfetch account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve Brandfetch brand profiles and resolve transaction labels through an OOMOL-connected Brandfetch account. It is suited for brand enrichment, merchant identification, and lookup workflows that should avoid direct Brandfetch API token handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The first-time setup path installs the oo CLI with a remote installer. <br>
Mitigation: Review the oo CLI installer before running the setup command, as recommended by the security guidance. <br>
Risk: Brandfetch lookups may use the user's OOMOL connection and account credits. <br>
Mitigation: Install and run the skill only when Brandfetch access through an OOMOL-connected account is intended; stop and resolve billing or credit errors before retrying. <br>
Risk: Connector action schemas can change over time. <br>
Mitigation: Fetch the live Brandfetch connector schema before constructing each action payload. <br>


## Reference(s): <br>
- [ClawHub Brandfetch skill page](https://clawhub.ai/oomol/skills/oo-brandfetch) <br>
- [Publisher profile: oomol](https://clawhub.ai/user/oomol) <br>
- [Brandfetch homepage](https://brandfetch.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution; command responses are JSON objects with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
