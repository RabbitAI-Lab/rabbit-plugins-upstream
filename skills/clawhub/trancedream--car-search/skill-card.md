## Description:

Acts as a used-car buying advisor that analyzes buyer needs, searches multiple Chinese used-car platforms, compares vehicle listings, and estimates car loan payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trancedream](https://clawhub.ai/user/trancedream)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search used-car listings, compare vehicle parameters across supported platforms, evaluate market fit, and calculate financing scenarios for purchase decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses scraping-style requests, browser impersonation, and anti-bot challenge handling against third-party used-car sites.

Mitigation: Review site terms before use, run the CLI in an isolated environment, and avoid high-volume or parallel requests.

Risk: Debug and HTTP trace logging can expose detailed request behavior while querying listing sites.

Mitigation: Keep debug and trace logging disabled unless needed for troubleshooting, and review logs before sharing them.

Risk: Dependency installation through uv sync may resolve dependencies from the network.

Mitigation: Prefer a committed lockfile or pinned dependencies before allowing dependency installation in production environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/trancedream/skills/car-search)
- [Adapter reference](references/adapters.md)
- [car-cli README](scripts/README.md)
- [uv documentation](https://docs.astral.sh/uv/)
- [Dongchedi](https://www.dongchedi.com)
- [Che168](https://www.che168.com)
- [Guazi](https://www.guazi.com)
- [Youxinpai](https://www.youxinpai.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional shell commands and structured listing data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use JSON, YAML, table, or CSV outputs from the bundled car-cli when gathering listing evidence.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
